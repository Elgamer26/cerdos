from flask import Blueprint, render_template, request, redirect, url_for
from os import getcwd, path, remove
from flask import jsonify, session
from models.cerdo import Cerdo
import time

import pandas as pd
#openpyxl

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
cerdo = Blueprint('cerdo', __name__)
# para mover la imagen
PATH_FILE = getcwd() + "/static/uploads/cerdo/"
PATH_EXCEL = getcwd() + "/static/uploads/cerdo_exel/"

# controlador para crear una nueva raza
@cerdo.route('/crear_raza', methods=['POST'])
def crear_raza():
    if request.method == 'POST':
        _raza = request.form['raza']
        dato = Cerdo.Crear_raza(_raza)
        return jsonify(dato)

# controlador para listar raza cerdo
@cerdo.route('/listar_cerdo', methods=['GET'])
def listar_cerdo():
    if request.method == 'GET':
        dato = Cerdo.Listar_cerdo()
        return jsonify(dato)

# controlador para estado de la raza cerdo
@cerdo.route('/estado_raza', methods=['POST'])
def estado_raza():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Cerdo.Estado_raza(_id, _dato)
        return str(dato)

# controlador para editar raza cerdo
@cerdo.route('/editar_cerdo', methods=['POST'])
def editar_cerdo():
    if request.method == 'POST':
        _raza = request.form['raza']
        _id = request.form['id']
        dato = Cerdo.Editar_cerdo(_raza, _id)
        return jsonify(dato)

# controlador para crear un cerdo
@cerdo.route('/crear_cerdo', methods=['POST'])
def crear_cerdo():
    if request.method == 'POST':
        _codigo_cerdo = request.form['codigo_cerdo']
        _nombre = request.form['nombre']
        _sexo_cerdo = request.form['sexo_cerdo']
        _raza_id = request.form['raza_id']
        _peso = request.form['peso']
        _origen = request.form['origen']
        _fecha = request.form['fecha']
        _detalle_c = request.form['detalle_c']
        
        _tipo_ingreso = request.form['tipo_ingreso']
        _costo = request.form['costo']
        _etapa = request.form['etapa']
        
        _foto = request.files.get("foto", False)

        if _foto:
            # cerdo con foto
            hora_ac = time.strftime('%Y%m%d%H%M%S_', time.localtime())
            archivo = hora_ac + _foto.filename             
            dato = Cerdo.Crear_cerdo(_codigo_cerdo, _nombre, _sexo_cerdo, _raza_id, _peso, _origen, _fecha, _detalle_c, archivo, _tipo_ingreso, _costo, _etapa)
            if dato == 1:
                _foto.save(PATH_FILE + archivo)
                return str(dato)
            else:
                return str(dato)        
        else:
            # cerdo sin foto
            archivo = "cerdo.jpg"
            dato = Cerdo.Crear_cerdo(_codigo_cerdo, _nombre, _sexo_cerdo, _raza_id, _peso, _origen, _fecha, _detalle_c, archivo, _tipo_ingreso, _costo, _etapa)
            return str(dato)

# controlador para listar el cerdo
@cerdo.route('/listado_cerdos', methods=['GET'])
def listado_cerdos():
    if request.method == 'GET':
        dato = Cerdo.Listado_cerdos()
        return jsonify(dato)

# controlador para estado del cerdo
@cerdo.route('/estado_cerdo', methods=['POST'])
def estado_cerdo():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Cerdo.Estado_cerdo(_id, _dato)
        return str(dato)

# para editar la foto del cerdo
@cerdo.route('/cambiar_foto_cerdo', methods=['POST'])
def cambiar_foto_cerdo():
    if request.method == 'POST':
        try:
            _id = request.form['id']
            foto_ac = request.form['ruta_actual']
            file = request.files.get("foto", False)

            hora_ac = time.strftime('%Y%m%d%H%M%S', time.localtime())
            archivo = hora_ac + file.filename

            data = Cerdo.Cambiar_foto_cerdo(_id, archivo)

            if data == 1:
                file.save(PATH_FILE + archivo)
                # para no eliminar la foto por defecto
                if foto_ac != "cerdo.jpg":
                    # esto es paar saber si el archivo existe y elimiarlo
                    if path.isfile(PATH_FILE + foto_ac) == True:
                        remove(PATH_FILE + foto_ac)
                
                return str(data)
            else:
                return str(data)
        except Exception as e:
            error = "Error " + str(e)
            return error

# controlador para editar un cerdo
@cerdo.route('/editar_cerdo_chancho', methods=['POST'])
def editar_cerdo_chancho():
    if request.method == 'POST':
        _id = request.form['id']
        _codigo_cerdo = request.form['codigo_cerdo']
        _nombre = request.form['nombre']
        _sexo_cerdo = request.form['sexo_cerdo']
        _raza_id = request.form['raza_id']
        _peso = request.form['peso']
        _origen = request.form['origen']
        _fecha = request.form['fecha']
        _detalle_c = request.form['detalle_c']
        
        _tipo_ingreso = request.form['tipo_ingreso']
        _costo = request.form['costo']
        _etapa = request.form['etapa']

        dato = Cerdo.Editar_cerdo_chancho(_codigo_cerdo, _nombre, _sexo_cerdo, _raza_id, _peso, _origen, _fecha, _detalle_c, _tipo_ingreso, _costo, _etapa, _id)
        return str(dato)

# controlador para registra el cerdo muerto
@cerdo.route('/registrar_muerte_cerdo', methods=['POST'])
def registrar_muerte_cerdo():
    if request.method == 'POST':
        _cerdo = request.form['cerdo']
        _fecha= request.form['fecha']
        _detalle = request.form['detalle']

        dato = Cerdo.Registrar_muerte_cerdo(_cerdo, _fecha, _detalle)
        return str(dato)

# controlador para eliminar  el cerdo muerto
@cerdo.route('/eliminar_cerdo_muerto', methods=['POST'])
def eliminar_cerdo_muerto():
    if request.method == 'POST':
        _id = request.form['id'] 

        dato = Cerdo.Eliminar_cerdo_muerto(_id)
        return str(dato)
    
# controlador para obterne los valores del cerdos para la tienda
@cerdo.route('/ver_detalle_cerdo', methods=['POST'])
def ver_detalle_cerdo():
    if request.method == 'POST':
        _id = request.form['id'] 
        dato = Cerdo.Ver_detalle_cerdo(_id)
        return jsonify(dato)
    
# para caargra archivos excel al sistema
@cerdo.route('/cargar_archivos', methods=['POST'])
def cargar_archivos():
    if request.method == 'POST':
        try:
            file = request.files.get("archivo", False)           
            file.save(PATH_EXCEL + file.filename) 
                      
            df = pd.read_excel(PATH_EXCEL + file.filename, sheet_name='cerdos', header=None, names=['Código','Nombre o Alias','Sexo','Raza','Foto','Peso (Kg)','Origen','Fecha','Detalle del cerdo','Tipo de ingreso','Costo','Etapa/Fase'])
            columna = df[3:].shape
            if str(columna[1]) == "12":
                data = df[3:].values
                for i in data:
                    result = Cerdo.Crear_cerdo_carga(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
                remove(PATH_EXCEL + file.filename)                
                return str(result)
            else:
                remove(PATH_EXCEL + file.filename)
                return str(2)
            
            # df.set_index('Costo', inplace=True)
            # conteo = len(df.index)
            
            # for i in range(conteo):
            #     componente = df.index[i][0]
            #     print(componente) 
                           
        except Exception as e:
            remove(PATH_EXCEL + file.filename)
            error = "Error: " + str(e)
            return error
