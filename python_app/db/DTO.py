from typing import Optional
from dataclasses import dataclass

@dataclass
class Id():
    id: int
    domain:Optional[str]


@dataclass
class Location:
    country: str
    city: str


@dataclass
class Person():
    id: Id
    sex:str or bool
    first_name: str
    last_name: str
    deactivated: bool
    is_closed: bool




@dataclass
class Post():
    id: Id
    views: int
    likes_count:int
    owner_id: Id
    from_id: Id 
    data: int
    text: str


@dataclass
class Comment():
    id: Id
    from_id: Id
    views: int
    likes_count:int
    date: str
    text: str

@dataclass
class Сommuniti():
    id:Id
    name: str
    screen_name: str
    is_closed: bool
    deactivated: bool
    type: str
    location:Location



