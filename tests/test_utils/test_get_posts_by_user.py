import pytest

import utils


def grade_parameters():
    post_all = utils.get_posts_all()
    parameters_all_posts = []
    for post in post_all:
        parameters_all_posts.append((post['poster_name'], post))
    return parameters_all_posts


parameters = grade_parameters()


@pytest.mark.parametrize('grade_name, data_person', parameters)
def test_get_posts_by_user(grade_name, data_person):
    assert utils.get_posts_by_user(grade_name)[0] == data_person or \
           utils.get_posts_by_user(grade_name)[1] == data_person
