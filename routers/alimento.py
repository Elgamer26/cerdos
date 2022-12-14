from flask import Blueprint, request, session
from flask import jsonify
from models.alimento import Alimento 
from os import getcwd, path, remove
import time

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
alimento = Blueprint('alimento', __name__)
# para mover la imagen
PATH_FILE = getcwd() + "/static/uploads/alimento/"

# controlador para listar tipo de alimento
@alimento.route('/listar_tipo_alimento', methods=['GET'])
def listar_tipo_alimento():
    if request.method == 'GET':
        dato = Alimento.Listar_tipio_alimento()
        return jsonify(dato)

# controlador para acciones de crear y editar el tipo de alimento
@alimento.route('/acciones_tipo_alimento', methods=['POST'])
def acciones_tipo_alimento():
    if request.method == 'POST':
        
        funcion = request.form['funcion']
        if funcion == 'registrar_tipo_a':       
            _valor = request.form['valor']
            dato = Alimento.Registrar_tipo_alimento(_valor)
            return jsonify(dato)

        elif funcion == 'estado_alimento':  
            _id = request.form['id']     
            _dato = request.form['dato']
            dato = Alimento.Estado_alimento_tipo(_id,_dato)
            return jsonify(dato)

        elif funcion == 'editar_tipo_a':   
            _id = request.form['id']    
            _valor = request.form['valor']
            dato = Alimento.Editar_tipo_alimento(_id,_valor)
            return jsonify(dato)

# controlador para listar marca de alimento
@alimento.route('/listar_marca_alimento', methods=['GET'])
def listar_marca_alimento():
    if request.method == 'GET':
        dato = Alimento.Listar_marca_alimento()
        return jsonify(dato)

# controlador para acciones de crear y editar la marca de alimento
@alimento.route('/acciones_marca_alimento', methods=['POST'])
def acciones_marca_alimento():
    if request.method == 'POST':
        
        funcion = request.form['funcion']
        if funcion == 'registrar_marca_a':       
            _valor = request.form['valor']
            dato = Alimento.Registrar_marca_alimento(_valor)
            return jsonify(dato)

        elif funcion == 'estado_marca':  
            _id = request.form['id']     
            _dato = request.form['dato']
            dato = Alimento.Estado_marca(_id,_dato)
            return jsonify(dato)

        elif funcion == 'editar_marca_a':   
            _id = request.form['id']    
            _valor = request.form['valor']
            dato = Alimento.Editar_marca_alimento(_id,_valor)
            return jsonify(dato)

# controlador para crear el alimento
@alimento.route('/registrar_alimento', methods=['POST'])
def registrar_alimento():
    if request.method == 'POST':
        _codigo = request.form['codigo']
        _nombre = request.form['nombre']
        _tipo = request.form['tipo']
        _marca = request.form['marca']
        _cantidad = request.form['cantidad']
        _precio = request.form['precio']
        _peso = request.form['peso']
        _detalle = request.form['detalle']
        _foto = request.files.get("foto", False)

        if _foto:
            # cerdo con foto
            hora_ac = time.strftime('%Y%m%d%H%M%S_', time.localtime())
            archivo = hora_ac + _foto.filename             
            dato = Alimento.Craer_alimento(_codigo, _nombre, _tipo, _marca, _cantidad, _precio, _peso, _detalle, archivo)
            if dato == 1:
                _foto.save(PATH_FILE + archivo)
                return str(dato)
            else:
                return str(dato)        
        else:
            # cerdo sin foto
            archivo = "alimento.jpg"
            dato = Alimento.Craer_alimento(_codigo, _nombre, _tipo, _marca, _cantidad, _precio, _peso, _detalle, archivo)
            return str(dato)

# controlador para listar marca de alimento
@alimento.route('/listar_alimentos', methods=['GET'])
def listar_alimentos():
    if request.method == 'GET':
        dato = Alimento.Listar_alimentos()
        return jsonify(dato)
    
# controlador para listar marca de alimento lote
@alimento.route('/listar_lote_alimento', methods=['GET'])
def listar_lote_alimento():
    if request.method == 'GET':
        dato = Alimento.Listar_lote_alimento()
        return jsonify(dato)
        
