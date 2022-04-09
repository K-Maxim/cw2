from flask import render_template, Blueprint, request

import utils

user_feed__blueprint = Blueprint('user_feed_blueprint', __name__, template_folder='templates')


@user_feed__blueprint.route('/users/<username>')
def user_name(username):
    post_by_username = utils.get_posts_by_user(username)
    return render_template('user-feed.html', post_by_username=post_by_username)

