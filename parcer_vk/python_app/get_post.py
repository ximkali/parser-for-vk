from tokenize import group
from urllib import response
import requests

access_token = "vk1.a.sqNszMOOdSHzehnpU1rK9KGA0x55c6lPw55XXEgKN9hj9CZ9dQxSIHYbzz5zgyrJhKkAVmyriAEQ2e50wJfIHsmKzdDggdpf3X6h7bUYaX8C5dtx_HwDMg9SmzTYLIJYFco8WmUHjOAG5B53WD0_QfIqMEpsgmQQO1_LxV6GZCULYqUhON-mg7NBDe724BRn"
v = "5.131"
id  = 'eto_yugansk_detka'
count = 20
n = 1
offset = 0


while True:
    param = {'domain':f'{id}','sort':'id_asc','offset':f'{offset}','count':20,'access_token':f'{access_token}','v':'5.131'}
    
    r = requests.get(url='https://api.vk.com/method/wall.get?',params=param)
    src = r.json()
    for text in src['response']['items']:
        print(text['id'],text['owner_id'],text['text'] + '\n') 
        offset = count*n
        print(offset)
        n+=1
        print(n)