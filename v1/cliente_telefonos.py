from flask import Blueprint, jsonify
from models import ClienteTelefono

cliente_telefono_v1_bp = Blueprint('cliente_telefono_v1', __name__, url_prefix='/v1/cliente_telefonos')

@cliente_telefono_v1_bp.route('/', methods=['GET'])
def obtener_cliente_telefonos():
    cliente_telefonos = ClienteTelefono.query.all()
    resultado = [{
        'id_cliente_telefono': cliente_telefono.id_cliente_telefono,
        'telefono': cliente_telefono.telefono
    } for cliente_telefono in cliente_telefonos]
    return jsonify(resultado)

@cliente_telefono_v1_bp.route('/<string:id_cliente_telefono>', methods=['GET'])
def obtener_cliente_telefono(id_cliente_telefono):
    cliente_telefono = ClienteTelefono.query.get(id_cliente_telefono)
    if not cliente_telefono:
        return jsonify({'mensaje': 'Telefono del Cliente no encontrado'}), 404

    resultado = {
        'id_cliente_telefono': cliente_telefono.id_cliente_telefono,
        'telefono': cliente_telefono.telefono
    }
    return jsonify(resultado)
