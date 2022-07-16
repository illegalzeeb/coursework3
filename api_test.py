import json
from pprint import pprint

from main import app
import pytest


def test_all_posts():
    response = app.test_client().get('/api/posts/')
    data = response.json
    assert type(data) == list, "Неверный тип данных"
    fields = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    for post in data:
        for field in fields:
            assert field in post, f"Нет поля {field}"

def test_post_by_id():
    response = app.test_client().get('/api/posts/post_id?p=3')
    data = response.json
    assert type(data) == dict, "Неверный тип данных"
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    for field in fields:
        assert field in data, f"Нет поля {field}"