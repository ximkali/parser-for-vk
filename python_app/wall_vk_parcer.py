import requests
from groupe_vk_parcer import session_
from groupe_vk_parcer import config
from urls import url_wall_get



def input_group_name():
    group_name = input("Input key word for search")
    config.read('conf/config.ini')
    config.set('wall.get', 'domain', f'{group_name}')
    with open('conf/config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)


def get_param_dict_from_config(method_name) -> dict:
    """Функция для формирования словаря с параметрами для запроса к API из конфигурационного файла программы"""
    sections = config.sections()
    if method_name in sections:
        config.read('/conf/config.ini')
        return dict(config.items(method_name) + config.items(section='vk_access'))
    else:
        print('Ошибка')

input_group_name()
param_dict = get_param_dict_from_config(method_name='wall.get')
r = requests.get(url=url_wall_get,params=param_dict)
r.json
print(r)

