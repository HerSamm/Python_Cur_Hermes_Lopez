
from flask import Flask, request, jsonify
from cliente import cliente

app = Flask(__name__)
app.register_blueprint(cliente)

@app.route('/login', methods=['POST'])
def llamarServicioSet():
    global user, password
    user = request.json['user']
    password = request.json['password']
    inicializarVariables(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': user,
        'accion': accion
    }
    return jsonify(salida)


def inicializarVariables(user, password):
    global codRes, menRes, accion
    userLocal = "hlopez"
    passLocal = "unida2025"
    codRes = 'SIN_ERROR'
    menRes = 'OK'

    try:
        print("Verificar login")
        if str(password) == str(passLocal) and str(user) == str(userLocal):
            print("Usuario y contraseña OK")
            accion = "Succes"
        else:
            print("Usuario o contraseña incorrecta")
            accion = "Usuario o contraseña incorrecta"
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'
    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, accion


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)
