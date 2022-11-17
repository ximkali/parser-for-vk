from abc import ABCMeta
from dataclasses import dataclass
import requests


@dataclass
class AuthorizeInfo():

    client_id:str
    # secret_id:Optional[str}
    redirect_uri:str
    display:str
    scope:str or int 
    # authorize_url:str
    response_type:str
    v:str


class AuthorizeInterface(ABCMeta):
    @classmethod
    def authorize():
        pass

    # @classmethod
    # def refresh_token():
    #     pass

vk_aut_info = AuthorizeInfo(client_id='51434932',
                            redirect_uri='https://oauth.vk.com/blank.html',
                            display='page',
                            scope='wall,offline,groups,friends',
                            response_type='token',
                            v= '5.131')


class AuthorizeVK(AuthorizeInterface):
    
    def authorize(info:AuthorizeInfo = vk_aut_info):
        auth_req = requests.get('https://oauth.vk.com/authorize?',params={"client_id":'51434932',
                            "redirect_uri":'https://oauth.vk.com/blank.html',
                            "display":'page',
                            "scope":'wall,offline,groups,friends',
                            "response_type":'token',
                            "v":'5.131'})
        r = auth_req.url
        print(r)


aut_sesion = AuthorizeVK.authorize()

