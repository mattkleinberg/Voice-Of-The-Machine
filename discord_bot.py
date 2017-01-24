import discord
import asyncio
import tokens


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        print(message.timestamp)

@client.event
async def on_voice_state_update(before, after):
    if after.voice.voice_channel and before is None:
        server = after.server
        msg = str(after.display_name) + ' joined ' + after.voice.voice_channel.name
        tmp = await client.send_message(server, msg, tts=True)
        await client.delete_message(tmp)

client.run(tokens.dt)
