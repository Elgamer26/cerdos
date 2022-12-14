from flask import Blueprint, request
from flask import jsonify
from models.galpon import Galpon
import time

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
galpon = Blueprint('galpon', __name__)

# controlador para crear el tipo de galpon
@galpon.route('/crear_tipo_g', methods=['POST'])
def crear_tipo_g():
    if request.method == 'POST':
        _tipo_g = request.form['tipo_g']
        dato = Galpon.Crear_tipo_galpo(_tipo_g)
        return jsonify(dato)

# controlador para listar el tipo de galpon
@galpon.route('/listar_tipo_galpon', methods=['GET'])
def listar_tipo_galpon():
    if request.method == 'GET':
        dato = Galpon.Listar_tipo_galpon()
        return jsonify(dato)

# controlador para estado del tipo de galpon
@galpon.route('/estado_tipo_g', methods=['POST'])
def estado_tipo_g():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Galpon.Estado_tipo_g(_id, _dato)
        return str(dato)

# controlador para editar el tipo de galpon
@galpon.route('/editar_tipo_g', methods=['POST'])
def editar_tipo_g():
    if request.method == 'POST':
        _tipo_g = request.form['tipo_g']
        _id = request.form['id']
        dato = Galpon.Editar_tipo_g(_tipo_g, _id)
        return jsonify(dato)

# controlador para crear el galpon
@galpon.route('/crear_galpon', methods=['POST'])
def crear_galpon():
    if request.method == 'POST':
        _numero = request.form['numero']
        _id_tipo = request.form['id_tipo']
        _capacidad = request.form['capacidad']
        _observacion = request.form['observacion']
        dato = Galpon.Crear_galpon(_numero, _id_tipo, _capacidad, _observacion)
        return jsonify(dato)

# controlador para listar el galpon
@galpon.route('/listar_galpon', methods=['GET'])
def listar_galpon():
    if request.method == 'GET':
        dato = Galpon.Listar_galpon()
        return jsonify(dato)

# controlador para estado del galpon
@galpon.route('/estado_galpon', methods=['POST'])
def estado_galpon():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Galpon.Estado_galpon(_id, _dato)
        return str(dato)

# controlador para crear el galpon
@galpon.route('/editar_galpon', methods=['POST'])
def editar_galpon():
    if request.method == 'POST':
        _id = request.form['id']
        _numero = request.form['numero']
        _id_tipo = request.form['id_tipo']
        _capacidad = request.form['capacidad']
        _observacion = request.form['observacion']
        dato = Galpon.Editar_galpon(_id, _numero, _id_tipo, _capacidad, _observacion)
        return jsonify(dato)

# controlador para listar no cerdos que no tienen galpon
@galpon.route('/listar_cerdo_galpon', methods=['GET'])
def listar_cerdo_galpon():
    if request.method == 'GET':
        dato = Galpon.Listar_cerdo_galpon()
        return jsonify(dato)

# controlador para traer la capacidad y disponibilidad
@galpon.route('/traer_disponible_capacidad', methods=['POST'])
def traer_disponible_capacidad():
    if request.method == 'POST':
        _id = request.form['id']
        dato = Galpon.Traer_disponible_capacidad(_id)
        return jsonify(dato)
    
##############
############# coreccion
# controlador para traer la capacidad y disponibilidad
@galpon.route('/traer_capacidad_galponn', methods=['POST'])
def traer_capacidad_galponn():
    if request.method == 'POST':
        _id = request.form['id']
        dato = Galpon.Traer_capacidad_galponn(_id)
        return jsonify(dato)
##############

# controlador para registra el galpn con el cerdo
@galpon.route('/registrar_cerdo_galpon', methods=['POST'])
def registrar_cerdo_galpon():
    if request.method == 'POST':

        _id = request.form['id_galpon']
        _id_c = request.form['id_c']
        _fecha = request.form['fecha'] 

        id_c = _id_c.split(",")
        fecha = _fecha.split(",") 

        for valor in zip(id_c, fecha):
            dato = Galpon.Registrar_cerdo_galpon(_id, valor[0], valor[1])         
        return jsonify(dato)
    
