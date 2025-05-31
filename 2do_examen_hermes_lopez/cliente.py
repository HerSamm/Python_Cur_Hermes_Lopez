from flask import Blueprint, request, jsonify
cliente = Blueprint('cliente', __name__)
@cliente.route('/cliente', methods=['POST'])

def llamarServicioSet():
    global ci
    ci = request.json['ci']
    inicializarVariables(ci)

    salida = { 'codRes': codRes, 'menRes': menRes, 'ci': ci, 'accion': accion }
    return jsonify(salida)

def inicializarVariables(ci):
    global codRes, menRes, accion
    cilocal = "5438133"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    try:
        print("Verificar Cliente")
        if str(ci) == str(cilocal):
            print("Cliente encontrado")
            accion = "Succes"
            codRes = "SIN_ERROR"
            menRes = "OK"
            ci     = "5438133"
        else:
            print("Cliente no existe")
            accion = "Cliente no está en el sistema"
            codRes = "ERROR"
            menRes = "Error Cliente"
    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, accion, ci