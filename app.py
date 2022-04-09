from flask import Flask, jsonify
import utils
from main_page.view import main_page_blueprint
from post.view import post_blueprint
from search.view import search_blueprint
from user_feed.view import user_feed__blueprint
from tag.view import tag_blueprint
from bookmarks.view import bookmarks_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_page_blueprint, url_prefix='/')
app.register_blueprint(post_blueprint, url_prefix='/')
app.register_blueprint(search_blueprint, url_prefix='/')
app.register_blueprint(user_feed__blueprint, url_prefix='/')
app.register_blueprint(tag_blueprint, url_prefix='/')
app.register_blueprint(bookmarks_blueprint, url_prefix='/')


@app.route('/api/posts/')
def get_json():
    data = utils.get_posts_all()
    return jsonify(data)


@app.route('/api/posts/<int:post_id>')
def get_one_json(post_id):
    data = utils.get_post_by_pk(post_id)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
