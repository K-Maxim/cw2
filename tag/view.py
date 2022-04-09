from flask import render_template, Blueprint, request

import utils

tag_blueprint = Blueprint('tag_blueprint', __name__, template_folder='templates')


@tag_blueprint.route('/tag/<tagname>')
def tag_name(tagname):
    post_by_tag, tags = utils.get_post_by_tagname(tagname)
    return render_template('tag.html', post_by_tag=post_by_tag, tags=tags[0])







