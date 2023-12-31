# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше веб приложение:
# ○ страницу "about"
# ○ страницу "contact".

from flask import Flask
app = Flask(__name__)


@app.route('/start/')
def start():
    return f'Hello World!'


@app.route('/about/')
def about():
    return f'page about'


@app.route('/contact/')
def contact():
    return f'page contact'


if __name__ == '__main__':
    app.run(debug=True, port=2000)
