import json
import os
from time import time
import requests
import time
#Токен доступа
access_token ="ab29852fe44a3d1edac474248bacac87f25f2b6e87fe7234762b696aa051b5370dc770270766315e05345"
#Параметры метода wall.get
group_name = "meowkyit"
count = input('Введите необходимое колличество постов')
ver_vk_api = '5.131'
offset = 0
#Параметры метоода wall.getComments
owner_id = -1530418941
post_id = 0
count_coments = 100
need_likes = 1
preview_length = 0
#start_comment_id =[]
#Получение постов со стены
url =f"https://api.vk.com/method/wall.get?domain={group_name}&count={count}&offset={offset}&access_token={access_token}&v={ver_vk_api}"
print(url)
req=requests.get(url)
src = req.json()
posts = src["response"]["items"]
   
#Создание директории

if os.path.exists(f"{group_name}"):
    print(f'Директоррия с именем: {group_name} существует')
else:
    os.mkdir(group_name)
#Создание json файла с данными со стены сообщества с именем {groupe_name} 

with open(f"{group_name}/{group_name}.json",'w',encoding="utf-8") as file:
    json.dump(src,file,indent=4,ensure_ascii= False)

fresh_posts_id = []
posts = src["response"]["items"] 
for fresh_post in posts:
    fresh_post = fresh_post[fresh_post]
    fresh_posts_id.append(fresh_post)