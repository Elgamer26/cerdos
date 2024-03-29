from flask import Blueprint, request
from flask import jsonify
from models.vacunas import Vacunas  
import time
from os import getcwd, path, remove

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
vacunas = Blueprint('vacunas', __name__)
PATH_FILE = getcwd() + "/static/uploads/vacuna/"

# controlador para registra el calendario
@vacunas.route('/calendario_registrar', methods=['POST'])
def calendario_registrar():
    if request.method == 'POST':
  
        titulo = request.form['titulo'] 
        galpon = request.form['galpon']
        descripcion = request.form['descripcion']
        tipo = request.form['tipo']
        fecha_evento = request.form['fecha_evento']
        color = request.form['color'] 
        color_etiqueta = request.form['color_etiqueta']  
        
        dato = Vacunas.Calendario_registrar(titulo, descripcion, tipo, fecha_evento, color, color_etiqueta, galpon)
        return str(dato)

# controlador para listar los eventos del calendario
@vacunas.route('/listar_calendario', methods=['GET'])
def listar_calendario():
    if request.method == 'GET':
        dato = Vacunas.Listar_calendario()
        return jsonify(dato)
    
@vacunas.route('/listar_calendario_tabla', methods=['GET'])
def listar_calendario_tabla():
    if request.method == 'GET':
        dato = Vacunas.Listar_calendario_tabla()
        return jsonify(dato)

@vacunas.route('/eliminar_evento_calendario', methods=['POST'])
def eliminar_evento_calendario():
    if request.method == 'POST':   
        _id = request.form['id']     
        dato = Vacunas.Eliminar_evento_calendario(_id)
        return str(dato)
    
# controlador para editar el calendario
@vacunas.route('/calendario_editar', methods=['POST'])
def calendario_editar():
    if request.method == 'POST':
        
        id = request.form['id']
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        tipo = request.form['tipo']
        fecha_evento = request.form['fecha_evento']
        color = request.form['color'] 
        color_etiqueta = request.form['color_etiqueta']  
        
        dato = Vacunas.Calendario_editar(id, titulo, descripcion, tipo, fecha_evento, color, color_etiqueta)
        return str(dato)

# controlador para acciones de crear y editar el tipo de vacuna
@vacunas.route('/accion_tipo_vacuna', methods=['POST'])
def accion_tipo_insumo():
    if request.method == 'POST':
        
        funcion = request.form['funcion']
        if funcion == 'registra_tipo_vacuna':       
            _valor = request.form['valor']
            dato = Vacunas.Registrar_tipo_vacuna(_valor)
            return jsonify(dato)

        elif funcion == 'editar_tipo_vacuna':  
            _id = request.form['id']     
            _dato = request.form['valor']
            dato = Vacunas.Editar_tipo_vacuna(_id,_dato)
            return jsonify(dato)

        elif funcion == 'estado_tipo_vacuna':   
            _id = request.form['id']    
            _valor = request.form['dato']
            dato = Vacunas.Estado_tipo_vacuna(_id,_valor)
            return jsonify(dato)

# controlador para listar el tipo de vacuna
@vacunas.route('/Listar_tipo_vacuna', methods=['GET'])
def Listar_tipo_vacuna():
    if request.method == 'GET':
        dato = Vacunas.Listar_tipo_vacuna()
        return jsonify(dato)

# controlador para crear la vacuna
@vacunas.route('/crear_vacuna_cerdos', methods=['POST'])
def crear_vacuna_cerdos():
    if request.method == 'POST':
        _codigo = request.form['codigo']
        _nombre = request.form['nombre']
        _tipo = request.form['tipo'] 
        _cantidad = request.form['cantidad']
        _precio = request.form['precio'] 
        _detalle = request.form['detalle']
        _presentacion = request.form['presentacion']
        
        _registro_sani = request.form['registro_sani']
        _cantidad_dosis = request.form['cantidad_dosis']
        
        _foto = request.files.get("foto", False)

        if _foto:
            # cerdo con foto
            hora_ac = time.strftime('%Y%m%d%H%M%S_', time.localtime())
            archivo = hora_ac + _foto.filename             
            dato = Vacunas.Crear_vacuna(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, _presentacion, archivo, _registro_sani, _cantidad_dosis)
            if dato == 1:
                _foto.save(PATH_FILE + archivo)
                return str(dato)
            else:
                return str(dato)        
        else:
            # cerdo sin foto
            archivo = "vacuna.jpg"
            dato = Vacunas.Crear_vacuna(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, _presentacion, archivo, _registro_sani, _cantidad_dosis)
            return str(dato)

