from flask import render_template, Blueprint, request

import utils

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search/')
def search():
    search_post = request.args['s']
    post_by_keyword = utils.search_for_posts(search_post)
    quantity_contents = len(post_by_keyword[:10])
    comments = utils.get_comments_all()
    post_by_tag, tags = utils.get_posts_by_tag()
    comments_count = utils.get_comments_count(comments)
    return render_template('search.html', search_post=search_post,
                           quantity_contents=quantity_contents,
                           post_by_keyword=post_by_keyword[:10],
                           comments_count=comments_count, tags=tags)

