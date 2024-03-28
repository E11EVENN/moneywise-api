
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pais(db.Model):
    __tablename__ = 'pais'
    __table_args__ = {'schema': 'public'}


    id_pais = db.Column(db.String(3), primary_key=True)  # Cambiado a minúsculas
    nombre = db.Column(db.String(40), nullable=False)  # Cambiado a minúsculas
    indicativo_telefonico = db.Column(db.Numeric(4), nullable=False)  # Cambiado a minúsculas
    estado = db.Column(db.Numeric(1), nullable=False)  # Cambiado a minúsculas
    fecha_resgistro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)  # Cambiado a minúsculas
    fecha_actualizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Cambiado a minúsculas
    id_usuario = db.Column(db.String(10), nullable=True)  # Cambiado a minúsculas
    id_address = db.Column(db.String(15), nullable=True)  # Cambiado a minúsculas

    def __repr__(self):
        return f"<Pais(id_pais='{self.id}', nombre='{self.nombre}', indicativo_telefonico={self.indicativo_telefonico}, estado={self.estado}, fecha_resgistro='{self.fecha_resgistro}', fecha_actualizacion='{self.fecha_actualizacion}', id_usuario='{self.id_usuario}', id_address='{self.id_address}')>"

class Ciudad(db.Model):
    __tablename__ = 'ciudad'  # Asegúrate de que el nombre de la tabla es el correcto.
    # Aquí estamos definiendo cada columna explícitamente con el tipo apropiado.
    id_ciudad = db.Column(db.Integer, primary_key=True)  # Cambiando a Integer si id_ciudad es un número.
    id_departamento = db.Column(db.Integer, nullable=True)  # Asumiendo que es un número, cambia según sea necesario.
    nombre = db.Column(db.String(40), nullable=False)  # Asegúrate de que el tamaño es el correcto.
    indicativo = db.Column(db.String(4), nullable=False)  # Cambiando a String si es un VARCHAR en la base de datos.
    estado = db.Column(db.Boolean, nullable=False)  # Asumiendo que estado es un booleano.
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Usando DateTime de SQLAlchemy.
    fecha_actulizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Ciudad(id_ciudad={self.id_ciudad}, id_departamento={self.id_departamento}, nombre='{self.nombre}', indicativo='{self.indicativo}', estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}')>"


class Credito(db.Model):
    __tablename__ = 'credito'
    __table_args__ = {'schema': 'public'}

    id_credito = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, nullable=True)
    id_tipo_credito = db.Column(db.Integer, nullable=True)
    monto = db.Column(db.Numeric(10, 2), nullable=True)
    fecha_inicio = db.Column(db.Date, nullable=True)
    estado = db.Column(db.String(2), nullable=True)

    def __repr__(self):
        return f"<Credito(id_credito={self.id_credito}, id_cliente={self.id_cliente}, id_tipo_credito={self.id_tipo_credito}, monto={self.monto}, fecha_inicio='{self.fecha_inicio}', estado='{self.estado}')>"



class CreditoIntereses(db.Model):
    __tablename__ = 'credito_intereses'
    __table_args__ = {'schema': 'public'}

    id_credito_intereses = db.Column(db.Numeric(10), primary_key=True)
    interes = db.Column(db.Numeric(10), nullable=True)
    id_credito = db.Column(db.Numeric(10), db.ForeignKey('public.CREDITO.id_credito'), nullable=True)
    id_tipo_interes = db.Column(db.Numeric(10), nullable=True)

    def __repr__(self):
        return f"<CreditoIntereses(id_credito_intereses={self.id_credito_intereses}, interes={self.interes}, id_credito={self.id_credito}, id_tipo_interes={self.id_tipo_interes})>"

class Depto(db.Model):
    __tablename__ = 'depto'
    __table_args__ = {'schema': 'public'}

    id_departamento = db.Column(db.String(3), primary_key=True)
    id_pais = db.Column(db.String(3), db.ForeignKey('public.depto.id_depto'))
    nombre = db.Column(db.String(30), nullable=False)
    indicativo = db.Column(db.String(3), nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    estado = db.Column(db.Numeric(1), nullable=False)
    id_usuario = db.Column(db.String(10))
    op_address = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"<Depto(id_departamento='{self.id_departamento}', nombre='{self.nombre}', indicativo='{self.indicativo}', fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}', estado={self.estado}, id_usuario='{self.id_usuario}', op_address='{self.op_address}')>"


# ... Otros modelos si es necesario