# controlador para estado de alimento
@alimento.route('/estado_alimento', methods=['POST'])
def estado_alimento():
    if request.method == 'POST':
        _id = request.form['id']     
        _dato = request.form['dato']
        dato = Alimento.Estado_alimento(_id,_dato)
        return jsonify(dato)
    
# eliminar lote de alimento
@alimento.route('/eliminar_lote_alimento', methods=['POST'])
def eliminar_lote_alimento():
    if request.method == 'POST':
        _id = request.form['id']      
        dato = Alimento.Eliminar_lote_alimento(_id)
        return jsonify(dato)

# controlador para cambiar la foto del alimento
@alimento.route('/cambiar_foto_alimento', methods=['POST'])
def cambiar_foto_alimento():
    if request.method == 'POST':
        try:
            _id = request.form['id']
            foto_ac = request.form['ruta_actual']
            file = request.files.get("foto", False)

            hora_ac = time.strftime('%Y%m%d%H%M%S', time.localtime())
            archivo = hora_ac + file.filename

            data = Alimento.Cambiar_foto_alimento(_id, archivo)

            if data == 1:
                file.save(PATH_FILE + archivo)
                # para no eliminar la foto por defecto
                if foto_ac != "alimento.jpg":
                    # esto es paar saber si el archivo existe y elimiarlo
                    if path.isfile(PATH_FILE + foto_ac) == True:
                        remove(PATH_FILE + foto_ac)
                
                return str(data)
            else:
                return str(data)
        except Exception as e:
            error = "Error " + str(e)
            return error

# controlador para editar el alimento
@alimento.route('/editar_alimento', methods=['POST'])
def editar_alimento():
    if request.method == 'POST':
        _codigo = request.form['codigo']
        _nombre = request.form['nombre']
        _tipo = request.form['tipo']
        _marca = request.form['marca']
        _cantidad = request.form['cantidad']
        _precio = request.form['precio']
        _peso = request.form['peso']
        _detalle = request.form['detalle'] 
        _id = request.form['id']  
        
        dato = Alimento.Editar_alimento(_codigo, _nombre, _tipo, _marca, _cantidad, _precio, _peso, _detalle, _id)
        return str(dato)

# controlador para listar tipo de alimentacion
@alimento.route('/listar_tipo_alimentacion', methods=['GET'])
def listar_tipo_alimentacion():
    if request.method == 'GET':
        dato = Alimento.Listar_tipio_alimentacion()
        return jsonify(dato)

# controlador para acciones de crear y editar el tipo de alimentacion
@alimento.route('/acciones_tipo_alimentacionn', methods=['POST'])
def acciones_tipo_alimentacionn():
    if request.method == 'POST':
        
        funcion = request.form['funcion']
        if funcion == 'registrar_tipo_alimentacion':       
            _valor = request.form['valor']
            dato = Alimento.Registrar_tipo_alimentacion(_valor)
            return jsonify(dato)

        elif funcion == 'estado_alimentacion':  
            _id = request.form['id']     
            _dato = request.form['dato']
            dato = Alimento.Estado_alimentacion(_id,_dato)
            return jsonify(dato)

        elif funcion == 'editar_tipo_alimentacion':   
            _id = request.form['id']    
            _valor = request.form['valor']
            dato = Alimento.Editar_tipo_alimentacion(_id,_valor)
            return jsonify(dato)

# controlador para el select del alimento del cerdo
@alimento.route('/select_alimento_cerdo', methods=['POST'])
def select_alimento_cerdo():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Select_alimento_cerdo(_id)
        return jsonify(dato)
    
# controlador para el select del alimento del cerdo por lotes
@alimento.route('/select_alimento_cerdo_lote', methods=['POST'])
def select_alimento_cerdo_lote():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Select_alimento_cerdo_lote(_id)
        return jsonify(dato)
    
# controlador para traer cantidas kg lotes
@alimento.route('/traer_cantidad_lote_kg', methods=['POST'])
def traer_cantidad_lote_kg():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Traer_cantidad_lote_kg(_id)
        return jsonify(dato)
    
# controlador para traer la cantidad de sacos de alimento
@alimento.route('/traer_cantida_saco_alimento', methods=['POST'])
def traer_cantida_saco_alimento():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Traer_cantida_saco_alimento(_id)
        return jsonify(dato)

