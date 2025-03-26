from flask import Flask, request
from pymysql.constants.ER import GET_ERRMSG
from sqlalchemy.orm.loading import PostLoad

app = Flask(__name__)  # http://127.0.0.1:5000

@app.route('/home')  # http://127.0.0.1:5000/home
def home():
    return "You are on the HOME page."


@app.route('/me') # статические параметры
def user_page():
    return "User Profile Page"


@app.route('/user/<string:username>') # динамичные параметры
def get_user_info(username):
    return f"Hello, {username}"

@app.route('/user-by-id/<int:user_id>')
def get_user_by_id(user_id):
    return f"User by ID {user_id}"


@app.route('/file/<path:file_path>/<int:file_id>')
def get_file(file_path, file_id):
    # file_path = str(r'path/to/file')
    remote_url = "https://example.com"
    return f"File by remote path: {remote_url}/{file_path}{file_id}"

@app.route('/registrate', methods=['POST'])
def post_request():
    # username= request.form['username']
    # password = request.form['password']
    # email = request.form['email']
    data = request.json
    username = data['username']
    password = data['password']
    email = data['email']
    return f"Username: {username}\nPassword: {"*" * len(password)}\nEmail: {email}"

#
# int  1
# float  2.0
# string ort_text
# path  path/to/file
# uuid (sdsg8-d7f6g-5sg78-sd6f-gsd56) из 32 символов

if __name__ == "__main__":
    app.run(debug=True)


# GET (получить объект \ список объектов)
# POST (создать объект)
# PUT \ PATCH (обновить конкретный объект или целиком, или кнкретное поле(поля))
# DELETE (удалить конкретный объект)
# HEAD (почти как и метод GET, но не возвращает тело ответа, возвращает HTTP заголовки)
# OPTIONS


