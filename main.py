import discord
from discord.ext import commands
import datetime
import time
import pyblox3
import urllib
import requests

assets = pyblox3.Assets
friends = pyblox3.Friends
groups = pyblox3.Groups
users = pyblox3.Users
http = pyblox3.Http

client = commands.Bot(command_prefix='!')
client.remove_command('help')
start_time = datetime.datetime.utcnow()

TOKEN = 'NjYzOTI4MjAwMTQ0ODc5NjI3.XhPpYg.TJABxkOr1VpXsEoME8Ee5thsEIo'


# ---------------------------------------
# Bot Initialization
# ---------------------------------------
@client.event
async def on_ready():
    print('Bot is ready.')


# ---------------------------------------
# Background Check Command
# ---------------------------------------
@client.command()
async def bc(ctx, *, user):
    user_not_found_embed = discord.Embed(
        color=discord.Color.dark_red(),
        title=f"User {user} not found.",
        timestamp=datetime.datetime.utcnow()
    )

    waiting_embed = discord.Embed(
        color=discord.Color.dark_purple(),
        title=f"Please wait while the data is being processed. This may take a couple of minutes.",
        timestamp=datetime.datetime.utcnow()
    )

    try:
        target_username = users.User(user).Username
        user_id = users.User(user).Id
        await ctx.send(embed=waiting_embed)
    except KeyError:
        print(f'User {user} not found.')
        await ctx.send(embed=user_not_found_embed)
        return

    friend_embed1 = discord.Embed(
        color=discord.Color.orange(),
        title=f"{target_username}'s Friend Information",
        timestamp=datetime.datetime.utcnow()
    )

    friend_embed2 = discord.Embed(
        color=discord.Color.orange(),
        # title=f'Friend Information on {target_username}',
        timestamp=datetime.datetime.utcnow()
    )

    friend_embed3 = discord.Embed(
        color=discord.Color.orange(),
        # title=f'Friend Information on {target_username}',
        timestamp=datetime.datetime.utcnow()
    )

    friend_embed4 = discord.Embed(
        color=discord.Color.orange(),
        # title=f'Friend Information on {target_username}',
        timestamp=datetime.datetime.utcnow()
    )

    group_embed = discord.Embed(
        color=discord.Color.dark_green(),
        title=f"{target_username}'s Group Information",
        timestamp=datetime.datetime.utcnow()
    )

    # FRIENDS BACKGROUND CHECK

    user_friends1 = []
    user_friends2 = []
    user_friends3 = []
    user_friends4 = []

    for page in range(1, 5):
        for i in friends.friendList(user_id, page):
            if len(user_friends1) <= 50:
                user_friends1.append(i)
            elif len(user_friends2) <= 50:
                user_friends2.append(i)
            elif len(user_friends3) <= 50:
                user_friends3.append(i)
            elif len(user_friends4) <= 50:
                user_friends4.append(i)

    number_of_friends = len(user_friends1) + len(user_friends2) + len(user_friends3) + len(user_friends4)

    for friend in user_friends1:
        try:
            friend_id = users.User(friend).Id
            friend_embed1.add_field(name=friend, value=f'[Profile](https://www.roblox.com/users/{friend_id}/profile)', inline=True)
        except:
            pass

    if len(user_friends2) != 0:
        for friend in user_friends2:
            try:
                friend_id = users.User(friend).Id
                friend_embed2.add_field(name=friend, value=f'[Profile](https://www.roblox.com/users/{friend_id}/profile)', inline=True)
            except:
                pass

    if len(user_friends3) != 0:
        for friend in user_friends3:
            try:
                friend_id = users.User(friend).Id
                friend_embed3.add_field(name=friend, value=f'[Profile](https://www.roblox.com/users/{friend_id}/profile)', inline=True)
            except:
                pass

    if len(user_friends4) != 0:
        for friend in user_friends4:
            try:
                friend_id = users.User(friend).Id
                friend_embed4.add_field(name=friend, value=f'[Profile](https://www.roblox.com/users/{friend_id}/profile)', inline=True)
            except:
                pass

    # GROUPS BACKGROUND CHECK

    user_groups = groups.groupList(user_id)
    user_groups = str(user_groups)
    user_groups = user_groups.lstrip("b'")
    user_groups = user_groups.lstrip('[')
    user_groups = user_groups.rstrip("]'")
    user_groups = user_groups.split('}')

    u_group = []
    user_group_info = []

    for i in user_groups:
        i += '}'
        i = i.lstrip(',')
        i = i.lstrip('}')
        u_group.append(i)

    u_group.pop(len(u_group) - 1)
    number_of_groups = len(u_group)

    for group in u_group:
        location = group.find('IsPrimary') - 2
        group = group[:location]
        group += '}'
        group = eval(group)
        group_name = group['Name']
        group_id = group['Id']
        user_rank = group['Role']
        user_group_info.append(f'{group_name}, {group_id}, {user_rank}')

    for group in user_group_info:
        group = group.split(',')
        group_embed.add_field(name=f'{group[0]} - {group[1][1:]}', value=f'Rank: {group[2][1:]}', inline=True)

    # GENERAL BACKGROUND CHECK

    general_embed = discord.Embed(
        color=discord.Color.dark_blue(),
        title=f'General Information on {target_username}',
        timestamp=datetime.datetime.utcnow()
    )

    profile = urllib.request.urlopen(f'https://www.roblox.com/users/{user_id}/profile')
    profile_data = str(profile.read())

    join_date_lead = profile_data.find("Join Date<p class=text-lead")
    after_join_date_lead = profile_data.find("<li class=profile-stat><p class=text-label>Place Visits")

    followed_lead = profile_data.find('data-followerscount=')
    after_followed_lead = profile_data.find(' data-followingscount=')

    following_lead = profile_data.find('data-followingscount=')
    after_following_lead = profile_data.find(' data-acceptfriendrequesturl=')

    pfp_lead = profile_data.find('<meta property=og:image content=https://tr.rbxcdn.com')
    after_pfp_lead = profile_data.find('><meta property=fb:app_id')

    pfp_url = profile_data[pfp_lead + 32:after_pfp_lead]

    join_date = profile_data[join_date_lead + 28:after_join_date_lead]
    followers_count = profile_data[followed_lead + 20:after_followed_lead]
    following_count = profile_data[following_lead + 21:after_following_lead]

    following_count = following_count.replace(',', '')

    general_embed.set_thumbnail(url=pfp_url)
    general_embed.add_field(name='Creation Date', value=join_date, inline=True)
    general_embed.add_field(name='Friend Count', value=str(number_of_friends), inline=True)
    general_embed.add_field(name='Followers Count', value=str(followers_count), inline=True)
    general_embed.add_field(name='Following Count', value=str(following_count), inline=True)
    general_embed.add_field(name='Group Count', value=str(number_of_groups), inline=True)

    await ctx.send(embed=general_embed)
    await ctx.send(embed=friend_embed1)

    if len(user_friends2) != 0:
        await ctx.send(embed=friend_embed2)

    if len(user_friends3) != 0:
        await ctx.send(embed=friend_embed3)

    if len(user_friends4) != 0:
        await ctx.send(embed=friend_embed4)

    await ctx.send(embed=group_embed)

    print(f'Successfully background checked {target_username}')

client.run(TOKEN)