# controlador para listar la vacunas
@vacunas.route('/listar_vacunas', methods=['GET'])
def listar_vacunas():
    if request.method == 'GET':
        dato = Vacunas.Listar_vacunas()
        return jsonify(dato)
    
# controlador para listar la vacunas lotes
@vacunas.route('/listar_vacunas_lotes', methods=['GET'])
def listar_vacunas_lotes():
    if request.method == 'GET':
        dato = Vacunas.Listar_vacunas_lotes()
        return jsonify(dato)

# controlador para cambiar el estado de la vacuna
@vacunas.route('/estado_vacuna', methods=['POST'])
def estado_vacuna():
    if request.method == 'POST':   
        _id = request.form['id']    
        _dato = request.form['dato']
        dato = Vacunas.Estado_vacuna(_id,_dato)
        return jsonify(dato)
    
#para eliminra  el lot de vacunas
@vacunas.route('/eliminar_lote_vacuna_a', methods=['POST'])
def eliminar_lote_vacuna_a():
    if request.method == 'POST':   
        _id = request.form['id']     
        dato = Vacunas.Eliminar_lote_vacuna(_id)
        return jsonify(dato)

# controlador para editar la vacuna
@vacunas.route('/editar_vacuna', methods=['POST'])
def editar_vacuna():
    if request.method == 'POST':
        _id = request.form['id']
        _codigo = request.form['codigo']
        _nombre = request.form['nombre']
        _tipo = request.form['tipo'] 
        _cantidad = request.form['cantidad']
        _precio = request.form['precio'] 
        _detalle = request.form['detalle']
        _presentacion = request.form['presentacion'] 
        
        _registro_sani = request.form['registro_sani']
        _cantidad_dosis = request.form['cantidad_dosis'] 

        dato = Vacunas.Editar_vacuna(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, _presentacion, _id, _registro_sani, _cantidad_dosis)
        return str(dato)

# controlador para cambiar la foto de la vacuna
@vacunas.route('/cambiar_foto_vacuna', methods=['POST'])
def cambiar_foto_vacuna():
    if request.method == 'POST':
        try:
            _id = request.form['id']
            foto_ac = request.form['ruta_actual']
            file = request.files.get("foto", False)

            hora_ac = time.strftime('%Y%m%d%H%M%S', time.localtime())
            archivo = hora_ac + file.filename

            data = Vacunas.Editar_foto_vacuna(_id, archivo)

            if data == 1:
                file.save(PATH_FILE + archivo)
                # para no eliminar la foto por defecto
                if foto_ac != "vacuna.jpg":
                    # esto es paar saber si el archivo existe y elimiarlo
                    if path.isfile(PATH_FILE + foto_ac) == True:
                        remove(PATH_FILE + foto_ac)
                
                return str(data)
            else:
                return str(data)
        except Exception as e:
            error = "Error " + str(e)
            return error

# controlador para traer la cantidad de vacunas
@vacunas.route('/traer_cantidad_vacunas', methods=['POST'])
def traer_cantidad_vacunas():
    if request.method == 'POST':   
        _id = request.form['id']     
        dato = Vacunas.Traer_cantidad_vacunas(_id)
        return jsonify(dato)

# controlador para registrar la vacunacion del cerdo
@vacunas.route('/registro_vacunacion_cerdo', methods=['POST'])
def registro_vacunacion_cerdo():
    if request.method == 'POST': 
        cerdo_id = request.form['cerdo_id']
        fecha = request.form['fecha']
        observacion = request.form['observacion'] 

        dato = Vacunas.Registro_vacunacion_cerdo(cerdo_id, fecha, observacion)
        return jsonify(dato)

# controlador para registra el detalle de la vacunacion
@vacunas.route('/registro_detalle_vacunacion_cerdo', methods=['POST'])
def registro_detalle_vacunacion_cerdo():
    if request.method == 'POST':

        _id = request.form['id']
        _idv = request.form['idv']
        _fecha = request.form['fecha']
        _cantidad = request.form['cantidad'] 
        _motivo = request.form['motivo']  

        idv = _idv.split(",")
        fecha = _fecha.split(",")
        cantidad = _cantidad.split(",") 
        motivo = _motivo.split(",") 

        for valor in zip(idv, fecha, cantidad, motivo):
            dato = Vacunas.Registro_detalle_vacunacion_cerdo(_id, valor[0], valor[1], valor[2], valor[3])  
        return jsonify(dato)

