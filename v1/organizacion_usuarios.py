from flask import Blueprint, jsonify
from models import OrganizacionUsuario

organizacion_usuario_v1_bp = Blueprint('organizacion_usuario_v1', __name__, url_prefix='/v1/organizacion_usuarios')

@organizacion_usuario_v1_bp.route('/', methods=['GET'])
def obtener_organizacion_usuarios():
    organizacion_usuarios = OrganizacionUsuario.query.all()
    resultado = [{
        'id_organizacion_usuario': org_usuario.id_organizacion_usuario,
        'id_organizacion': org_usuario.id_organizacion,
        'id_usuario': org_usuario.id_usuario
    } for org_usuario in organizacion_usuarios]
    return jsonify(resultado)

@organizacion_usuario_v1_bp.route('/<string:id_organizacion_usuario>', methods=['GET'])
def obtener_organizacion_usuario(id_organizacion_usuario):
    org_usuario = OrganizacionUsuario.query.get(id_organizacion_usuario)
    if not org_usuario:
        return jsonify({'mensaje': 'Organización Usuario no encontrado'}), 404

    resultado = {
        'id_organizacion_usuario': org_usuario.id_organizacion_usuario,
        'id_organizacion': org_usuario.id_organizacion,
        'id_usuario': org_usuario.id_usuario
    }
    return jsonify(resultado)
