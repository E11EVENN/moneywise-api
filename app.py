from flask import Flask
from models import db 
from v1.pais import pais_v1_bp
from v1.ciudad import ciudad_v1_bp
from v1.credito import credito_v1_bp



def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234567890@localhost:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Inicialización de la base de datos
    db.init_app(app)

    # Registro del blueprint para la versión 1 de la API
    app.register_blueprint(pais_v1_bp, url_prefix='/v1/pais')

    app.register_blueprint(ciudad_v1_bp, url_prefix='/v1/ciudad')
    
    app.register_blueprint(credito_v1_bp, url_prefix='/v1/credito')

   
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
