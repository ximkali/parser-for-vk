import json
import os
from re import search
from time import time
from urllib import response
import requests
import time
#Токен доступа
access_token ="ab29852fe44a3d1edac474248bacac87f25f2b6e87fe7234762b696aa051b5370dc770270766315e05345"
#Параметры метода wall.get
search_string = "СГУ"
ver_vk_api = '5.131'
offset = 0
#Параметры метоода group.search
vk_groupe_type = "group"
post_id = 0
count_coments = 100
need_likes = 1
preview_length = 0
#start_comment_id =[]
#поиcк группы
url =f"https://api.vk.com/method/groups.search?q={search_string}&type={vk_groupe_type}&count={count_coments}&offset={offset}&access_token={access_token}&v={ver_vk_api}"
#print(url)
req=requests.get(url)
src = req.json()

#print(src["response"]["items"])

fresh_groupe_id = []
posts = src["response"]["items"] 
for groupe_id in posts:
    groupe_id = groupe_id["id"]
    fresh_groupe_id.append(groupe_id)

#print(fresh_groupe_id)

groupe_id = 81186882
count_members = 1000

url = f"https://api.vk.com/method/groups.getById?group_ids={fresh_groupe_id}&fields=city,country,members_count&access_token={access_token}&v={ver_vk_api}"
#print(url)
members_count_more_thousand = []
req=requests.get(url)
src = req.json()
src1 = (src['response'])
for members_count in src1:
    members_count = members_count['members_count']
    if members_count > 1000:
        members_count_more_thousand.append(members_count)
    else:
        member_count = 1000
        url = f"https://api.vk.com/method/groups.getMembers?group_id={groupe_id}&offset={offset}&count={member_count}&access_token={access_token}&v={ver_vk_api}"
        req=requests.get(url)
        time.sleep(0.9)
        src = req.json()
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(src)



url = f"https://api.vk.com/method/groups.getMembers?group_id={groupe_id}&count={members_count}&access_token={access_token}&v={ver_vk_api}"
#print(url)

#req=requests.get(url)
#src = req.json()
#print(src["response"]["items"] )
