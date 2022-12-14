from flask import Blueprint, request
from flask import jsonify
from models.venta import Venta

venta = Blueprint('venta', __name__)

@venta.route('/registro_cliente', methods=["POST"])
def registro_cliente():
    if request.method == "POST":
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        domicilio = request.form["domicilio"]
        telefono = request.form["telefono"]
        cedula = request.form["cedula"]
        correo = request.form["correo"]
        valor = Venta.Registrar_cliente(
            nombres, apellidos, domicilio, telefono, cedula, correo)
        return str(valor)

@venta.route('/listar_cliente', methods=['GET'])
def listar_cliente():
    if request.method == 'GET':
        dato = Venta.Listar_cliente()
        return jsonify(dato)

@venta.route('/cambiar_estado_cliente', methods=["POST"])
def cambiar_estado_cliente():
    if request.method == "POST":
        id = request.form["id"]
        dato = request.form["dato"]
        valor = Venta.Cambiar_estado_cliente(id, dato)
        return str(valor)

@venta.route('/editar_cliente', methods=["POST"])
def editar_cliente():
    if request.method == "POST":
        id = request.form["id"]
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        domicilio = request.form["domicilio"]
        telefono = request.form["telefono"]
        cedula = request.form["cedula"]
        correo = request.form["correo"]
        valor = Venta.Editar_cliente(nombres, apellidos, domicilio, telefono, cedula, correo, id)
        return str(valor)
