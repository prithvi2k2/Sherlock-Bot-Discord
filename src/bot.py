import discord
from subprocess import run
import os
from dotenv import load_dotenv
load_dotenv('.env')


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$search'):
        print("REQUEST:", message.content,'| requested by {}'.format(message.author.name))
        if len(message.content.strip().split()) >= 2:
            await message.reply('You need patience, I might take some time to hunt down users...\nAlso consider donating, who knows I might speed up!!')
            users = message.content.strip().split()[1:]
            for user in users:
                await message.reply('Searching for {}'.format(user))
                run(['python', 'sherlock.py', user])
                await message.reply("Generated .txt file of TARGET {}:".format(user), file=discord.File('{}.txt'.format(user)))
                os.remove('{}.txt'.format(user))
                # with open('{}.txt'.format(user),'r') as f:
                #     data=f.read()
                #     await message.channel.send(data)
                #     os.remove(f)
            await message.reply('Successfully processed your request!')
            print(users, ' <-- Successful SEARCH!! requested by {}'.format(message.author.name))

        else:
            await message.reply('Check usage guide...')
        


client.run(os.getenv('TOKEN'))
