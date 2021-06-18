import discord
from subprocess import run
import os
from dont_die import dont_die
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


    #PUBLIC SEARCH
    if message.content.startswith('$search'):
        print("REQUEST:", message.content,'> requested by {}'.format(message.author.name))
        if len(message.content.strip().split()) >= 2:
            await message.reply('You need patience, I might take some time to hunt down users...\nAlso consider donating, who knows I might speed up!!')
            users = message.content.strip().split()[1:]
            for user in users:
                await message.reply('Searching for {}...'.format(user))
                run(['python', 'src/sherlock.py', user])
                await message.reply("Generated .txt file of TARGET {}:".format(user), file=discord.File('{}.txt'.format(user)))
                os.remove('{}.txt'.format(user))
                # Live printing to discord will be figured out later due to 4k chaar limit per msg of discord 
                # with open('{}.txt'.format(user),'r') as f:
                #     data=f.read()
                #     await message.channel.send(data)
                #     os.remove(f)
            await message.reply('Successfully processed your request!')
            print(users, ' <-- Successful PUBLIC SEARCH!! requested by {}'.format(message.author.name))
        else:
            await message.reply('Check usage guide...')
        #PRIVATE SEARCH
    elif message.content.startswith('$dm'):
        print("REQUEST:", message.content,'> requested by {}'.format(message.author.name))
        if len(message.content.strip().split()) >= 2:
            users = message.content.strip().split()[1:]
            await message.reply('Keep an eye on your DMs')
            await message.delete()
            await message.author.send('You need patience, I might take some time to hunt down users...\nAlso consider donating, who knows I might speed up!!')
            await message.author.send("YOUR REQUEST :> {}".format(message.content))
            for user in users:
                await message.author.send('Searching for {}...'.format(user))
                run(['python', 'src/sherlock.py', user])
                await message.author.send("Generated .txt file of TARGET {}:".format(user), file=discord.File('{}.txt'.format(user)))
                os.remove('{}.txt'.format(user))
                # Live printing to discord will be figured out later due to 4k chaar limit per msg of discord 
                # with open('{}.txt'.format(user),'r') as f:
                #     data=f.read()
                #     await message.channel.send(data)
                #     os.remove(f)
            await message.author.send('Successfully processed your request!')
            print(users, ' <-- Successful SEARCH!! requested by {}'.format(message.author.name))
        else:
            await message.reply('Check usage guide...')

dont_die()      #Efforts to keep bot alive 24/7
client.run(os.getenv('TOKEN'))
