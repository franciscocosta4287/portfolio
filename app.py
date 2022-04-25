from crypt import methods
from flask import Flask, redirect, render_template,request, flash
from flask_mail import Mail, Message
from config import email, senha 
# https://www.youtube.com/watch?v=Exsd5pN61RI&list=PLR8JXremim5DU70e3x_rYhClgMTzTyv4m&index=11&ab_channel=ThiCode

app = Flask(__name__)
app.secret_key = 'senha_francisco'

# configurando email
mail_setting = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha

}

app.config.update(mail_setting)
# Instancia Objeto
mail = Mail(app)

class Contato:
    def __init__(self, nome,email,mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


@app.route('/')
def home():
    # return "Obrigado Jesus  !!!"
    return render_template('index.html')


# Rota de envio
@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(  #formContato é um OBJ da classe contato
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            # subject = 'Contato do Portfólio'
            subject = f'{formContato.nome} te enviou uma memsagem no Portfólio',
            sender = app.config.get("MAIL_USERNAME"), #Quem esta enviando email
            recipients = ['fcsite@hotmail.com', 'francisco.costa@cmsw.com', 'bilanda@hotmail.com', app.config.get("MAIL_USERNAME")], #posso enviar email tanto para mim quantos para outras pessoas
            body = f''' 

            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

            {formContato.mensagem}
            
            '''
        )

        #enviando email
        mail.send(msg)
        #Mesagem para o usuario de retorno
        flash('Mensagem enviada com sucesso!')
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)