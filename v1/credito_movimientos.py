from flask import Blueprint, jsonify
from models import CreditoMovimientos

credito_movimientos_v1_bp = Blueprint('credito_movimientos_v1', __name__, url_prefix='/v1/credito_movimientos')

@credito_movimientos_v1_bp.route('/', methods=['GET'])
def obtener_credito_movimientos():
    credito_movimientos = CreditoMovimientos.query.all()
    resultado = [{
        'id_movimientos': mov.id_movimientos,
        'id_credito': mov.id_credito,
        'id_tipo_movimiento': mov.id_tipo_movimiento,
        'monto': float(mov.monto),
        'fecha_movimiento': mov.fecha_movimiento.isoformat() if mov.fecha_movimiento else None,
    } for mov in credito_movimientos]
    return jsonify(resultado)

@credito_movimientos_v1_bp.route('/<string:id_movimientos>', methods=['GET'])
def obtener_credito_movimiento(id_movimientos):
    credito_movimiento = CreditoMovimientos.query.get(id_movimientos)
    if not credito_movimiento:
        return jsonify({'mensaje': 'Movimiento de crédito no encontrado'}), 404

    resultado = {
        'id_movimientos': credito_movimiento.id_movimientos,
        'id_credito': credito_movimiento.id_credito,
        'id_tipo_movimiento': credito_movimiento.id_tipo_movimiento,
        'monto': float(credito_movimiento.monto),
        'fecha_movimiento': credito_movimiento.fecha_movimiento.isoformat() if credito_movimiento.fecha_movimiento else None,
    }
    return jsonify(resultado)
