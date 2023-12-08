from flask import Flask, render_template, request, jsonify,redirect, url_for
from api_key import get_weather

app = Flask(__name__)

class Message:
    def __init__(self, text, sender):
        self.text = text
        self.sender = sender

chat = []

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form['user_input']
        chat.append(Message(user_input, "user"))
        weather_data = get_weather(user_input)
        if weather_data:
            response = f"Cuaca di {user_input.capitalize()} saat ini adalah {weather_data['description']}.\nSuhu saat ini adalah {weather_data['temperature']}°C dengan kelembapan {weather_data['humidity']}%."
            chat.append(Message(response, "bot"))
        else:
            response = f"Maaf, saya tidak dapat menemukan informasi cuaca untuk kota {user_input.capitalize()}."
            chat.append(Message(response, "bot"))

        return jsonify(response=response)

    return render_template('index.html', chat=chat)


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            # return redirect(url_for('index.html'))
            return render_template('index.html', chat=chat)
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)