# controlador para anular la vacunación del cerdo
@vacunas.route('/anular_vacunacion_cerdo', methods=['POST'])
def anular_vacunacion_cerdo():    
    if request.method == 'POST':
        _id = request.form['id']   
        dato = Vacunas.Anular_vacunacion_cerdo(_id)   
        return str(dato)

# controlador para traer el historial de vacunacion del cerdo
@vacunas.route('/buscar_historia_vacunacion_cerdo', methods=['POST'])
def buscar_historia_vacunacion_cerdo():
    if request.method == 'POST':
        _id = request.form['id']  
        _f_i = request.form['f_i']  
        _f_f = request.form['f_f']  
 
        dato = Vacunas.Buscar_historia_vacunacion_cerdo(_id, _f_i, _f_f)  
        return jsonify(dato)

# controlador para traer el detalles de vacunas del cerdo
@vacunas.route('/ver_detalle_vacunas_cerdo', methods=['POST'])
def ver_detalle_vacunas_cerdo():
    if request.method == 'POST':
        _id = request.form['id']   
 
        dato = Vacunas.Ver_detalle_vacunas_cerdo(_id)  
        return jsonify(dato)

# controlador para traer la cantidad de medicamento
@vacunas.route('/traer_cantidad_medicamento', methods=['POST'])
def traer_cantidad_medicamento():
    if request.method == 'POST':   
        _id = request.form['id']     
        dato = Vacunas.Traer_cantidad_medicamento(_id)
        return jsonify(dato)

# controlador para registrar la desparasitacion del cerdo
@vacunas.route('/registro_desparasitacion_cerdo', methods=['POST'])
def registro_desparasitacion_cerdo():
    if request.method == 'POST': 
        cerdo_id = request.form['cerdo_id']
        fecha = request.form['fecha']
        observacion = request.form['observacion'] 

        dato = Vacunas.Registro_desparasitacion_cerdo(cerdo_id, fecha, observacion)
        return jsonify(dato)

# controlador para registra el detalle de la desparasitacion
@vacunas.route('/registro_detalle_desparasitacion_cerdo', methods=['POST'])
def registro_detalle_desparasitacion_cerdo():
    if request.method == 'POST':

        _id = request.form['id']
        _idv = request.form['idv']
        _fecha = request.form['fecha']
        _cantidad = request.form['cantidad'] 
        _motivo = request.form['motivo']  

        idv = _idv.split(",")
        fecha = _fecha.split(",")
        cantidad = _cantidad.split(",") 
        motivo = _motivo.split(",") 

        for valor in zip(idv, fecha, cantidad, motivo):
            dato = Vacunas.Registro_detalle_desparasitacion_cerdo(_id, valor[0], valor[1], valor[2], valor[3])  
        return jsonify(dato)

# controlador para anular la desparasitacion del cerdo
@vacunas.route('/anular_desparasitacion_cerdo', methods=['POST'])
def anular_desparasitacion_cerdo():    
    if request.method == 'POST':
        _id = request.form['id']   
        dato = Vacunas.Anular_desparasitacion_cerdo(_id)   
        return str(dato)

# controlador para traer el historial de desparasitacion del cerdo
@vacunas.route('/buscar_historia_desparasitacion_cerdo', methods=['POST'])
def buscar_historia_desparasitacion_cerdo():
    if request.method == 'POST':
        _id = request.form['id']  
        _f_i = request.form['f_i']  
        _f_f = request.form['f_f']  
 
        dato = Vacunas.buscar_historia_desparasitacion_cerdo(_id, _f_i, _f_f)  
        return jsonify(dato)

# controlador para traer el detalles de desparasitantes del cerdo
@vacunas.route('/ver_detalle_desparsitantes_cerdo', methods=['POST'])
def ver_detalle_desparsitantes_cerdo():
    if request.method == 'POST':
        _id = request.form['id']   
 
        dato = Vacunas.Ver_detalle_desparsitantes_cerdo(_id)  
        return jsonify(dato)
