import requests
import configparser

group_name = ''
owner_id = -153041894
comment_id = 156921
offset = 0
post_id =  156919
count = 10
need_likes = 1
access_token = config.get()

url_type_1 = 'https://api.vk.com/method/wall.get'
url_type_2 = 'https://api.vk.com/method/wall.getComments'
url_type_3 = 'https://api.vk.com/method/wall.getComment'

payload_1 = {'domain': {group_name},  
            'count': {count}, 
            'offset': {offset},
            'access_token':{access_token},
            'v':'5.131'}

payload_2 = {'owner_id': {owner_id}, 
            'post_id': {post_id}, 
            'count': {count}, 
            'need_likes': {need_likes},
            'preview_length': 0,
            'access_token':{access_token},
            'v':'5.131'}

payload_3 = {'owner_id': {owner_id}, 
            'comment_id': {comment_id}, 
            'access_token':{access_token},
            'v':'5.131'}




r = requests.get(url_type_1,params = payload_1)
print(r)


r = requests.get(url_type_2,params = payload_2)
print(r)


r = requests.get(url_type_3,params = payload_3)
print(r)
src = r.json()
print(src)




