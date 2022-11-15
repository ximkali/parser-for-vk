from abc import ABCMeta, abstractclassmethod
from requests_oauthlib import OAuth2Session
from dataclasses import dataclass
import requests


@dataclass
class AuthorizeInfo():

    client_id:str
    secret_id:str
    redirect_uri:str
    display:str
    scope:str or int 
    authorize_url:str

class AuthorizeInterface(ABCMeta):
    @abstractclassmethod
    def authorize():
        pass


