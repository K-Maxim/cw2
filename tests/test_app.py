import pytest

from app import app

json_file = [
    {
        "poster_name": "leo",
        "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
        "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
        "views_count": 376,
        "likes_count": 154,
        "pk": 1
    }
]


class TestJsonAPI:

    def test_get_all_json(self):
        response = app.test_client().get('/api/posts/')
        assert type(response.json) == list, 'Неверный тип данных при получении всех постов'

    def test_get_keywords_all_json(self):
        resource = app.test_client().get('/api/posts/')
        keys_resource = resource.json[0].keys()
        key_json_file = json_file[0].keys()
        assert keys_resource == key_json_file, 'В запросе неверный список ключей для всех постов'

    def test_get_one_json(self):
        resource = app.test_client().get('/api/posts/1')
        assert type(resource.json) == dict, 'Неверный тип данных при получении одного поста'

    def test_get_keywords_one_json(self):
        resource = app.test_client().get('/api/posts/1')
        keys_resource = resource.json.keys()
        keys_from_json_file = json_file[0].keys()
        assert keys_resource == keys_from_json_file, 'В запросе неверный список ключей для одного поста'
