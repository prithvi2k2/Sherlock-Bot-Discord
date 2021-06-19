import discord
from subprocess import run
import os
from dont_die import dont_die
from dotenv import load_dotenv
load_dotenv('.env')
from time import time

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
        print(f'REQUEST: {message.content} > by {message.author.name}')
        if len(message.content.strip().split()) >= 2:
            ETA=time()   #Calculate total time and print to console on completion
            await message.reply('You need patience, I might take some time to hunt down users...\nAlso consider donating, who knows I might speed up!!')
            users = message.content.strip().split()[1:]
            for user in users:
                await message.reply(f'Searching for {user}...')
                timer=time()    
                run(['python', 'src/sherlock.py', user])
                timer=round(time()-timer,2)     #Total time taken per userLookUp
                await message.reply(f'Generated .txt file of TARGET {user} in {timer}s', file=discord.File(f'{user}.txt'))
                os.remove('{}.txt'.format(user))
            await message.reply('Successfully processed your request!')
            print(f'{users} <-- Successful SEARCH!! for {message.author.name} in {round(time()-ETA,2)}s')
        else:
            await message.reply('Check usage guide...')
    #QUICK SEARCH TIMEOUT 1 second
    elif message.content.startswith('$quik'):
        print("REQUEST:", message.content,f'> requested by {message.author.name}')
        if len(message.content.strip().split()) >= 2:
            ETA=time()
            await message.reply('Consuming adrenaline, FLASH!!!\ngotta ditch slow sites, might not be accurate!!')
            users = message.content.strip().split()[1:]
            for user in users:
                await message.reply(f'Searching for {user}...')
                timer=time()
                run(['python', 'src/sherlock.py', '--timeout', '1', user])
                timer=round(time()-timer,2)
                await message.reply(f'Generated .txt file of TARGET {user} in {timer}s', file=discord.File(f'{user}.txt'))
                os.remove(f'{user}.txt')
            await message.reply('Successfully processed your request!')
            print(f'{users} <-- Successful QUICK SEARCH!! for {message.author.name} in {round(time()-ETA,2)}s')
        else:
            await message.reply('Check usage guide...')

dont_die()      #Efforts to keep bot alive 24/7
client.run(os.getenv('TOKEN'))
