# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.

from flask import Flask
app = Flask(__name__)


@app.route('/summa/<int:num_1>_<int:num_2>/')
def sum(num_1, num_2):
    return f'Сумма чисел:{str(num_1 + num_2)}'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
