from flask import Flask, render_template, request, redirect, url_for

from flask_mail import Mail, Message

import secrets




app = Flask(__name__)

# Set the secret key
app.secret_key = secrets.token_hex(24)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'subdas374@gmail.com'
app.config['MAIL_PASSWORD'] = 'rsmaqutwqdfgslni'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Initialize the Flask-Mail extension
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Create and send email
        msg = Message(subject, sender=email, recipients=['subdas374@gmail.com'])
        msg.body = f'From: {name}\nEmail: {email}\nMessage:\n{message}'
        mail.send(msg)

       

        # Redirect back to the index page
        return redirect(url_for('index', success=True))
