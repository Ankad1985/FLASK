# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.

from flask import Flask
app = Flask(__name__)


@app.route('/lenght string/<str>/')
def len_str(str):
    return f'Длина строки:{len(str)}'


if __name__ == '__main__':
    app.run(debug=True, port=4000)
