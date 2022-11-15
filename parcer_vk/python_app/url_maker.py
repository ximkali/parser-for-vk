from requests.compat import urljoin
import enum

class ApiUrl:


    def __init__(self,DOMEN:str,method_name:str,) -> None:
        
        self._PROTOCOL = 'https://api.vk.com'
        self.DOMEN = 'api.vk.com'
        self.method_name = method_name
    

    def _make_url(self):
        _ulr = urljoin(self._PROTOCOL,self.method_name)
        return _ulr
    
class MethodsName(enum.Enum):


    #Методы для работы с группами
    "groups.getAddresses"
    "groups.search"
    "groups.getMembers"
    "groups.getById"
    #Методы для работы с поиском
    "search.getHints"
    #Методы для работы с пользовотелями 
    'users.get'
    'users.search'
    #Методы для работы с стенами сообществ
    'wall.getComments'
    'wall.get'
    #Методы для работы со статистикой ВК 
    'stats.get'
    'stats.getPostReach'



url = ApiUrl('https://api.vk.com','board.getTopics')

print(url._make_url())





