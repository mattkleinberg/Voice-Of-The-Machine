import discord
import asyncio


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
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!users'):
        tmp = []
        usrs = client.get_all_members()
        for usr in usrs:
            tmp.append(str(usr.display_name))
        msg = ", ".join(tmp)
        await client.send_message(message.channel, msg, tts=True)
    elif message.content.startswith('!datass'):
        await client.send_message(message.channel, 'http://imgur.com/gallery/Ns7ywcX')
    elif message.content.startswith('!texttest'):
        for c in message.server.channels:
            print('name: {0}. type: {1}'.format(c.name, c.type))

@client.event
async def on_voice_state_update(before, after):
    if after.voice.voice_channel:
        server = after.server
        msg = str(after.display_name) + ' joined ' + after.voice.voice_channel.name
        tmp = await client.send_message(server, msg, tts=True)
        await client.delete_message(tmp)

client.run('token')
