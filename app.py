from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Configuración de la aplicación
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referidos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

# Modelo de Referido


class Referido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100), nullable=False)
    curso_interes = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), default='pendiente')
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

# Modelo de Incentivo


class Incentivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referido_id = db.Column(db.Integer, db.ForeignKey(
        'referido.id'), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    fecha_entrega = db.Column(db.DateTime, default=datetime.utcnow)

# Rutas principales


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/referidos', methods=['POST'])
def registrar_referido():
    data = request.json
    try:
        referido = Referido(
            nombre=data['nombre'],
            contacto=data['contacto'],
            curso_interes=data['curso_interes']
        )
        db.session.add(referido)
        db.session.commit()
        return jsonify({'message': 'Referido registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/referidos', methods=['GET'])
def listar_referidos():
    referidos = Referido.query.all()
    return render_template('referidos.html', referidos=referidos)


@app.route('/referidos/<int:referido_id>', methods=['PUT'])
def actualizar_estado_referido(referido_id):
    data = request.json
    referido = Referido.query.get(referido_id)
    if not referido:
        return jsonify({'error': 'Referido no encontrado'}), 404

    try:
        referido.estado = data['estado']
        db.session.commit()
        return jsonify({'message': 'Estado del referido actualizado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/incentivos', methods=['POST'])
def registrar_incentivo():
    data = request.json
    referido = Referido.query.get(data['referido_id'])
    if not referido:
        return jsonify({'error': 'Referido no encontrado'}), 404

    try:
        incentivo = Incentivo(
            referido_id=referido.id,
            descripcion=data['descripcion']
        )
        db.session.add(incentivo)
        db.session.commit()
        return jsonify({'message': 'Incentivo registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/dashboard', methods=['GET'])
def dashboard():
    referidos = Referido.query.all()
    conversiones = Referido.query.filter_by(estado='matriculado').count()
    total_referidos = len(referidos)
    pendientes = Referido.query.filter_by(estado='pendiente').count()
    report = {
        'total_referidos': total_referidos,
        'conversiones': conversiones,
        'pendientes': pendientes
    }
    return render_template('dashboard.html', report=report)



@app.route('/actualizar', methods=['GET'])
def actualizar_referidos():

    return render_template('referidos.html')

@app.route('/incentivos', methods=['GET'])
def registrar_incentivos():

    return render_template('incentivos.html')
    
@app.route('/registrar', methods=['GET', 'POST'])
def registrar_referido():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        curso_interes = request.form['curso_interes']
        referido = Referido(nombre=nombre, contacto=contacto,
                            curso_interes=curso_interes)
        db.session.add(referido)
        db.session.commit()
        return render_template('success.html', message="Referido registrado exitosamente.")
    return render_template('registrar.html')
    


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