# controlador para el select de galpon cerdo
@alimento.route('/select_cerdo_galpon', methods=['POST'])
def select_cerdo_galpon():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Select_cerdo_galpon(_id)
        return jsonify(dato)

# controlador para peso del cerdo
@alimento.route('/traer_peso_cerdo_actual', methods=['POST'])
def traer_peso_cerdo_actual():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Traer_peso_cerdo_actual(_id)
        return jsonify(dato)

# controlador para guadar la alimentacion
@alimento.route('/guardar_la_alimentacion', methods=['POST'])
def guardar_la_alimentacion():
    if request.method == 'POST':
        _id = session['id_usu']
        _alimento_id = request.form['alimento_id']
        _tipo_id = request.form['tipo_id']
        _fecha_c = request.form['fecha_c']
        _cantidad_sacos = request.form['cantidad_sacos']
        _observacion = request.form['observacion'] 
        
        dato = Alimento.Guardar_la_alimentacion(_alimento_id, _tipo_id, _fecha_c, _cantidad_sacos, _observacion, _id)
        
        return str(dato)

# controlador para registra el detalle de alimentacion del cerdo
@alimento.route('/guardar_detalle_alimentacion', methods=['POST'])
def guardar_detalle_alimentacion():
    if request.method == 'POST':

        _id = request.form['id']
        _idc = request.form['idc']
        _peso = request.form['peso']  

        idc = _idc.split(",")
        peso = _peso.split(",") 

        for valor in zip(idc, peso):
            dato = Alimento.Guardar_detalle_alimentacion(_id, valor[0], valor[1])  
        return jsonify(dato)

# controlador para registra el peso del cerdo
@alimento.route('/guardar_pesaje_cerdo', methods=['POST'])
def guardar_pesaje_cerdo():
    if request.method == 'POST':
        
        id = request.form['id']
        peso_pasado = request.form['peso_actual']
        metodo = request.form['metodo']  
        observacion = request.form['observacion']
        etapa_fase = request.form['etapa_fase']
        nuevo_pesaje = request.form['nuevo_pesaje']  
        semana = request.form['semana'] 
        
        perimetro_t = request.form['perimetro_t']  
        largo_c = request.form['largo_c'] 

        dato = Alimento.Guardar_peso_cerdo(id,peso_pasado,metodo,observacion,etapa_fase,nuevo_pesaje,perimetro_t,largo_c,semana)  
        return str(dato)

# controlador para traer los datos del pessaje del cerdo
@alimento.route('/traer_pesos_cerdo', methods=['POST'])
def traer_pesos_cerdo():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Traer_pesos_cerdo(_id)  
        return jsonify(dato)

# controlador para traer los datos de la alimentacion del cerdo
@alimento.route('/traer_alimentos_del_cerdo', methods=['POST'])
def traer_alimentos_del_cerdo():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.traer_alimentos_del_cerdo(_id)  
        return jsonify(dato)

# controlador para eliminar peso del cerdo
@alimento.route('/eliminar_peso', methods=['POST'])
def eliminar_peso():
    if request.method == 'POST': 
        _id = request.form['id']  
        
        dato = Alimento.Eliminar_peso(_id)
        return str(dato)



################
############### corregido 
@alimento.route('/registrar_toda_alimentacion', methods=['POST'])
def registrar_toda_alimentacion():
    if request.method == 'POST':
        _id = session['id_usu']
        _alimento_id = request.form['alimento_id']
        _tipo_id = request.form['tipo_id']
        _fecha_c = request.form['fecha_c']
        _cantidad_kg = request.form['cantidad_kg']
        _observacion = request.form['observacion'] 
        _semana = request.form['semana'] 
        _lote_id = request.form['lote_id'] 
        _idcerdo = request.form['idcerdo'] 
        
        dato = Alimento.Registrar_toda_alimentacion(_alimento_id, _tipo_id, _fecha_c, _cantidad_kg, _observacion, _semana, _id, _lote_id, _idcerdo)
        return str(dato)
    
