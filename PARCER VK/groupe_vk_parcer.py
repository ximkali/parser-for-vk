from re import search
from time import time
from urllib import response
import requests
import time
#Токен доступа
access_token ="ab29852fe44a3d1edac474248bacac87f25f2b6e87fe7234762b696aa051b5370dc770270766315e05345"
#Параметры метода wall.get

ver_vk_api = '5.131'
offset = 0
#Параметры метоода group.search
search_string = input("Введите ключевое слов для поиска")
vk_groupe_type = input("Выберете тип сообщества для поиска: 1) Группа; 2) Страница; 3) Событие")
match vk_groupe_type:
    case"1":
        vk_groupe_type = "group"
    case"2":
        vk_groupe_type = "page"
    case"3":
        vk_groupe_type = "event"
    case _:
        print("Undiferend type")


post_id = 0
count_groups = 1000
need_likes = 1
preview_length = 0
#start_comment_id =[]
#поиcк группы
url =f"https://api.vk.com/method/groups.search?q={search_string}&type={vk_groupe_type}&count={count_groups}&offset={offset}&access_token={access_token}&v={ver_vk_api}"
#print(url)
req=requests.get(url)
src = req.json()
# print(src)

fresh_groupe_id = []
posts = src["response"]["items"] 
for groupe_id in posts:
    groupe_id = groupe_id["id"]
    fresh_groupe_id.append(groupe_id)

params_fields = str()

url = f"https://api.vk.com/method/groups.getById?group_ids={fresh_groupe_id}&fields=city,country,members_count&access_token={access_token}&v={ver_vk_api}"
#print(url)
req=requests.get(url)
src = req.json()
string_info = ''

for x in src["response"]:
    try:
        string_info = x['id'],x['name'],x["screen_name"],x['members_count'],x['city']["title"],x['country']["title"]
        print(string_info)
    except:
        string_info = x['id'],x['name'],x["screen_name"],x['members_count']
        print(string_info)
        continue

member_count = 1000



for groupe_id_vk in fresh_groupe_id:
    groupe_id = groupe_id_vk
    url = f"https://api.vk.com/method/groups.getMembers?group_id={groupe_id}&offset={offset}&count={member_count}&access_token={access_token}&v={ver_vk_api}"
    try:
        req = requests.get(url)
        time.sleep(0.6)
    except:
        print('Error')
    src = req.json()
    print('===========================================================================================================================================================================')
    try:
        print(src['response']['items'])
    except:
        print(src)






