# Referidos e Incentivos - Aplicación Flask

Este proyecto es una aplicación basada en Flask para la gestión de referidos e incentivos. Incluye la funcionalidad para registrar y listar referidos, actualizar su estado, registrar incentivos asociados a referidos, y generar reportes básicos.

## Características principales

- **Gestión de Referidos:**
  - Registrar nuevos referidos con nombre, contacto, curso de interés y estado inicial.
  - Actualizar el estado de los referidos (ejemplo: "pendiente" a "matriculado").
  - Listar todos los referidos en formato JSON.

- **Gestión de Incentivos:**
  - Registrar incentivos asociados a referidos específicos.

- **Panel de Reportes:**
  - Ver estadísticas sobre el número total de referidos, referidos pendientes y conversiones a "matriculado".

## Requisitos previos

1. **Python 3.7 o superior**.
2. **Entorno virtual (opcional, pero recomendado)**.
3. **Bibliotecas necesarias:**
   - Flask
   - Flask-SQLAlchemy

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO>
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea la base de datos:
   ```bash
   python app.py
   ```
   Esto generará un archivo `referidos.db` en el directorio raíz del proyecto.

## Uso

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

2. Accede a la aplicación en tu navegador en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Endpoints disponibles

### **Rutas de Referidos**

1. **Registrar un referido**
   ```http
   POST /referidos
   ```
   - **Cuerpo JSON:**
     ```json
     {
       "nombre": "Juan Pérez",
       "contacto": "juan@example.com",
       "curso_interes": "Inteligencia Artificial"
     }
     ```
   - **Respuesta:**
     ```json
     {
       "message": "Referido registrado exitosamente"
     }
     ```

2. **Listar referidos**
   ```http
   GET /referidos
   ```
   - **Respuesta:**
     ```json
     [
       {
         "id": 1,
         "nombre": "Juan Pérez",
         "contacto": "juan@example.com",
         "curso_interes": "Inteligencia Artificial",
         "estado": "pendiente",
         "fecha_creacion": "2024-12-21T00:00:00"
       }
     ]
     ```

3. **Actualizar el estado de un referido**
   ```http
   PUT /referidos/<referido_id>
   ```
   - **Cuerpo JSON:**
     ```json
     {
       "estado": "matriculado"
     }
     ```
   - **Respuesta:**
     ```json
     {
       "message": "Estado del referido actualizado"
     }
     ```

### **Rutas de Incentivos**

1. **Registrar un incentivo**
   ```http
   POST /incentivos
   ```
   - **Cuerpo JSON:**
     ```json
     {
       "referido_id": 1,
       "descripcion": "Descuento del 10% en la matrícula"
     }
     ```
   - **Respuesta:**
     ```json
     {
       "message": "Incentivo registrado exitosamente"
     }
     ```

### **Panel de Reportes**

1. **Generar reporte de referidos**
   ```http
   GET /dashboard
   ```
   - **Respuesta:**
     ```json
     {
       "total_referidos": 10,
       "conversiones": 5,
       "pendientes": 3
     }
     ```

## Estructura del Proyecto

```plaintext
.
├── app.py                # Código principal de la aplicación
├── referidos.db          # Base de datos SQLite (generada automáticamente)
├── templates/
│   └── index.html        # Página principal de la aplicación
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Documentación del proyecto
```

## Futuras Mejoras

- Agregar autenticación de usuarios para el acceso al dashboard.
- Implementar un sistema de notificaciones para los referidos.
- Mejorar la interfaz de usuario utilizando un framework como Bootstrap.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

