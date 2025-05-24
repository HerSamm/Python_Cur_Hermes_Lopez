from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)
    
clientes_existentes = ["5438133"]

@cliente.route('/cliente', methods=['POST'])
def verificar_cliente():
    try:
        data = request.get_json()
        ci = data.get("ci")

        if ci in clientes_existentes:
            return jsonify({
                "accion": "Success",
                "codRes": "SIN_ERROR",
                "menRes": "OK",
                "ci": ci
            })
        else:
            return jsonify({
                "accion": "Cliente no está en el sistema",
                "codRes": "ERROR",
                "menRes": "Error cliente",
                "ci": ci
            })

    except Exception as e:
        return jsonify({
            "accion": "Error interno",
            "codRes": "ERROR",
            "menRes": f"Msg: {str(e)}",
            "ci": ""
        })
