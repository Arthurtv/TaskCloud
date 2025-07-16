from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskcloud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200))
    status = db.Column(db.String(20), default="pendente")

@app.route('/')
def hello():
    return 'TaskCloud API'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    if User.query.filter_by(email=email).first():
        return jsonify({'erro': 'Usuário já existe'}), 400

    senha_hash = generate_password_hash(senha)
    novo_usuario = User(email=email, password_hash=senha_hash)
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({'mensagem': 'Usuário registrado com sucesso'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, senha):
        return jsonify({'mensagem': 'Login bem-sucedido', 'user_id': user.id})
    else:
        return jsonify({'erro': 'Credenciais inválidas'}), 401

@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    tarefas = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': t.id, 'title': t.title, 'status': t.status} for t in tarefas])

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    nova_tarefa = Task(user_id=user_id, title=title)
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa criada com sucesso'})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    status = data.get('status')
    tarefa = Task.query.get(task_id)
    if tarefa:
        tarefa.status = status
        db.session.commit()
        return jsonify({'mensagem': 'Tarefa atualizada'})
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tarefa = Task.query.get(task_id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({'mensagem': 'Tarefa deletada'})
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
  
