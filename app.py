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

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

@app.route('/atividades/criar', methods=['GET', 'POST'])
def criar_atividade():
    dados = {}
    if request.method == 'POST':
        nome_atividade = request.form.get('form_nome')
        data_atividade = request.form.get('form_data')
        tipo_atividade = request.form.get('form_tipo')
        professor_atividade = request.form.getlist('form_professor')
        objetivo_atividade = request.form.get('form_objetivo')

        dados = {
            'nome_atividade': nome_atividade,
            'data_atividade': data_atividade,
            'tipo_atividade': tipo_atividade,
            'professor_atividade': professor_atividade,
            'objetivo_atividade': objetivo_atividade
        }
        print(f'dados_cadastrados: {dados}')
        base_fake.append(dados)
        print(f"base fake: {base_fake}")
        return render_template('criar_atividade.html',dados_atividade=base_fake)
    return render_template('criar_atividade.html')

@app.route('/atividades/listar')
def listar_atividades():
    return render_template('listar_atividades.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
#Este é o fim do projeto, não coloca nada em baixo disso