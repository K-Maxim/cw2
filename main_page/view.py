from flask import render_template, Blueprint

import utils

main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='templates')


@main_page_blueprint.route('/')
def main_page():
    posts_all = utils.get_posts_all()
    bookmarks = utils.get_bookmarks()
    comments = utils.get_comments_all()
    post_by_tag, tags = utils.get_posts_by_tag()
    comments_count = utils.get_comments_count(comments)
    return render_template('index.html', posts_all=posts_all, bookmarks=bookmarks,
                           comments_count=comments_count, tags=tags)

