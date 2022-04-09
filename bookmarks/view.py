from flask import render_template, Blueprint, redirect

import utils

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@bookmarks_blueprint.route('/bookmark/')
def all_bookmarks():
    all_posts = utils.get_bookmarks()
    return render_template('bookmarks.html', all_posts=all_posts)


@bookmarks_blueprint.route('/bookmark/add/<int:postid>')
def add_to_bookmarks(postid):
    add_bookmark = utils.add_to_json(postid)
    return redirect('/', code=302)


@bookmarks_blueprint.route('bookmark/remove/<int:postid>')
def delete_from_bookmarks(postid):
    delete_bookmarks = utils.delete_from_json(postid)
    return redirect('/', code=302)

