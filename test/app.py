from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'dmelkk@gmail.com'
app.config['MAIL_PASSWORD'] = "Don't 4got"
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

@app.route('/')
def index():
    msg = Message("Hello",
            sender = "demlkk@gmail.com",
            recipients=["dmelkk@gmail.com"])
    msg.body = "Hello"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True)
