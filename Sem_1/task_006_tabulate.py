from flask import Flask, render_template
from tabulate import tabulate
app = Flask(__name__)


@app.route('/students/')
def stud_list():
    people = [
        {'Имя': 'Иван', 'Фамилия': 'Иванов', 'Возраст': 20, 'Средний балл': 4.5},
        {'Имя': 'Петр', 'Фамилия': 'Петров', 'Возраст': 21, 'Средний балл': 4.2},
        {'Имя': 'Сергей', 'Фамилия': 'Сергеев',
            'Возраст': 19, 'Средний балл': 4.8},
        {'Имя': 'Анна', 'Фамилия': 'Иванова', 'Возраст': 20, 'Средний балл': 4.7}
    ]

    html_table = tabulate(people, headers='keys', tablefmt='html')

    return render_template('table.html', table=html_table)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
