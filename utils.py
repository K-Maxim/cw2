import json
from json import JSONDecodeError


def get_posts_all():
    """
    Ипортирует Json-файл
    :return: список постов
    """
    try:
        with open('data/data.json', 'r', encoding='UTF-8') as file:
            posts_all = json.load(file)
        return posts_all
    except FileNotFoundError:
        return 'Файл не найдет'
    except JSONDecodeError:
        return 'Файл не удается преобразовать'


def save_json(all_post):
    """
    запись новых данных в JSON-файл
    :param all_post: список всех постов
    """
    with open('posts.json', 'w', encoding='UTF-8') as file:
        json.dump(all_post, file, ensure_ascii=False)



def get_comments_all():
    """
    Ипортирует Json-файл
    :return: список комментариев
    """
    try:
        with open('data/comments.json', 'r', encoding='UTF-8') as file:
            comments = json.load(file)
            return comments
    except FileNotFoundError:
        return 'Файл не найдет'
    except JSONDecodeError:
        return 'Файл не удается преобразовать'


def get_posts_by_user(user_name):
    """
    :param user_name: имя ползователя (тип str)
    :return: пост в замисимости от имени (list)
    """
    posts_all = get_posts_all()
    posts_by_name = []
    for post in posts_all:
        if user_name.lower() == post["poster_name"].lower():
            posts_by_name.append(post)
    return posts_by_name


def get_comments_by_post_id(post_id):
    """
    :param post_id: id поста (тип int)
    :return: список комментариев в зависимости от id, имена комментаторов в зависимости от id
    """
    comments = get_comments_all()
    comments_on_the_post = []
    commenter_name = []
    for i in range(len(comments)):
        if post_id == comments[i]['post_id']:
            comments_on_the_post.append(comments[i]['comment'])
            commenter_name.append(comments[i]['commenter_name'])
    return comments_on_the_post, commenter_name


def get_comments_count(comments):
    """
    :param comments: список комментариев
    :return: количество комментариев к определенному посту (dict)
    """
    count = {}
    list_pk = []
    for comment in comments:
        list_pk.append(comment.get('post_id'))
    for pk in list_pk:
        num, name = get_comments_by_post_id(pk)
        quantity_comments = len(num)
        count[pk] = quantity_comments
    return count


def search_for_posts(search_post):
    """
    поиск постов по вхождению слова
    :param search_post: слово (тип str)
    :return: список постов
    """
    posts_all = get_posts_all()
    post_by_keyword = []

    for post in posts_all:
        if search_post.lower() in post["content"].lower():
            post_by_keyword.append(post)
    return post_by_keyword


def get_post_by_pk(pk):
    """
    :param pk: pk поста (int)
    :return: один пост
    """
    posts_all = get_posts_all()
    for post in posts_all:
        if pk == post["pk"]:
            return post


def get_posts_by_tag():
    """
    :return: возвращает все посты в зависимости от тега в виде списка, список тегов
    иднекс тега будет равен индексу поста в который входит этот тег
    """
    post_all = get_posts_all()
    post_by_tag = []
    tag = []
    for post in post_all:
        word_list = post['content'].split(' ')
        for word in word_list:
            if word[0] == '#':
                post_by_tag.append(post)
                tag.append(word)
    return post_by_tag, tag


def get_post_by_tagname(tag_name):
    """
    поиск по тэгу
    :param tag_name: тег (тип str)
    :return: вывод поста
    """
    post_all = get_posts_all()
    post_by_tag = []
    tag = []
    for post in post_all:
        word_list = post['content'].split(' ')
        for word in word_list:
            if f'#{tag_name}' == word:
                post_by_tag.append(post)
                tag.append(word)
    return post_by_tag, tag


def add_to_json(postid):
    """
    добаление поста в закладки
    :param postid: id поста (тип int)
    :return: список постов с учетом добавленных постов
    """
    with open('data/bookmarks.json', 'r+', encoding='UTF-8') as file:
        bookmarks = json.load(file)
        post = get_post_by_pk(postid)
        if post not in bookmarks:
            bookmarks.append(post)
            with open('data/bookmarks.json', 'w', encoding='UTF-8') as file:
                json.dump(bookmarks, file, ensure_ascii=False, indent=4)
        return bookmarks


def delete_from_json(postid):
    """
    удаление поста из закладок
    :param postid: id поста (тип int)
    :return: список постов с учетом удаленных постов
    """
    with open('data/bookmarks.json', 'r', encoding='UTF-8') as file:
        bookmarks = json.load(file)
        post = get_post_by_pk(postid)
        if post in bookmarks:
            bookmarks.remove(post)
            with open('data/bookmarks.json', 'w', encoding='UTF-8') as file:
                json.dump(bookmarks, file, indent=4)
        return bookmarks


def get_bookmarks():
    """
    :return: изначальный список в который дуду добавлять и удалять посты
    """
    with open('data/bookmarks.json', 'r', encoding='UTF-8') as file:
        all_add_post = json.load(file)
        return all_add_post






