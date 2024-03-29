from flask import Blueprint, jsonify
from models import CreditoCliente

credito_cliente_v1_bp = Blueprint('credito_cliente_v1', __name__, url_prefix='/v1/credito_cliente')

@credito_cliente_v1_bp.route('/', methods=['GET'])
def obtener_creditos_clientes():
    creditos_clientes = CreditoCliente.query.all()
    resultado = [{
        'id_credito_cliente': credito_cliente.id_credito_cliente,
        'id_cliente': credito_cliente.id_cliente,
        'id_credito': credito_cliente.id_credito
    } for credito_cliente in creditos_clientes]
    return jsonify(resultado)

@credito_cliente_v1_bp.route('/<int:id_credito_cliente>', methods=['GET'])
def obtener_credito_cliente(id_credito_cliente):
    credito_cliente = CreditoCliente.query.get(id_credito_cliente)
    if not credito_cliente:
        return jsonify({'mensaje': 'Crédito Cliente no encontrado'}), 404

    resultado = {
        'id_credito_cliente': credito_cliente.id_credito_cliente,
        'id_cliente': credito_cliente.id_cliente,
        'id_credito': credito_cliente.id_credito
    }
    return jsonify(resultado)
