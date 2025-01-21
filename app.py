from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from sql_alchemy import banco

# Configuração do app Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'  # Define o caminho para o banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False         # Desativa notificações de mudanças no SQLAlchemy

# Inicialização do SQLAlchemy
banco.init_app(app)

# Configuração da API RESTful
api = Api(app)
api.add_resource(Hoteis, '/hoteis')                          # Endpoint para lista de hotéis
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')         # Endpoint para detalhes de um hotel específico

# Criação do banco de dados antes de iniciar o servidor
with app.app_context():
    banco.create_all()

# Início da aplicação
if __name__ == '__main__':
    app.run(debug=True)
