import configparser

from pathlib import Path

config = configparser.ConfigParser()


def create_config():
    config.add_section("vk_authorize")
    config.set('vk_authorize', 'client_id', '')
    config.set('vk_authorize', 'display', 'page')
    config.set('vk_authorize', 'redirect_uri', '')
    config.set('vk_authorize', 'scope', '')
    config.set('vk_authorize', 'response_type', 'token')

    config.add_section("vk_access")
    config.set("vk_access", "access_token",
               "f5771c63f5771c63f5771c63bbf50c622cff577f5771c6397555119c2f4faf86e274da2")
    config.set("vk_access", "v", "5.131")

    config.add_section("wall.get")
    config.set("wall.get", "owner_id", "None")
    config.set("wall.get", "domain", "None")
    config.set("wall.get", "count", "10")
    config.set("wall.get", "offset", "0")

    config.add_section("wall.getComments")
    config.set("wall.getComments", "owner_id", "None")
    config.set("wall.getComments", "post_id", "None")
    config.set("wall.getComments", "count ", "10")
    config.set("wall.getComments", "need_likes", "1")
    config.set("wall.getComments", "preview_length", "0")

    config.add_section("wall.getComment")
    config.set("wall.getComment", "owner_id", "None")
    config.set("wall.getComment", "comment_id", "None")

    config.add_section("group.search")
    config.set("group.search", "q", "None")
    config.set("group.search", "type", "group,page,event")
    config.set("group.search", "country_id", "10")
    config.set("group.search", "city_id", "0")
    config.set("group.search", "sort", "0")
    config.set("group.search", "offset", "0")
    config.set("group.search", "count", "1000")

    config.add_section('groups.getById')
    config.set('groups.getById','group_id','')
    config.set('groups.getById','group_ids','')
 
    config.add_section('sub_info')
    config.set('sub_info','activity','activity')
    config.set('sub_info','addresses','addresses')
    config.set('sub_info','age_limits','age_limits')
    config.set('sub_info','city','city')
    config.set('sub_info','contacts','contacts')
    config.set('sub_info','country','country')
    config.set('sub_info','description','description')
    config.set('sub_info','members_count','members_count')

    config.add_section("connection_to_data_base")
    config.set("connection_to_data_base", "host", "None")
    config.set("connection_to_data_base", "user", "None")
    config.set("connection_to_data_base", "password", "None")

    with open("conf/config.ini", "w", encoding='utf-8') as configfile:
        config.write(configfile)




def create_logger_config():
    pass


create_config()
