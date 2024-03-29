from flask import Blueprint, jsonify
from models import OrganizacionCliente

organizacion_cliente_v1_bp = Blueprint('organizacion_cliente_v1', __name__, url_prefix='/v1/organizacion_clientes')

@organizacion_cliente_v1_bp.route('/', methods=['GET'])
def obtener_organizacion_clientes():
    organizacion_clientes = OrganizacionCliente.query.all()
    resultado = [{
        'id_organizacion_cliente': org_cliente.id_organizacion_cliente,
        'id_cliente': org_cliente.id_cliente,
        'id_organizacion': org_cliente.id_organizacion
    } for org_cliente in organizacion_clientes]
    return jsonify(resultado)

@organizacion_cliente_v1_bp.route('/<string:id_organizacion_cliente>', methods=['GET'])
def obtener_organizacion_cliente(id_organizacion_cliente):
    org_cliente = OrganizacionCliente.query.get(id_organizacion_cliente)
    if not org_cliente:
        return jsonify({'mensaje': 'Organización Cliente no encontrado'}), 404

    resultado = {
        'id_organizacion_cliente': org_cliente.id_organizacion_cliente,
        'id_cliente': org_cliente.id_cliente,
        'id_organizacion': org_cliente.id_organizacion
    }
    return jsonify(resultado)
