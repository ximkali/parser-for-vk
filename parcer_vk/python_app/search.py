import json
from unittest import result
import requests
import configparser
import datetime
from conf import logger

"""
Программа для получения информации из социальной сети ВКонтакте

"""

config = configparser.ConfigParser()
session_ = requests.Session()
dt = datetime.datetime.now


def input_search_word():
    search_string = input("Input key word for search")
    config.read('conf/config.ini')
    config.set('group.search', 'q', f'{search_string}')
    with open('conf/config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)


def get_param_dict_from_config(method_name: str) -> dict:
    """Функция для формирования словаря с параметрами для запроса к API из конфигурационного файла программы"""
    sections = config.sections()
    if method_name in sections:
        return dict(config.items(method_name) + config.items(section='vk_access'))
    else:
        logger.dbug_logger('Ошибка')


def normolize_user_input(user_input: str) -> str:
    normolize_string = user_input.lower
    normolize_string = normolize_string.r


def sub_fild():
    filter_fild = ''


def get_filter_dict_from_config(filter_fild: str) -> dict:
    sections = config.sections()
    if 'sub_info' in sections:
        return
    else:
        logger.dbug_logger('Ошибка')


def save_response(src: json):
    """Функция для сохранения ответа сервера во временную директорию"""
    with open(f'Search results-key word-{config.get()}-{dt}.json', 'w', encoding='utf-8') as data_fiel:
        json.dump(src, indent=4, ensure_ascii=False)


def get_element_response(src: json, name_element):
    """Функция для получения всех значений элементов из ответа сервера"""
    result = [item[f'{name_element}'] for item in src['response']['items']]
    return f'{name_element}:' + result


def get_group_id(src: json) -> list:
    """Функция для получения всех значений элемента[id] из ответа сервера"""
    result = [item['id'] for item in src['response']['items']]
    return result


def get_group_name(src: json) -> list:
    """Функция для получения всех значений элемента[name] из ответа сервера"""
    result = [item['name'] for item in src['response']['items']]
    return result


def get_group_name(src: json) -> list:
    """Функция для получения всех значений элемента[type] из ответа сервера"""
    result = [item['type'] for item in src['response']['items']]
    return result


def get_all_info(src: json):
    """Функция для получения основной информации из ответа сервера"""
    for item in src['response']['items']:
        item = item['id'], item['name'], item['type']
        data = list(item)
        print(data)


if __name__ == '__main__':
    pass
