"""
import pytest

from post_dao import PostDAO
from test_posts.post import Post

def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    for field in fields:
        assert hasattr(post, "field"), f"Нет поля {field}"


class TestPostsDAO:

    @pytest.fixture
    def post_dao(self):
        post_dao_inst = PostDAO("../posts.json")
        return post_dao_inst

    def test_get_all(self, post_dao):

        posts = post_dao.get_all()
        assert type(posts) == list, "Incorrect type for result"

#        post = post_dao.get_all()[0]
#        assert type(post) == post.Post, "Incorrect type for item"

    def test_get_all_fields(self, post_dao):
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_all()
        correct_pks = {1,2,3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks, "Не совпадают полученные id"
"""