from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_tarro = 9000
        total_sin = tarros * precio_tarro

        if 18 <= edad <= 30:
            porcentaje_desc = 0.15
        elif edad > 30:
            porcentaje_desc = 0.25
        else:
            porcentaje_desc = 0.0

        descuento = total_sin * porcentaje_desc
        total_con = total_sin - descuento

        resultado = {
            'nombre': nombre,
            'total_sin': int(total_sin),
            'descuento': int(descuento),
            'total_con': int(total_con)
        }
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        contrasena = request.form['contrasena'].strip()

        if nombre == "juan" and contrasena == "admin":
            mensaje = "Bienvenido Administrador juan"
        elif nombre == "pepe" and contrasena == "user":
            mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
