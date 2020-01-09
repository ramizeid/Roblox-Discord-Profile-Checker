import urllib
import requests
import os
import time

profile = urllib.request.urlopen('https://www.roblox.com/users/36569569/profile')
profile_data = str(profile.read())
print(profile_data)

join_date = profile_data.find("Join Date<p class=text-lead")
after_join_date = profile_data.find("<li class=profile-stat><p class=text-label>Place Visits")

followed_lead = profile_data.find('data-followerscount=')
after_followed_lead = profile_data.find(' data-followingscount=')

following_lead = profile_data.find('data-followingscount=')
after_following_lead = profile_data.find(' data-acceptfriendrequesturl=')

pfp_lead = profile_data.find('<meta property=og:image content=https://tr.rbxcdn.com')
after_pfp_lead = profile_data.find('><meta property=fb:app_id')

print(join_date)
print(after_join_date)
print(profile_data[join_date + 28:after_join_date])
print(profile_data[followed_lead + 20:after_followed_lead])
print(profile_data[following_lead + 21:after_following_lead])

pfp_url = profile_data[pfp_lead + 32:after_pfp_lead]
user_pfp = urllib.request.urlretrieve(pfp_url, 'user_pfp.png')
# time.sleep(5)
# os.remove('user_pfp.png')

# urllib.request.urlretrieve('https://www.roblox.com/Thumbs/Avatar.ashx?x=100&y=100&username=%3CJoyValor%3E', 'test.png')

