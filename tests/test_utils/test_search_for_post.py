import pytest
import utils


def grade_parameters():
    posts_all = utils.get_posts_all()
    posts_by_comments = []
    for post in posts_all:
        posts_by_comments.append((post['content'], post))
    return posts_by_comments


post_by_comments = grade_parameters()


@pytest.mark.parametrize('word, post', post_by_comments)
def test_get_comments_by_post_id(word, post):
    post_by_keyword = utils.search_for_posts(word)
    for one_post in post_by_keyword:
        assert one_post == post
