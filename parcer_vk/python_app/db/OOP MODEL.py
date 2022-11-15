import typing
from dataclasses import dataclass

@dataclass
class Id():
    id: int


@dataclass
class Location:
    country: str
    city: str


@dataclass
class Person():
    id: Id
    first_name: str
    last_name: str
    deactivated: bool
    is_closed: bool


@dataclass
class Post():
    id: Id
    owner_id: Id
    from_id: Id 
    data: int
    text: str


@dataclass
class Comment():
    id: Id
    from_id: Id
    date: int
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



