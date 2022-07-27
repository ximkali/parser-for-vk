#https://oauth.vk.com/blank.html#access_token=ab29852fe44a3d1edac474248bacac87f25f2b6e87fe7234762b696aa051b5370dc770270766315e05345&expires_in=0&user_id=191075990
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

#Получение id постов из группы с именем {groupe_name}
fresh_posts_id = []
posts = src["response"]["items"] 
for fresh_post_id in posts:
    fresh_post_id = fresh_post_id["id"]
    fresh_posts_id.append(fresh_post_id)

print(fresh_posts_id)

#Создание json файла с id записей 
with open(f"{group_name}/ID posts from {group_name}.json",'w',encoding="utf-8") as file:
    json.dump(fresh_posts_id,file,indent=4,ensure_ascii= False)

# Cоздание url для получение комментариев с постов 
url_list = []
for id_post in fresh_posts_id:
    post_id = str(id_post)
    url =f"https://api.vk.com/method/wall.getComments?owner_id={owner_id}&post_id={post_id}&count={count}&need_likes={need_likes}&preview_length={preview_length}&access_token={access_token}&v={ver_vk_api}"
    url_list.append(url)

#Создание json файла с url для доступа к коментам по id записей 
with open(f"{group_name}/URL for get comments from {group_name}.json",'w',encoding="utf-8") as file:
    json.dump(url_list,file,indent=4,ensure_ascii= False)

# Запросы к полученным URL с коментами к постам записей 
for adress in url_list:
    url = adress
    req = requests.get(url)
    time.sleep(1)
    src = req.json()

# Получаем ID коментариев и ответов на комментарии

comments = src["response"]["items"]
fresh_comments_id = [] 
for fresh_comemnt_id in comments:
    fresh_comemnt_id = fresh_comemnt_id["id"]
    fresh_comments_id.append(fresh_comemnt_id)
    print(f'ID Комментариев к посту{fresh_comments_id}')

# Cоздание url для получение комментария к записи 
url_get_comment_list = []
for id_comment_from_post in fresh_comments_id:
    post_id = str(id_comment_from_post)
    url =f"https://api.vk.com/method/wall.getComment?owner_id={owner_id}&comment_id={post_id}&access_token={access_token}&v={ver_vk_api}"
    url_get_comment_list.append(url)
    print(url_get_comment_list)

# Запросы к полученным URL

for adress in url_get_comment_list:
    url = adress
    req = requests.get(url)
    src = req.json()
comment = src['response']['items']




fresh_comment = [] 
comment=src['response']['items']
for fresh_comemnt in comment:
    fresh_comemnt = fresh_comemnt["text"]
    fresh_comment.append(fresh_comemnt)
    print(f'Комментарий к посту к посту {fresh_comemnt}')



