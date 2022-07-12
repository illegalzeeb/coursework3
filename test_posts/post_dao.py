import json
from json import JSONDecodeError
from pprint import pprint
from post import Post
from exceptions.exeptions import DataSourceError


class PostDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """
        читает файл posts и возвращает его как posts_data
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Ошибка чтения файла {self.path}')
        return posts_data

    def _load_posts(self):
        """
        формирует список из элементов Post из posts_data
        """
        posts_data = self._load_data()
        list_of_posts = [Post(**post_data) for post_data in posts_data]
        return list_of_posts

    def get_all(self):
        """
        получает посты, возвращает список элементов класса Post
        """
        posts = self._load_posts()
        return posts

    def get_by_pk(self):
        """
        получает пост по pk
        """
        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_content(self, substring):
        """
        ищет посты по кусочку текста
        """
        substring = str(substring).lower()
        posts = self._load_posts()
        matching_posts = [post for post in posts if substring in post.content.lower()]
        return matching_posts

    def search_user(self, user_name):
        """
        Поиск по имени пользователя
        """
        user_name = str(user_name).lower()
        posts = self._load_posts()
        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]
        return matching_posts

pd = PostDAO("../posts.json")
pprint(pd.get_all())