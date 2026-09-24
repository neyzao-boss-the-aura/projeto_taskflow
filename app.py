# importei a biblioteca principal
from calendar import error

import sqlalchemy
from flask import Flask, render_template, request, flash
from datetime import datetime
from models import Recurso, Pessoa, db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bitata'
activity_list = []
suggestion_list = []
#Dei um nome pra ela
#Rotas
#Banco de dados
# Um banco relacional (SQL) usa tabelas rígidas ligadas por chaves e exige um formato fixo [SQL],
# Sendo ideal para dados que pedem alta segurança e precisão (como sistemas de bancos).
# Já um banco não relacional (NoSQL) usa documentos flexíveis, como arquivos JSON [NoSQL],
# Permitindo mudar a estrutura dos dados facilmente e escalando com alta velocidade em grandes volumes.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pessoa/cadasto', methods=['GET', 'POST'])
def cadastro_pessoa():
    if request.method == 'GET':

        nome_form = request.form.get('form_nome2')
        email_from = request.form.get('form_email2')
        senha_from = request.form.get('form_senha2')

        try:
            nova_pessoa = Pessoa(nome=nome_form, email=email_from, senha=senha_from)
            db_session.add(nova_pessoa)
            db_session.commit()
            print(f'nova_pessoa')
            return render_template('cadastro_pessoa.html')
        except sqlalchemyError as e:
            db_session.rollback()
            print(f'Erro ao cadastrar nova_pessoa: {e}')
            flash('Erro ao cadastrar nova_pessoa', category='Error')
            return render_template('cadastro_pessoa.html')

        if not nome_form:
            flash('Preencha este campo', category=error)
            return render_template('cadastro_pessoa.html')
        if not email_form:
            flash('Preencha este campo', category=error)
            return render_template('cadastro_pessoa.html')
        if not senha_form:
            flash('Preencha este campo', category=error)
            return render_template('cadastro_pessoa.html')

        return render_template('listar_pessoa.html')
    return render_template('cadastro_pessoa.html')

@app.route('/atividade', methods=['GET', 'POST'])
def atividade():
    if request.method == 'POST':
        nome_atividade = request.form.get('form_nome4')
        data_atividade = request.form.get('form_data4')
        tipo_atividade = request.form.get('form_tipo4')
        professor_atividade = request.form.getlist('form_professor4')
        objetivo_atividade = request.form.get('form_objetivo4')

        dados4 = {
            'nome_atividade': nome_atividade,
            'data_atividade': data_atividade,
            'tipo_atividade': tipo_atividade,
            'professor_atividade': professor_atividade,
            'objetivo_atividade': objetivo_atividade
        }

        activity_list.append(dados4)

    return render_template('listar_atividades.html',dados_atividade_listar=activity_list)

@app.route('/atividades/listar', methods=['GET', 'POST'])
def listar_atividades():
    if request.method == 'POST':
        activities = activity_list

        return render_template('listar_atividades.html',activities=activities)

@app.route('/pessoa', methods=['GET', 'POST'])
def pessoa():
    if request.method == 'POST':
        nome_da_atividade = request.form.get('form_nome3')

        dados3 = {
            'nome_da_atividade': nome_da_atividade,
        }
        print(f'dados_cadastrados: {dados3}')
        base_fake.append(dados3)
        print(f"base fake: {base_fake}")
        return render_template('listar_atividades.html',dados_atividade_listar=base_fake)
    return render_template('listar_atividades.html')

@app.route('/recurso', methods=['GET', 'POST'])
def recurso():
    if request.method == 'GET':
        return render_template('recurso.html')

    nome = request.form.get('form_nome')
    uso_pratico = request.form.get('form_uso')
    print(f'nome: {nome}, uso_pratico: {uso_pratico}')
    Recurso(nome_recurso=nome, uso_pratico=uso_pratico)
    return render_template('recurso.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
#Este é o fim do projeto, não coloca nada em baixo disso