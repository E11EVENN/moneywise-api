from flask import Blueprint, jsonify
from models import TipoMovimiento

tipo_movimiento_v1_bp = Blueprint('tipo_movimiento_v1', __name__, url_prefix='/v1/tipo_movimiento')

@tipo_movimiento_v1_bp.route('/', methods=['GET'])
def obtener_tipos_movimiento():
    tipos_movimiento = TipoMovimiento.query.all()
    resultado = [{
        'id_tipo_movimiento': tipo_movimiento.id_tipo_movimiento,
        'descripcion': tipo_movimiento.descripcion
    } for tipo_movimiento in tipos_movimiento]
    return jsonify(resultado)

@tipo_movimiento_v1_bp.route('/<string:id_tipo_movimiento>', methods=['GET'])
def obtener_tipo_movimiento(id_tipo_movimiento):
    tipo_movimiento = TipoMovimiento.query.get(id_tipo_movimiento)
    if not tipo_movimiento:
        return jsonify({'mensaje': 'Tipo de Movimiento no encontrado'}), 404

    resultado = {
        'id_tipo_movimiento': tipo_movimiento.id_tipo_movimiento,
        'descripcion': tipo_movimiento.descripcion
    }
    return jsonify(resultado)
