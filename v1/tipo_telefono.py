from flask import Blueprint, jsonify
from models import TipoTelefono

tipo_telefono_v1_bp = Blueprint('tipo_telefono_v1', __name__, url_prefix='/v1/tipo_telefono')

@tipo_telefono_v1_bp.route('/', methods=['GET'])
def obtener_tipos_telefono():
    tipos_telefono = TipoTelefono.query.all()
    resultado = [{
        'id_tipo_telefono': tipo_telefono.id_tipo_telefono,
        'id_cliente_telefono': tipo_telefono.id_cliente_telefono,
        'descripcion': tipo_telefono.descripcion
    } for tipo_telefono in tipos_telefono]
    return jsonify(resultado)

@tipo_telefono_v1_bp.route('/<int:id_tipo_telefono>', methods=['GET'])
def obtener_tipo_telefono(id_tipo_telefono):
    tipo_telefono = TipoTelefono.query.get(id_tipo_telefono)
    if not tipo_telefono:
        return jsonify({'mensaje': 'Tipo de Telefono no encontrado'}), 404

    resultado = {
        'id_tipo_telefono': tipo_telefono.id_tipo_telefono,
        'id_cliente_telefono': tipo_telefono.id_cliente_telefono,
        'descripcion': tipo_telefono.descripcion
    }
    return jsonify(resultado)
