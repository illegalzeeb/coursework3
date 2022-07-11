import json

def get_posts_all() -> list[dict]:
    """
    Читает файл posts.json, возвращает посты как список словарей
    """
    with open('posts.json', 'r', encoding='utf8') as file:
        return json.load(file)


def get_comments_all() -> list[dict]:
    """
    Читает файл comments.json, возвращает комментарии как список словарей
    """
    with open('comments.json', 'r', encoding='utf8') as file:
        return json.load(file)


def search_for_posts(word : str) -> list[dict]:
    """
    Читает файл posts.json, если находит слово в content - добавляет его в список словарей, затем возвращает как список словарей
    """
    word_found = []
    for post in get_posts_all():
        if word.lower() in post['content'].lower():
            word_found.append(post)
    return word_found


def get_post_by_pk(pk):
    """
    Читает файл posts.json, если находит пост с заданным pk - возвращает пост как словарь
    """
    for post in get_posts_all():
        if pk in post['pk']:
            return post
    raise ValueError("Такого поста не существует")


def get_comments_by_post_id(post_id) -> list[dict]:
    """
    Читает файл comments.json, если находит слово в content - добавляет его в список словарей, затем возвращает как список словарей
    """
    comments_found = []
    post_count = 0
    for post in get_posts_all():
        if post_id in post['pk']:
            post_count += 1
    for comment in get_comments_all():
        if post_id in comment['post_id']:
            comments_found.append(comment)
    if post_count == 0:
        raise ValueError("Такого поста не существует")
    return word_found


def get_posts_by_user(user_name : str) -> list[dict]:
    """
    Читает файл posts.json, если находит пользователя в content - добавляет его в список словарей, затем возвращает как список словарей
    """
    users_posts = []
    users_count = 0
    for post in get_posts_all():
        if user_name.lower() in post['poster_name'].lower():
            users_count += 1
            users_posts.append(post)
    if users_count == 0:
        raise ValueError("Такого пользователя не существует")
    return users_posts


#def add_post(post : dict) -> dict:
#    """
#    Добавляет новый пост в файл posts.json
#    """
#    posts: list[dict] = load_posts()
#    posts.append(post)
#    with open('posts.json', 'w', encoding='utf8') as file:
#        json.dump(posts, file)
#    return post