from app import app, db, Referido

# Generar registros de referidos
referidos = [
    {"nombre": "Luis Fernández", "contacto": "luis.fernandez@email.com",
        "curso_interes": "Desarrollo Web"},
    {"nombre": "María González", "contacto": "maria.gonzalez@email.com",
        "curso_interes": "Marketing Digital"},
    {"nombre": "Jorge Pérez", "contacto": "jorge.perez@email.com",
        "curso_interes": "Python Avanzado"},
    {"nombre": "Lucía Ramírez", "contacto": "lucia.ramirez@email.com",
        "curso_interes": "Diseño Gráfico"},
    {"nombre": "Andrés Torres", "contacto": "andres.torres@email.com",
        "curso_interes": "Bases de Datos"},
    {"nombre": "Carla Méndez", "contacto": "carla.mendez@email.com",
        "curso_interes": "Machine Learning"},
    {"nombre": "Ricardo López", "contacto": "ricardo.lopez@email.com",
        "curso_interes": "Inteligencia Artificial"},
    {"nombre": "Valeria Vargas", "contacto": "valeria.vargas@email.com",
        "curso_interes": "Ciberseguridad"},
    {"nombre": "Fernando Martínez", "contacto": "fernando.martinez@email.com",
        "curso_interes": "JavaScript Básico"},
    {"nombre": "Sofía Castillo", "contacto": "sofia.castillo@email.com",
        "curso_interes": "Frontend con React"}
]

# Crear el contexto de la aplicación
with app.app_context():
    # Agregar referidos a la base de datos
    for r in referidos:
        referido = Referido(
            nombre=r["nombre"],
            contacto=r["contacto"],
            curso_interes=r["curso_interes"]
        )
        db.session.add(referido)

    db.session.commit()
    print("Referidos añadidos exitosamente.")
