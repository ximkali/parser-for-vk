import configparser
import os

path = R'C:\Users\Дима\Desktop'
 
def createConfig(path):
    config = configparser.ConfigParser()
    config.add_section("vk access")
    config.set("vk access", "access_token", "ab29852fe44a3d1edac474248bacac87f25f2b6e87fe7234762b696aa051b5370dc770270766315e05345")
    config.set("vk access", "ver_vk_api", "5.131")
    
    config.add_section("wall.get")
    config.set("wall.get","owner_id","")
    config.set("wall.get","domain","")
    config.set("wall.get","count","10")
    config.set("wall.get","offset","0")
   
    config.add_section("wall.getComments")
    config.set("wall.getComments","owner_id","")
    config.set("wall.getComments","post_id","")
    config.set("wall.getComments","count ","10")
    config.set("wall.getComments","need_likes","1")
    config.set("wall.getComments","preview_length","0")

    config.add_section("wall.getComment")
    config.set("wall.getComment","owner_id","")
    config.set("wall.getComment","comment_id","")

    config.add_section("MySQL_DB")
    config.set("MySQL_DB","host","")
    config.set("MySQL_DB","user","")
    config.set("MySQL_DB","password","")
    
    
    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    
    if not os.path.exists(path):
        createConfig(path)
    
    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    """
    Print out a setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )
    
    print(msg)
    return value

def update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)
 
 
def delete_setting(path, section, setting):
    """
    Delete a setting
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)