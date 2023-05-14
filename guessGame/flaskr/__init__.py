from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def game():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)

    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess == session['number']:
            message = 'Congratulations! You guessed the correct number.'
            session.pop('number')
        elif guess < session['number']:
            message = 'Try again! The number is higher.'
        else:
            message = 'Try again! The number is lower.'
        return render_template('game.html', message=message)

    return render_template('game.html')


if __name__ == '__main__':
    app.run()
