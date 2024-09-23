from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuração de e-mail (usando Flask-Mail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página de contato
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Enviar e-mail usando Flask-Mail
        msg = Message('Contato do Site', sender=email, recipients=['seuemail@ong.com'])
        msg.body = f"Nome: {name}\nE-mail: {email}\nMensagem:\n{message}"
        mail.send(msg)
        
        flash('Mensagem enviada com sucesso!', 'success')
        return redirect('/contact')
    
    return render_template('contact.html')

# Rota para a página de eventos
@app.route('/events')
def events():
    # Aqui você pode carregar os eventos de um banco de dados ou arquivo
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)
