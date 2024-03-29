from flask import Blueprint, jsonify
from models import CreditoLotePago

credito_lote_pago_v1_bp = Blueprint('credito_lote_pago_v1', __name__, url_prefix='/v1/credito_lote_pagos')

@credito_lote_pago_v1_bp.route('/', methods=['GET'])
def obtener_creditos_lote_pagos():
    lote_pagos = CreditoLotePago.query.all()
    resultado = [{
        'id_credito_lote_pago': lote_pago.id_credito_lote_pago,
        'id_credito_pago': lote_pago.id_credito_pago
    } for lote_pago in lote_pagos]
    return jsonify(resultado)

@credito_lote_pago_v1_bp.route('/<int:id_credito_lote_pago>', methods=['GET'])
def obtener_credito_lote_pago(id_credito_lote_pago):
    lote_pago = CreditoLotePago.query.get(id_credito_lote_pago)
    if not lote_pago:
        return jsonify({'mensaje': 'Crédito Lote Pago no encontrado'}), 404

    resultado = {
        'id_credito_lote_pago': lote_pago.id_credito_lote_pago,
        'id_credito_pago': lote_pago.id_credito_pago
    }
    return jsonify(resultado)
