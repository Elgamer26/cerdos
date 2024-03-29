from flask import Blueprint, request, render_template
from flask import jsonify
from models.venta import Venta
from flask_mail import Message
from utils.email import mail
from utils.Complemento import Complement

data = Complement.data_email()

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

@venta.route('/registra_veenta_cerdos', methods=["POST"])
def registra_veenta_cerdos():
    if request.method == "POST":
        cliente = request.form["cliente"]
        fecha_c = request.form["fecha_c"]
        numero_venta = request.form["numero_venta"]
        tipo_comprobante = request.form["tipo_comprobante"]
        iva = request.form["iva"]
        subtotal = request.form["subtotal"]
        impuesto_sub = request.form["impuesto_sub"]
        total_pagar = request.form['total_pagar']
        valor = Venta.Registra_veenta_cerdos(cliente, fecha_c, numero_venta, tipo_comprobante, iva, subtotal, impuesto_sub, total_pagar)
        return str(valor)

@venta.route('/registrar_detalle_venta_cerdo', methods=["POST"])
def registrar_detalle_venta_cerdo():
    if request.method == "POST":
        
        id = request.form["id"]
        idc = request.form["idc"]
        peso = request.form["peso"]
        precio = request.form["precio"]
        total = request.form["total"] 
        
        id_cerdo = idc.split(",")
        peso_cerdo = peso.split(",")
        precio_cerdo = precio.split(",")
        total_cerdo = total.split(",")
        
        for valor in zip(id_cerdo, peso_cerdo, precio_cerdo, total_cerdo):        
            valorr = Venta.Registrar_detalle_venta_cerdo(id, valor[0], valor[1], valor[2], valor[3])
        return str(valorr)
    
        # if str(valorr) == "1":
        #     try:
        #         cabecera = Venta.Cabecera_factura(id)
        #         detalle = Venta.Detalle_venta(id)
                                
        #         msg = Message('FACTURA DE VENTA CERDOS', 
        #             sender=data['correo'],
        #             recipients=[cabecera[2]])
                    
        #         valores =  {
        #             'cliente': cabecera,
        #             'detalle': detalle
        #         }
        #         msg.html = render_template('view/ventas/factura_venta.html', valores = valores)
        #         mail.send(msg)
        #         return str(valorr)
        #     except Exception as e:
        #         return str("Error: " + e)
        # else:
        #     return str(valorr)
    
@venta.route('/venta_cerdo_anular', methods=["POST"])
def venta_cerdo_anular():
    if request.method == "POST":
        id = request.form["id"] 
        valor = Venta.venta_cerdo_anular(id)
        return str(valor)

@venta.route('/envio_correo_venta', methods=["POST"])
def envio_correo_venta():
    if request.method == "POST":
        try:
            id = request.form["id"] 
            cabecera = Venta.Cabecera_factura(id)
            detalle = Venta.Detalle_venta(id)
                        
            # msg = Message('FACTURA DE VENTA CERDOS', 
            #     sender=data['correo'],
            #     recipients=[cabecera[2]])
            
            valores =  {
                'cliente': cabecera,
                'detalle': detalle
            }
            #msg.html = render_template('view/ventas/factura_venta.html', valores = valores)
            #mail.send(msg)
            html = render_template('view/ventas/factura_venta.html', valores = valores)
            
            return jsonify(html, cabecera[2])
        except Exception as e:
            return str(1)

## procesar pedidos de cerdos
@venta.route('/procesar_pedidos', methods=["POST"])
def procesar_pedidos():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        telefono = request.form["telefono"]
        cedula = request.form["cedula"]
        correo = request.form["correo"]
        direccion = request.form["direccion"] 
        subtotal = request.form["subtotal"]
        impuesto = request.form["impuesto"]
        total = request.form["total"] 
        valor = Venta.Procesar_pedidos(nombre, apellido, telefono, cedula, correo, direccion, subtotal, impuesto, total)
        return str(valor)

# registrar detalle de pedidos
@venta.route('/registrar_detalle_pedido', methods=["POST"])
def registrar_detalle_pedido():
    if request.method == "POST":
        
        id = request.form["id"]
        id_cerdo = request.form["id_cerdo"]
        peso = request.form["peso"]
        precio = request.form["precio"]
        total = request.form["total"] 
        
        id_cerdo = id_cerdo.split(",")
        peso_cerdo = peso.split(",")
        precio_cerdo = precio.split(",")
        total_cerdo = total.split(",")
        
        for valor in zip(id_cerdo, peso_cerdo, precio_cerdo, total_cerdo):        
            valorr = Venta.Registrar_detalle_pedido(id, valor[0], valor[1], valor[2], valor[3])
        return str(valorr)
        # if str(valorr) == "1":
        #     try:
        #         cabecera = Venta.Cabecera_pedido(id)
        #         detalle = Venta.Detalle_pedido_envio(id)
                                
        #         msg = Message('PEDIDO DE CERDOS', 
        #             sender=data['correo'],
        #             recipients=[cabecera[4]])
                    
        #         valores =  {
        #             'cliente': cabecera,
        #             'detalle': detalle
        #         }
        #         msg.html = render_template('view/ventas/pedido_cero_envio.html', valores = valores)
        #         mail.send(msg)
        #         return str(valorr)
        #     except Exception as e:
        #         return str("Error: " + e)
        # else:
        #     return str(valorr)

@venta.route('/listar_pedidos_cerdos', methods=['GET'])
def listar_pedidos_cerdos():
    if request.method == 'GET':
        dato = Venta.Listar_pedidos_cerdos()
        return jsonify(dato)

@venta.route('/envio_correo_pedido', methods=["POST"])
def envio_correo_pedido():
    if request.method == "POST":
        try:
            id = request.form["id"] 
            cabecera = Venta.Cabecera_pedido(id)
            detalle = Venta.Detalle_pedido_envio(id)
                        
            # msg = Message('PEDIDO DE CERDOS', 
            #     sender=data['correo'],
            #     recipients=[cabecera[4]])
            
            valores =  {
                'cliente': cabecera,
                'detalle': detalle
            }
            # msg.html = render_template('view/ventas/pedido_cero_envio.html', valores = valores)
            # mail.send(msg)
            
            html = render_template('view/ventas/pedido_cero_envio.html', valores = valores)
            return jsonify(html, cabecera[4])
        except Exception as e:
            return str(1)

@venta.route('/anuar_pedido_cerdos', methods=["POST"])
def anuar_pedido_cerdos():
    if request.method == "POST":
        id = request.form["id"] 
        valor = Venta.Anuar_pedido_cerdos(id)
        return str(valor)

@venta.route('/procesar_pedido', methods=["POST"])
def procesar_pedido():
    if request.method == "POST":
        id = request.form["id"] 
        valor = Venta.Procesar_pedido(id)
        return str(valor)
    
        # if str(valor) == "1":
        #     try:
        #         cabecera = Venta.Cabecera_pedido(id)
        #         detalle = Venta.Detalle_pedido_envio(id)
                                
        #         msg = Message('PEDIDO PROCESADO', 
        #             sender=data['correo'],
        #             recipients=[cabecera[4]])
                    
        #         valores =  {
        #             'cliente': cabecera,
        #             'detalle': detalle
        #         }
        #         msg.html = render_template('view/ventas/pedido_cero_envio.html', valores = valores)
        #         mail.send(msg)
        #         return str(valor)
        #     except Exception as e:
        #         return str("Error: " + e)
        # else:
        #     return str(valor)