@alimento.route('/registrar_toda_alimentacion_full', methods=['POST'])
def registrar_toda_alimentacion_full():
    if request.method == 'POST':

        _id = session['id_usu']
        _alimento_id = request.form['alimento_id']
        _tipo_id = request.form['tipo_id']
        _fecha_c = request.form['fecha_c']
        _cantidad_kg = request.form['cantidad_kg']
        _observacion = request.form['observacion'] 
        _semana = request.form['semana'] 
        _lote_id = request.form['lote_id'] 
        _id_c = request.form['id_c'] 
        
        id_cerdo = _id_c.split(",") 
        
        for valor in zip(id_cerdo):
            dato = Alimento.Registrar_toda_alimentacion(_alimento_id, _tipo_id, _fecha_c, _cantidad_kg, _observacion, _semana, _id, _lote_id, valor[0])
        return jsonify(dato)

@alimento.route('/guardar_detalle_alimentacion_todo', methods=['POST'])
def guardar_detalle_alimentacion_todo():
    if request.method == 'POST':

        _id = request.form['id']
        _id_c = request.form['id_c']  

        id_c = _id_c.split(",") 

        for valor in zip(id_c):
            dato = Alimento.Guardar_detalle_alimentacion_todo(_id, valor[0])  
        return jsonify(dato)

# controlador para registra el detalle de alimentacion del cerdo
@alimento.route('/guardar_detalle_alimentacion_uni', methods=['POST'])
def guardar_detalle_alimentacion_uni():
    if request.method == 'POST':

        _id = request.form['id']
        _idcerdo = request.form['idcerdo']  

        dato = Alimento.Guardar_detalle_alimentacion_todo(_id, _idcerdo)  
        return jsonify(dato)

# controlador para traer los datos del pessaje del cerdo
@alimento.route('/listar_aliento_cerdo', methods=['POST'])
def listar_aliento_cerdo():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Listar_aliento_cerdo(_id)  
        return jsonify(dato)

@alimento.route('/listar_aliento_cerdo_seguimineto', methods=['POST'])
def listar_aliento_cerdo_seguimineto():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Listar_aliento_cerdo_seguimiento(_id)  
        return jsonify(dato)
    
@alimento.route('/listar_pesaje_cerdo', methods=['POST'])
def listar_pesaje_cerdo():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Listar_pesaje_cerdo(_id)  
        return jsonify(dato)
    
@alimento.route('/listar_pesaje_cerdo_seguimiento', methods=['POST'])
def listar_pesaje_cerdo_seguimiento():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Listar_pesaje_cerdo_seguimeinto(_id)  
        return jsonify(dato)
    
@alimento.route('/select_vacuna_lote_all', methods=['POST'])
def select_vacuna_lote_all():
    if request.method == 'POST':
        id = request.form['id']
        dato = Alimento.Select_vacuna_lote_all(id)         
        return jsonify(dato)

@alimento.route('/select_desparasitante_lote_all', methods=['POST'])
def select_desparasitante_lote_all():
    if request.method == 'POST':
        id = request.form['id']
        dato = Alimento.Select_desparasitante_lote_all(id)         
        return jsonify(dato)
    
@alimento.route('/traer_cantidad_dosis_lote', methods=['POST'])
def traer_cantidad_dosis_lote():
    if request.method == 'POST':
        id = request.form['id']
        dato = Alimento.Traer_cantidad_dosis_lote(id)         
        return jsonify(dato)

@alimento.route('/traer_cantidad_desparasitante_lote', methods=['POST'])
def traer_cantidad_desparasitante_lote():
    if request.method == 'POST':
        id = request.form['id']
        dato = Alimento.Traer_cantidad_desparasitante_lote(id)         
        return jsonify(dato)

@alimento.route('/guardar_vacunasaa_cerdoo', methods=['POST'])
def guardar_vacunasaa_cerdoo():
    if request.method == 'POST':
        
        _id_v = request.form['id_vacuna']
        _id_l = request.form['id_lote']
        _cantidad = request.form['cantidad']
        _semana = request.form['semana'] 
        _id_c = request.form['id_c'] 
        
        dato = Alimento.Guardar_vacunasaa_cerdoo(_id_v, _id_l, _cantidad, _semana, _id_c)
        return str(dato)

@alimento.route('/listar_vacunasa_cerdo', methods=['POST'])
def listar_vacunasa_cerdo():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Listar_vacunasa_cerdo(_id)  
        return jsonify(dato)
    
