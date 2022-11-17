import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('conf/config.ini')

access_token = config.get('vk_access', 'access_token')
ver_vk_api = config.get('vk_access', 'ver_vk_api')


def get_param_dict_from_config(method_name: str) -> dict:
    sections = config.sections()
    if method_name in sections:
        return dict(config.items(method_name) + config.items(section='vk_access'))
    else:
        print('ER0R')


def pars_response():
    scr = response


param_dict = get_param_dict_from_config(method_name='wall.get')
print(param_dict)

url = 'https://api.vk.com/method/groups.search?'
session_ = requests.Session()

if __name__ == '__main__':
    response = session_.get(url, params=param_dict)
    src = response.json()
    print(src)
