from flask import Blueprint, jsonify
from models import TipoEmail

tipo_email_v1_bp = Blueprint('tipo_email_v1', __name__, url_prefix='/v1/tipo_email')

@tipo_email_v1_bp.route('/', methods=['GET'])
def obtener_tipos_email():
    tipos_email = TipoEmail.query.all()
    resultado = [{
        'id_tipo_email': tipo_email.id_tipo_email,
        'descripcion': tipo_email.descripcion
    } for tipo_email in tipos_email]
    return jsonify(resultado)

@tipo_email_v1_bp.route('/<string:id_tipo_email>', methods=['GET'])
def obtener_tipo_email(id_tipo_email):
    tipo_email = TipoEmail.query.get(id_tipo_email)
    if not tipo_email:
        return jsonify({'mensaje': 'Tipo de Email no encontrado'}), 404

    resultado = {
        'id_tipo_email': tipo_email.id_tipo_email,
        'descripcion': tipo_email.descripcion
    }
    return jsonify(resultado)
