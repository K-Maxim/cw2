from flask import Blueprint, render_template, request
# from utils import load_json_file, save_json
import utils
import logging

add_post_blueprint = Blueprint('add_post_blueprint', __name__, template_folder='templates')


@add_post_blueprint.route('/post/')
def add_post():
    """
    страница для добавления своего поста
    :return: страницу в браузере
    """
    return render_template('add_post.html')


@add_post_blueprint.route('/loader/', methods=['POST'])
def post_uploaded():
    text = request.values.get('content')  # помещение текста к посту в переменную
    picture = request.files.get('picture')  # помещение картинки к посту в переменную
    filename = picture.filename  # помещение названия файла в переменную
    all_posts = utils.get_posts_all()  # импорт списка всех постов
    picture.save(f"./static/img/{filename}")  # сохранение картинки в определенную папку
    if filename.split('.')[-1] not in ['jpg', 'jpeg', 'png']:  # проверка расширения формата картинки
        logging.info('Файл не является изображением')  # выведет в консоли, если файл не картинка
    try:
        all_posts.append({
            'pic': f'/static/img/{filename}',
            'content': text
        })
        utils.save_json(all_posts)
        # если добавление прошло успешно
    except FileNotFoundError:
        logging.error('Ошибка при загрузке')
        return f'<h1>Файл не найден</h1>'
        # если файл в который надо добавить не был найден
    else:
        return render_template('post_uploaded.html', text=text, filename=filename)
        # если try будет успешным, то выведет страницу с готовым новым постом
