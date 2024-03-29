from flask import Blueprint, jsonify
from models import ClienteDireccion

cliente_direccion_v1_bp = Blueprint('cliente_direccion_v1', __name__, url_prefix='/v1/cliente_direcciones')

@cliente_direccion_v1_bp.route('/', methods=['GET'])
def obtener_cliente_direcciones():
    cliente_direcciones = ClienteDireccion.query.all()
    resultado = [{
        'id_direcciones': direccion.id_direcciones,
        'id_cliente': direccion.id_cliente,
        'id_direccion': direccion.id_direccion,
        'tip_id_direccion': direccion.tip_id_direccion
    } for direccion in cliente_direcciones]
    return jsonify(resultado)

@cliente_direccion_v1_bp.route('/<string:id_direcciones>', methods=['GET'])
def obtener_cliente_direccion(id_direcciones):
    direccion = ClienteDireccion.query.get(id_direcciones)
    if not direccion:
        return jsonify({'mensaje': 'Direccion del Cliente no encontrada'}), 404

    resultado = {
        'id_direcciones': direccion.id_direcciones,
        'id_cliente': direccion.id_cliente,
        'id_direccion': direccion.id_direccion,
        'tip_id_direccion': direccion.tip_id_direccion
    }
    return jsonify(resultado)
