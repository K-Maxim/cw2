import pytest

import utils


def grade_parameters():
    comments = utils.get_comments_all()
    comments_by_id = []
    for comment in comments:
        comments_by_id.append((comment['post_id'], comment['comment']))
    return comments_by_id


comment_list = grade_parameters()


@pytest.mark.parametrize('post_id, comment', comment_list)
def test_get_comments_by_post_id(post_id, comment):
    comments_on_the_post, name = utils.get_comments_by_post_id(post_id)
    assert comment in comments_on_the_post





