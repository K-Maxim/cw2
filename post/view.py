from flask import render_template, Blueprint, request

import utils

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/post/<int:postid>')
def one_post(postid):
    id = postid
    post_by_pk = utils.get_post_by_pk(postid)
    comments_on_the_post, commenter_name = utils.get_comments_by_post_id(postid)
    quantity_comments = len(comments_on_the_post)
    return render_template('post.html', post_by_pk=post_by_pk, id=id,
                           comments_on_the_post=comments_on_the_post,
                           quantity_comments=quantity_comments,
                           commenter_name=commenter_name)


