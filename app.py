from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Definindo variáveis globais
numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 10

@app.route('/', methods=['GET', 'POST'])
def index():
    global tentativas
    global numero_secreto
    mensagem = ''
    if request.method == 'POST':
        tentativa = int(request.form['tentativa'])
        tentativas += 1

        if tentativa < numero_secreto:
            mensagem = 'O número é maior do que isso.'
        elif tentativa > numero_secreto:
            mensagem = 'O número é menor do que isso.'
        else:
            mensagem = f'Parabéns! Você adivinhou o número em {tentativas} tentativas.'
            tentativas = 0
            numero_secreto = random.randint(1, 100)

        if tentativas >= max_tentativas:
            mensagem = f'Suas tentativas acabaram. O número era {numero_secreto}. Boa sorte na próxima vez!'
            tentativas = 0
            numero_secreto = random.randint(1, 100)

    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
