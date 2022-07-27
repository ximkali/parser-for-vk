from re import search
from urllib import response
import requests
import configparser
#Токен доступа
access_token ="ab29852fe44a3d1edac474248bacac87f25f2b6e87fe7234762b696aa051b5370dc770270766315e05345"


#Параметры метода wall.get
group_id = group_name =  "ria"
count = 100
ver_vk_api = v = '5.131'
offset = 0

#Параметры метоода wall.getComments
comment_id = 156891

owner_id = -153041894
post_id = 156886
count_coments = 100
need_likes = 1
preview_length = 0

#Типы URL адрессов
url_type_1 = 'https://api.vk.com/method/wall.get'
url_type_2 = 'https://api.vk.com/method/wall.getComments'
url_type_3 = 'https://api.vk.com/method/wall.getComment'
url_type_4 = 'https://api.vk.com/method/groups.search'
url_type_5 = 'https://api.vk.com/method/groups.getById'
url_type_6 = 'https://api.vk.com/method/groups.getMembers'
url_type_7 = ''

def get_to_ulr(url_type):
    match url_type:
        case"url_type_1":
            requests.get(url_type_1,params = param_wall_get)
        case"url_type_2":
            requests.get(url_type_2,params = param_wall_getComments,timeout = 3,stream = True)
        case"url_type_3":
            requests.get(url_type_3,params = param_wall_getComment,timeout = 3,stream = True)
        case _:
           print("Undiferend type")

#Параметры метода wall.get
param_wall_get = {  'domain': {group_name},  
                    'count': {count}, 
                    'offset': {offset},
                    'access_token':{access_token},
                    'v' : {v}}

#Параметры метода wall.getComments
param_wall_getComments = {  'owner_id': {owner_id}, 
                            'post_id': {post_id}, 
                            'count': {count}, 
                            'need_likes': {need_likes},
                            'preview_length': {preview_length},
                            'access_token':{access_token},
                            'v' : {v}  }

#Параметры метода wall.getComment
param_wall_getComment = {   'owner_id': {owner_id}, 
                            'comment_id': {comment_id}, 
                            'access_token':{access_token},
                            'v' : {v} }

search_string = input()
vk_groupe_type = ''

param_groups_search = {     'q': {search_string},
                            'type':{vk_groupe_type},
                            'count': {count},  
                            'access_token':{access_token},
                            'v' : {v} }

fresh_groupe_id = []

param_groups_getById = {     'group_ids': {fresh_groupe_id},
                            'fields':'city,country,members_count',  
                            'access_token':{access_token},
                            'v' : {v} }

count_members = 1000

param_groups_getMembers = { 'group_id': {group_id},
                            'count': {count_members},  
                            'access_token':{access_token},
                            'v' : {v} }


# #Получение записей со стены
r = requests.get(url_type_1,params = param_wall_get)
src = r.json()

#Получение набора комментариев к записе на стене сообщества 
r = requests.get(url_type_2,params = param_wall_getComments)
src = r.json()
print(src["response"]["items"])

#Получение информации о комментарии к записе на стене сообщества 
r = requests.get(url_type_3,params = param_wall_getComment)
print(r)
src = r.json()
