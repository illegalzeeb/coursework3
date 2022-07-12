from json import JSONDecodeError

from flask import Blueprint, render_template, request
from utils import get_posts_all, search_for_posts, get_posts_by_user
import textwrap

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def main_page():
    posts = get_posts_all()
#    del posts[10:]                 #Это отказалось ненужно по условиям
    for post in posts:
        post['content'] = textwrap.shorten(post['content'], width=30, placeholder='...')
    return render_template("index.html", posts=posts)


@main_blueprint.route("/search/")
def search_page():
    search_query = request.args.get('s', '')
#    logging.info("Поиск")
    try:
        posts = search_for_posts(search_query)
    except FileNotFoundError:
#        logging.info('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Ошибка в файле JSON"
    posts_found_count = len(posts)
    del posts[10:]                 #А вот тут это нужно
    for post in posts:
        post['content'] = textwrap.shorten(post['content'], width=30, placeholder='...')
    return render_template("search.html", query=search_query, posts=posts, count=posts_found_count)


@main_blueprint.route("/user-feed/")
def user_feed():
    poster_name = request.args.get('u')
#    return user_name               #Проверка
    try:
        posts = get_posts_by_user(poster_name)
    except FileNotFoundError:
        logging.info('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Ошибка в файле JSON"
    for post in posts:
        post['content'] = textwrap.shorten(post['content'], width=30, placeholder='...')
    return render_template("user-feed.html", posts=posts)
