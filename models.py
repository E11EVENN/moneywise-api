
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pais(db.Model):
    __tablename__ = 'pais'
    __table_args__ = {'schema': 'public'}

    id_pais = db.Column(db.String(5), primary_key=True)  # Longitud cambiada a 5 para coincidir con CHAR(5)
    nombre = db.Column(db.String(40), nullable=False)  # VARCHAR(40) coincide con String(40)
    indicativo_telefonico = db.Column(db.Numeric(5, 0), nullable=False)  # Precisión cambiada a 5
    estado = db.Column(db.String(10), nullable=False)  # VARCHAR(10) se refleja como String(10)
    fecha_registro = db.Column(db.DateTime(timezone=True), nullable=True)  # Corregido el typo y cambiado a DateTime
    fecha_actualizacion = db.Column(db.DateTime(timezone=True), nullable=True, onupdate=datetime.utcnow)
    usuario_id = db.Column(db.String(15), nullable=False)  # NOT NULL agregado
    id_address = db.Column(db.Numeric(10, 0), nullable=True)  # Tipo cambiado a Numeric y nullable True

    def __repr__(self):
        return f"<Pais(id_pais='{self.id_pais}', nombre='{self.nombre}', indicativo_telefonico={self.indicativo_telefonico}, estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}', id_usuario='{self.id_usuario}', id_address='{self.id_address}')>"
    
    
class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id_ciudad = db.Column(db.Integer, primary_key=True)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id_departamento'), nullable=True)
    nombre = db.Column(db.String(40), nullable=False)
    indicativo = db.Column(db.String(4), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

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
    id_pais = db.Column(db.String(3), db.ForeignKey('public.pais.id_pais'))
    nombre = db.Column(db.String(30), nullable=False)
    indicativo = db.Column(db.String(3), nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    estado = db.Column(db.Numeric(1), nullable=False)
    id_usuario = db.Column(db.String(10))
    ip_address = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"<Depto(id_departamento='{self.id_departamento}', nombre='{self.nombre}', indicativo='{self.indicativo}', fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}', estado={self.estado}, id_usuario='{self.id_usuario}', op_address='{self.op_address}')>"



class Cliente(db.Model):
    __tablename__ = 'cliente'
    __table_args__ = {'schema': 'public'}

    id_cliente = db.Column(db.Numeric(10), primary_key=True)
    id_ciudad = db.Column(db.String(255))
    id_cliente_email = db.Column(db.String(255))
    id_direccion = db.Column(db.String(255))
    id_tipo_telefono = db.Column(db.Numeric(10))
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(30))
    documento = db.Column(db.String(10))
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Cliente(id_cliente={self.id_cliente}, id_ciudad='{self.id_ciudad}', id_cliente_email='{self.id_cliente_email}', id_direccion='{self.id_direccion}', id_tipo_telefono={self.id_tipo_telefono}, nombre='{self.nombre}', apellido='{self.apellido}', documento='{self.documento}', fecha_registro='{self.fecha_registro}')>"


# ... Otros modelos si es necesario