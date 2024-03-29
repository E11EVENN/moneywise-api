from flask import Blueprint, jsonify
from models import TipoCliente

tipo_cliente_v1_bp = Blueprint('tipo_cliente_v1', __name__, url_prefix='/v1/tipo_cliente')

@tipo_cliente_v1_bp.route('/', methods=['GET'])
def obtener_tipos_cliente():
    tipos_cliente = TipoCliente.query.all()
    resultado = [{
        'id_tipo_cliente': tipo_cliente.id_tipo_cliente,
        'id_cliente': tipo_cliente.id_cliente,
        'descripcion': tipo_cliente.descripcion
    } for tipo_cliente in tipos_cliente]
    return jsonify(resultado)

@tipo_cliente_v1_bp.route('/<string:id_tipo_cliente>', methods=['GET'])
def obtener_tipo_cliente(id_tipo_cliente):
    tipo_cliente = TipoCliente.query.get(id_tipo_cliente)
    if not tipo_cliente:
        return jsonify({'mensaje': 'Tipo de Cliente no encontrado'}), 404

    resultado = {
        'id_tipo_cliente': tipo_cliente.id_tipo_cliente,
        'id_cliente': tipo_cliente.id_cliente,
        'descripcion': tipo_cliente.descripcion
    }
    return jsonify(resultado)
