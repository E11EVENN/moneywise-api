from flask import Blueprint, jsonify
from models import CreditoPago

credito_pago_v1_bp = Blueprint('credito_pago_v1', __name__, url_prefix='/v1/credito_pagos')

@credito_pago_v1_bp.route('/', methods=['GET'])
def obtener_creditos_pagos():
    creditos_pagos = CreditoPago.query.all()
    resultado = [{
        'id_credito_pago': credito_pago.id_credito_pago,
        'id_credito': credito_pago.id_credito,
        'monto': float(credito_pago.monto),
        'fecha_pago': credito_pago.fecha_pago.isoformat() if credito_pago.fecha_pago else None
    } for credito_pago in creditos_pagos]
    return jsonify(resultado)

@credito_pago_v1_bp.route('/<int:id_credito_pago>', methods=['GET'])
def obtener_credito_pago(id_credito_pago):
    credito_pago = CreditoPago.query.get(id_credito_pago)
    if not credito_pago:
        return jsonify({'mensaje': 'Credito Pago no encontrado'}), 404

    resultado = {
        'id_credito_pago': credito_pago.id_credito_pago,
        'id_credito': credito_pago.id_credito,
        'monto': float(credito_pago.monto),
        'fecha_pago': credito_pago.fecha_pago.isoformat() if credito_pago.fecha_pago else None
    }
    return jsonify(resultado)
