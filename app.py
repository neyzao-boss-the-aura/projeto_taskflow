# importei a biblioteca principal
from flask import Flask, render_template, request

app = Flask(__name__)
#Dei um nome pra ela
#Rotas
#Banco de dados
# Um banco relacional (SQL) usa tabelas rígidas ligadas por chaves e exige um formato fixo [SQL],
# Sendo ideal para dados que pedem alta segurança e precisão (como sistemas de bancos).
# Já um banco não relacional (NoSQL) usa documentos flexíveis, como arquivos JSON [NoSQL],
# Permitindo mudar a estrutura dos dados facilmente e escalando com alta velocidade em grandes volumes.
base_fake = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pessoa', methods=['GET', 'POST'])
def pessoa():
    if request.method == 'POST':
        nome_pessoa = request.form.get('form_nome2')
        idade_pessoa = request.form.get('form_idade2')
        email_pessoa = request.form.get('form_email2')

        dados2 = {
            'nome_pessoa': nome_pessoa,
            'idade_pessoa': idade_pessoa,
            'email_pessoa': email_pessoa
        }
        print(f'dados_cadastrados: {dados2}')
        base_fake.append(dados2)
        print(f"base fake: {base_fake}")
        return render_template('pessoa.html',dados_atividade_pessoa=base_fake)
    return render_template('pessoa.html')

@app.route('/atividades/listar', methods=['GET', 'POST'])
def listar_atividades():
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

@app.route('/atividades/criar', methods=['GET', 'POST'])
def criar_atividade():
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
        print(f'dados_cadastrados: {dados4}')
        base_fake.append(dados4)
        print(f"base fake: {base_fake}")
        return render_template('criar_atividade.html',dados_atividade_criar=base_fake)
    return render_template('criar_atividade.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
#Este é o fim do projeto, não coloca nada em baixo disso