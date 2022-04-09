import pytest
import utils


def grade_parameters():
    posts_all = utils.get_posts_all()
    posts_by_id = []
    for post in posts_all:
        posts_by_id.append((post['pk'], post))
    return posts_by_id


post_by_id = grade_parameters()


@pytest.mark.parametrize('number, post', post_by_id)
def test_get_comments_by_post_id(number, post):
    post_by_pk = utils.get_post_by_pk(number)
    assert post_by_pk == post
