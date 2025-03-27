from flask import Blueprint, request

answers_bp = Blueprint('answers', __name__)

@answers_bp.route('', methods=['GET', 'POST'])
def work_with_answers():
    if request.method == 'GET':
        return "Получен список всех ответов"
    if request.method == 'POST':
        return "Создание нового ответа на запрос"

@answers_bp.route('<int:id>', methods=['GET'])
def retrieve_answer(id):
    return f"Ответ на запрос по id {id}"

