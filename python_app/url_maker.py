from requests.compat import urljoin


    
method_list ={


    #Методы для работы с группами
    "groups.getAddresses": {
        'params':{
            'group_id':str,
            'address_ids':str,
            'count':int,
            'filds':{
                'base_filds':{
                    'id':True,
                    'name': True,
                    'screen_name': True,
                    'is_closed': True,
                    'type': True
                },
                'sub_filds':{
                    'activity': True,
                    'addresses': True,
                    'age_limits': True,
                    'city': True,
                    'contacts':False,
                    'country':True,
                    'description':True,
                    'links':False,
                    'members_count':False,
                    'place':False,
                    'verified':False,
                    'wall':False
                }
            }

        }
    },
    "groups.search": {
        'params':{
            'q':str,
            'type':str,
            'country_id':int,
            'city_id':str,
            'sort':{
                'defult':0,
                'members':6
            },
            'offset':str,
            'count':int
        }
    },
    "groups.getMembers": {
        'params':{
            'group_id':str,
            'groups.getMembers':['id_asc','id_desc','time_asc','time_desc'],
            'count':int,
            'offset':str,
            'filds':{
                'sub_filds':{
                    'city',
                    'country',
                    'domain',
                    'education',
                    'sex',
                    'relatives',

                    
                }
            }

        }
    },
    #Возвращает информацию о заданном сообществе или о нескольких сообществах.
    "groups.getById": {
        'params':{
            'group_ids':str, #Идентификаторы или короткие имена сообществ. Максимальное число идентификаторов — 500.
            'address_ids':str,
            'count':int,
            'filds':{
                'verified':False,
                
            }

        }
    },
    #Методы для работы с поиском
    "search.getHints": {
        'params':{
            'group_id':str,
            'address_ids':str,
            'count':int,
            'filds':{
                'base_filds':{

                },
                'sub_filds':{
                    
                }
            }

        }
    },
    #Методы для работы с пользовотелями
    # Возвращает расширенную информацию о пользователях. 
    'users.get': {
        'params':{
            'user_ids':str,
            'address_ids':str,
            'count':int,
            'filds':{
                #Содержимое поля «О себе» из профиля.
                'about':False,
                #Содержимое поля «Деятельность» из профиля.
                'activities':False,
                #Дата рождения
                'bdate':False,
                #Содержимое поля «Любимые книги» из профиля пользователя.
                'books':False,
                #Информация о карьере пользователя. Объект, содержащий следующие поля:
                'career':False,
                'city':False,
                'contacts':False,
                'country':False,
                'home_town':False,
                'personal':False,
                'sex':True
            }

        }
    },

    #Методы для работы с стенами сообществ
    'wall.getComments': {
        'params':{
            'owner_id':str,
            'post_id':str,
            'need_likes':1,
            'count':str,
            'offset':str,
            'preview_length':0,
            'filds':{
                'base_filds':{

                },
                'sub_filds':{
                    
                }
            }

        }
    },
    'wall.get': {
        'params':{
            'owner_id':str,
            'domain':str,
            'offset':int,
            'count':100,
            'filter':['owner','others','all'],
            'filds':{
                'base_filds':{

                },
                'sub_filds':{
                    
                }
            }

        }
    },
    #Методы для работы со статистикой ВК 
    'stats.get': {
        'params':{
            'group_id':str,
            'address_ids':str,
            'count':int,
            'filds':{
                'base_filds':{

                },
                'sub_filds':{
                    
                }
            }

        }
    },
    'stats.getPostReach': {
        'params':{
            'group_id':str,
            'address_ids':str,
            'count':int,
            'filds':{
                'base_filds':{

                },
                'sub_filds':{
                    
                }
            }

        }
    },
}




class URL:
    def __init__(self, PROTOCOL:str,DOMAIN:str,) -> None:
        self.PROTOCOL = PROTOCOL 
        self.DOMAIN = DOMAIN
        self._base = self.PROTOCOL + self.DOMAIN + '/'

    def add_method(self, method_name, ):
        self.url = self._base + method_name +'?'
        return self.url

    def add_agrs(self,*args,**kwargs):
        self.url = str(url) + args
        return self.url
    
    def __str__(self) -> str:
        print(self.url)

    

url = URL('https//','vk.api')
url_update = url.add_method('stats.getPostReach')
url_update.add_agrs("owner_id",'offset')

print(url_update)
    
    



