from flask import Blueprint, jsonify
from models import TipoDocumento

tipo_documento_v1_bp = Blueprint('tipo_documento_v1', __name__, url_prefix='/v1/tipo_documento')

@tipo_documento_v1_bp.route('/', methods=['GET'])
def obtener_tipos_documento():
    tipos_documento = TipoDocumento.query.all()
    resultado = [{
        'id_tipo_documento': tipo_documento.id_tipo_documento,
        'descripcion': tipo_documento.descripcion
    } for tipo_documento in tipos_documento]
    return jsonify(resultado)

@tipo_documento_v1_bp.route('/<string:id_tipo_documento>', methods=['GET'])
def obtener_tipo_documento(id_tipo_documento):
    tipo_documento = TipoDocumento.query.get(id_tipo_documento)
    if not tipo_documento:
        return jsonify({'mensaje': 'Tipo de Documento no encontrado'}), 404

    resultado = {
        'id_tipo_documento': tipo_documento.id_tipo_documento,
        'descripcion': tipo_documento.descripcion
    }
    return jsonify(resultado)
