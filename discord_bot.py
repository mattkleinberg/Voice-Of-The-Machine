import discord
import asyncio
import tokens
from critical_role.reddit import RedditBot


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
        RedditBot().get_time_till_cr(message.timestamp)

@client.event
async def on_voice_state_update(before, after):
    print(after.voice.voice_channel.is_private)
    if after.voice.voice_channel and before.voice.voice_channel is None:
        server = after.server
        msg = str(after.display_name) + ' joined ' + after.voice.voice_channel.name
        tmp = await client.send_message(server, msg, tts=True)
        await client.delete_message(tmp)
    elif after.voice.voice_channel is None:
        server = before.server
        msg = str(after.display_name) + ' left the server'
        tmp = await client.send_message(server, msg, tts=True)
        await client.delete_message(tmp)

client.run(tokens.dt)
