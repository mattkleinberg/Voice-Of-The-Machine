import re
import discord
import asyncio
import tokens
from phonetic import phonetic


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!callme'):
        r = re.compile('!callme: .*')
        if r.match(message.content) is not None:
            sp = message.content.split('!callme: ', 1)[1]
            phon = phonetic.Phonetic()
            usr_p = phon.add_phon(str(message.author), sp)
            await client.send_message(message.server, usr_p)
        else:
            await client.send_message(message.server, 'Command does not match format. Format is !callme: YOUR TEXT HERE')

    if message.content.startswith('!callme_remove'):
        phon = phonetic.Phonetic()
        stats = phon.del_phon(str(message.author))
        await client.send_message(message.server, stats)

@client.event
async def on_voice_state_update(before, after):
    if after.voice.voice_channel and before.voice.voice_channel is None:
        server = after.server
        phon = phonetic.Phonetic()
        usr_phon = phon.find_name(after)
        msg = str(usr_phon) + ' joined ' + after.voice.voice_channel.name
        tmp = await client.send_message(server, msg, tts=True)
        await client.delete_message(tmp)
    elif after.voice.voice_channel is None:
        server = before.server
        phon = phonetic.Phonetic()
        usr_phon = phon.find_name(before)
        msg = str(usr_phon) + ' left the server'
        tmp = await client.send_message(server, msg, tts=True)
        await client.delete_message(tmp)

client.run(tokens.dt)
