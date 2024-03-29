from flask import Blueprint, jsonify
from models import ClienteEmail

cliente_email_v1_bp = Blueprint('cliente_email_v1', __name__, url_prefix='/v1/cliente_email')

@cliente_email_v1_bp.route('/', methods=['GET'])
def obtener_clientes_email():
    clientes_email = ClienteEmail.query.all()
    resultado = [{
        'id_cliente_email': cliente_email.id_cliente_email,
        'id_tipo_email': cliente_email.id_tipo_email,
        'email': cliente_email.email
    } for cliente_email in clientes_email]
    return jsonify(resultado)

@cliente_email_v1_bp.route('/<string:id_cliente_email>', methods=['GET'])
def obtener_cliente_email(id_cliente_email):
    cliente_email = ClienteEmail.query.get(id_cliente_email)
    if not cliente_email:
        return jsonify({'mensaje': 'Email del Cliente no encontrado'}), 404

    resultado = {
        'id_cliente_email': cliente_email.id_cliente_email,
        'id_tipo_email': cliente_email.id_tipo_email,
        'email': cliente_email.email
    }
    return jsonify(resultado)