@alimento.route('/listar_vacunasa_cerdo_seguimineto', methods=['POST'])
def listar_vacunasa_cerdo_seguimineto():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Listar_vacunasa_cerdo_seguimineto(_id)  
        return jsonify(dato)
    
@alimento.route('/ver_cerdos_muertos_galpon', methods=['POST'])
def ver_cerdos_muertos_galpon():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Ver_cerdos_muertos_galpon(_id)  
        return jsonify(dato)
   
# controlador para registra las vacunas de todo los cerdos
@alimento.route('/guardar_vacunasaa_cerdoo_todo', methods=['POST'])
def guardar_vacunasaa_cerdoo_todo():
    if request.method == 'POST':

        id_vacuna = request.form['id_vacuna']
        id_lote = request.form['id_lote']
        cantidad = request.form['cantidad']  
        semana = request.form['semana']
        _idc = request.form['id_c']   

        id_cerdo = _idc.split(",") 

        for valor in zip(id_cerdo):
            dato = Alimento.Guardar_vacunasaa_cerdoo(id_vacuna, id_lote, cantidad, semana, valor[0])  
        return jsonify(dato)

@alimento.route('/guardar_muerte_cerdo', methods=['POST'])
def guardar_muerte_cerdo():
    if request.method == 'POST':
        id_cerdo = request.form['id_cerdo']
        ig_galpon = request.form['ig_galpon']
        fecha = request.form['fecha']
        hora = request.form['hora'] 
        motivo_muerte = request.form['motivo_muerte'] 
        semana = request.form['semana'] 
        dato = Alimento.Guardar_muerte_cerdo(id_cerdo, ig_galpon, fecha, hora, motivo_muerte, semana)
        return str(dato)

@alimento.route('/guardar_desparasitantee_cerdoo', methods=['POST'])
def guardar_desparasitantee_cerdoo():
    if request.method == 'POST':
        
        _id_d = request.form['id_desparasitante']
        _id_l = request.form['id_lote']
        _cantidad = request.form['cantidad']
        _semana = request.form['semana'] 
        _id_c = request.form['id_c'] 
        
        dato = Alimento.Guardar_desparasitantee_cerdoo(_id_d, _id_l, _cantidad, _semana, _id_c)
        return str(dato)

@alimento.route('/guardar_desparasitantee_cerdoo_todo', methods=['POST'])
def guardar_desparasitantee_cerdoo_todo():
    if request.method == 'POST':

        _id_d = request.form['id_desparasitante']
        _id_l = request.form['id_lote']
        _cantidad = request.form['cantidad']
        _semana = request.form['semana'] 
        _id_c = request.form['id_c'] 
        
        id_cerdo = _id_c.split(",") 
        
        for valor in zip(id_cerdo):
            dato = Alimento.Guardar_desparasitantee_cerdoo(_id_d, _id_l, _cantidad, _semana, valor[0]) 
        return jsonify(dato)

@alimento.route('/listar_desparasitantess_cerdo', methods=['POST'])
def listar_desparasitantess_cerdo():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Listar_desparasitantess_cerdo(_id)  
        return jsonify(dato)
    
@alimento.route('/listar_desparasitantess_cerdo_seguimiento', methods=['POST'])
def listar_desparasitantess_cerdo_seguimiento():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Alimento.Listar_desparasitantess_cerdo_seguimiento(_id)  
        return jsonify(dato)

@alimento.route('/listar_medicamento_lote_tratamiento', methods=['GET'])
def listar_medicamento_lote_tratamiento():
    if request.method == 'GET':
        dato = Alimento.Listar_medicamento_lote_tratamiento()
        return jsonify(dato)

@alimento.route('/listar_insumo_lote_tratamiento', methods=['GET'])
def listar_insumo_lote_tratamiento():
    if request.method == 'GET':
        dato = Alimento.Listar_insumo_lote_tratamiento()
        return jsonify(dato)

@alimento.route('/traer_cantidad_dosis_lote_disponibles', methods=['POST'])
def traer_cantidad_dosis_lote_disponibles():
    if request.method == 'POST':        
        id = request.form['id'] 
        dato = Alimento.Traer_cantidad_dosis_lote_disponibles(id)
        return jsonify(dato)
   