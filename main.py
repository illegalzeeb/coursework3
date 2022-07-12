import logging

from flask import Flask, request, render_template, send_from_directory

from views import main_blueprint

POST_PATH = "posts.json"
COMMENTS_PATH = "comments.json"
BOOKMARKS_PATH = "bookmarks.json"

app = Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(main_blueprint)
logging.basicConfig(filename="basic.log", level=logging.INFO)

app.run()