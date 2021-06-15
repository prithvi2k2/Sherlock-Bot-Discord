import os
from dotenv import load_dotenv
load_dotenv('.env')


from subprocess import run
import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(('$slock', '$sherlock')):
        print("content:",message.content)
        if len(message.content.strip().split())>=2:
            await message.channel.send('Hello, u need patience, i might take some time to hunt down users...\nAlso consider donating, who knows I might speed up!!'  )
            users=message.content.strip().split()
            run(['python','.\sherlock.py',*users[1:]])
            for user in users[1:]:
                await message.author.send(".txt file for user {}:".format(user),file=discord.File('{}.txt'.format(user)))
                os.remove('{}.txt'.format(user))
                # with open('{}.txt'.format(user),'r') as f:
                #     data=f.read()
                #     await message.channel.send(data)
                #     os.remove(f)
            print('[',*users[1:],'] <-- Successful HUNT!!')


        else:
            await message.channel.send('You need to enter atleast one username to continue the quest...')
            await message.channel.send('Example: $sherlock user1 user2 user3 ... (one is enough or else you will see me struggling)')
            await message.channel.send("Consier donating if you don't want me to struggle!")


            


client.run(os.getenv('TOKEN'))