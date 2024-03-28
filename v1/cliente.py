from flask import Blueprint, jsonify
from models import Cliente

cliente_v1_bp = Blueprint('cliente_v1', __name__, url_prefix='/v1/cliente')

@cliente_v1_bp.route('/', methods=['GET'])
def obtener_clientes():
    clientes = Cliente.query.all()
    resultado = [{
        'id_cliente': cliente.id_cliente,
        'id_ciudad': cliente.id_ciudad,
        'id_cliente_email': cliente.id_cliente_email,
        'id_direccion': cliente.id_direccion,
        'id_tipo_telefono': int(cliente.id_tipo_telefono),
        'nombre': cliente.nombre,
        'apellido': cliente.apellido,
        'documento': cliente.documento,
        'fecha_registro': cliente.fecha_registro.isoformat() if cliente.fecha_registro else None,
    } for cliente in clientes]
    return jsonify(resultado)

@cliente_v1_bp.route('/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    if not cliente:
        return jsonify({'mensaje': 'Cliente no encontrado'}), 404

    resultado = {
        'id_cliente': cliente.id_cliente,
        'id_ciudad': cliente.id_ciudad,
        'id_cliente_email': cliente.id_cliente_email,
        'id_direccion': cliente.id_direccion,
        'id_tipo_telefono': int(cliente.id_tipo_telefono),
        'nombre': cliente.nombre,
        'apellido': cliente.apellido,
        'documento': cliente.documento,
        'fecha_registro': cliente.fecha_registro.isoformat() if cliente.fecha_registro else None,
    }
    return jsonify(resultado)

# Add more routes for creating, updating, and deleting clients as needed.
