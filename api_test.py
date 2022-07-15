from main import app
import pytest


def test_all_posts():
    response = app.test_client().get('/api/posts/')
    assert type(response.json.get) == list, "Неверный тип данных"
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    for field in fields:
        assert hasattr(response, "field"), f"Нет поля {field}"

def test_post_by_id():
    response = app.test_client().get('/api/posts/post_id')
    assert type(response.json.get) == list, "Неверный тип данных"
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    for field in fields:
        assert hasattr(response, "field"), f"Нет поля {field}"