#####################
# controlador para registra el galpn con el cerdo
@galpon.route('/registrar_cerdo_galpon_new', methods=['POST'])
def registrar_cerdo_galpon_new():
    if request.method == 'POST':

        id_galpon = request.form['id_galpon']
        fecha_i = request.form['fecha_i']
        fecha_f = request.form['fecha_f'] 
        semanas = request.form['semanas']  

        dato = Galpon.Registrar_cerdo_galpon_new(id_galpon, fecha_i, fecha_f, semanas)         
        return jsonify(dato)

@galpon.route('/registrar_detalle_cerdo_galpon', methods=['POST'])
def registrar_detalle_cerdo_galpon():
    if request.method == 'POST':

        _id = request.form['id']
        _id_c = request.form['id_c']
        _fecha = request.form['fecha'] 

        id_c = _id_c.split(",")
        fecha = _fecha.split(",") 

        for valor in zip(id_c, fecha):
            dato = Galpon.Registrar_detalle_cerdo_galpon(_id, valor[0], valor[1])         
        return jsonify(dato)
    
#############

# controlador para pasar el cerdo a otro galpon
@galpon.route('/editar_cerdo_galpon', methods=['POST'])
def editar_cerdo_galpon():
    if request.method == 'POST':

        _id_f = request.form['id_f']
        _id_a = request.form['id_actual']
        _id_n = request.form['id_nuevo']
        _id_c = request.form['id_c'] 
        _fecha = request.form['fecha'] 
        _text = request.form['text'] 

        id_f = _id_f.split(",")
        id_c = _id_c.split(",")
        fecha = _fecha.split(",") 

        for valor in zip(id_c, fecha, id_f):
            dato = Galpon.Editar_cerdo_galpon(_id_a, _id_n, valor[0], valor[1], valor[2], _text)  
        return jsonify(dato)


######################
####################### correcciones
@galpon.route('/traer_cerdo_dentro_galpon', methods=['POST'])
def traer_cerdo_dentro_galpon():
    if request.method == 'POST':
        id = request.form['id']
        dato = Galpon.Traer_cerdo_dentro_galpon(id)         
        return jsonify(dato)
    
@galpon.route('/traer_cerdo_dentro_galpon_buscar', methods=['POST'])
def traer_cerdo_dentro_galpon_buscar():
    if request.method == 'POST':
        id = request.form['id']
        valor = request.form['valor']
        dato = Galpon.Traer_cerdo_dentro_galpon_buscar(id, valor)         
        return jsonify(dato)

##############################
## cantidad de cerdos en galpon
@galpon.route('/traer_cantidad_cerdos_glpon', methods=['POST'])
def traer_cantidad_cerdos_glpon():
    if request.method == 'POST':
        _id = request.form['id']
        dato = Galpon.Traer_cantidad_cerdos_glpon(_id)
        return jsonify(dato)
    
############ mover cerdos a nuevo galpon
@galpon.route('/guardar_cerdos_movimiento', methods=['POST'])
def guardar_cerdos_movimiento():
    if request.method == 'POST':
        id_anterior = request.form['id_anterior']
        id_cergo_galpon = request.form['id_cergo_galpon']
        galpon_nuevo = request.form['galpon_nuevo']
        dato = Galpon.Guardar_cerdos_movimiento(id_anterior, id_cergo_galpon, galpon_nuevo)
        return jsonify(dato)
    
############ LISTAR LOS GALPONES CON TODOS SUS CERDOS
@galpon.route('/listar_cerdos_en_galpon', methods=['GET'])
def listar_cerdos_en_galpon():
    if request.method == 'GET': 
        dato = Galpon.Listar_cerdos_en_galpon()
        return jsonify(dato)
    
@galpon.route('/listar_galpones', methods=['GET'])
def listar_galpones():
    if request.method == 'GET': 
        dato = Galpon.Listar_galpon_combooo()
        return jsonify(dato)