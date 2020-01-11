import discord
from discord.ext import commands
import pyblox3
import datetime
import time
import os

TOKEN = 'NjY1MzYwNjI4ODczMDM1ODE3.XhkfgQ.V09X90jHYU4qYKHbaJy1-LySk3M'

client = commands.Bot(command_prefix='.', self_bot=True)
client.remove_command('help')
start_time = datetime.datetime.utcnow()

# ---------------------------------------
# Bot Initialization
# ---------------------------------------
@client.event
async def on_ready():
    print('Discord integration is ready.')

    channel = client.get_channel(665339313931943941)
    user_id = (open('roblox_id.txt')).read()
    print(user_id)

    if len(user_id) == 0:
        pass
    else:
        user_id = int(user_id)

        await channel.send(f'!reverselookup {user_id}')
        time.sleep(2)

        async for message in channel.history(limit=1):
            msg = message.content
            print(msg)

        msg_1 = msg.find('(')
        msg_2 = msg.find(')')

        user_discord = msg[msg_1 + 1:msg_2]

        if user_discord[0] == "<" or user_discord[0] == "!":
            discord_user_file = open('discord_user.txt', 'w')
            discord_user_file.write('Not found')
            print('Not found')
            discord_user_file.close()
            # await channel.send('Cancel')

            roblox_id_file = open('roblox_id.txt', 'w')
            roblox_id_file.write('')
            roblox_id_file.close()
        else:
            discord_user_file = open('discord_user.txt', 'w')
            discord_user_file.write(user_discord)
            print(user_discord)
            discord_user_file.close()

            roblox_id_file = open('roblox_id.txt', 'w')
            roblox_id_file.write('')
            roblox_id_file.close()
            time.sleep(2)

        user_id = (open('roblox_id.txt')).read()

        while len(user_id) != 0:
            pass

    print('restarting discord integration')

# ------ TEST ---------

client.run(TOKEN, bot=False)
os.system('discord-integration.py')
