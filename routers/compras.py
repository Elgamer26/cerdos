from flask import Blueprint, request, session
from flask import jsonify
from models.compras import Compras
from os import getcwd, path, remove
import time

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
compras = Blueprint('compras', __name__)
# para mover la imagen
PATH_FILE = getcwd() + "/static/uploads/insumo/"
PATH_MEDICA = getcwd() + "/static/uploads/medicamento/"

# controlador para regitra el proveedor
@compras.route('/registrar_proveedor', methods=['POST'])
def registrar_proveedor():
    if request.method == 'POST':
        _razon_social = request.form['razon_social']
        _ruc = request.form['ruc']
        _telefonoo = request.form['telefonoo']
        _correo = request.form['correo']
        _direccion = request.form['direccion']
        _descripcion = request.form['descripcion']
        _encargdo = request.form['encargdo']
        _telefonoo_en = request.form['telefonoo_en']  

        dato = Compras.Registrar_proveedor(_razon_social, _ruc, _telefonoo, _correo, _descripcion, _encargdo, _telefonoo_en, _direccion)
        return str(dato)

# controlador para listar el proveedor
@compras.route('/listado_proveedores', methods=['GET'])
def listado_proveedores():
    if request.method == 'GET':
        dato = Compras.Listado_proveedores()
        return jsonify(dato)

# controlador para estado del proveedor
@compras.route('/estado_proveedor', methods=['POST'])
def estado_proveedor():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Compras.Estado_proveedor(_id, _dato)
        return str(dato)

# controlador para editar el proveedor
@compras.route('/editar_proveedor', methods=['POST'])
def editar_proveedor():
    if request.method == 'POST':
        _id = request.form['id']
        _razon_social = request.form['razon_social']
        _ruc = request.form['ruc']
        _telefonoo = request.form['telefonoo']
        _correo = request.form['correo']
        _direccion = request.form['direccion']
        _descripcion = request.form['descripcion']
        _encargdo = request.form['encargdo']
        _telefonoo_en = request.form['telefonoo_en']  

        dato = Compras.Editar_proveedor(_razon_social, _ruc, _telefonoo, _correo, _descripcion, _encargdo, _telefonoo_en, _direccion, _id)
        return str(dato)

# controlador para registrar la compra
@compras.route('/registrar_compra_alimento', methods=['POST'])
def registrar_compra_alimento():
    if request.method == 'POST':
        _id = session['id_usu']
        _id_pro = request.form['proveedor']
        _fecha_c = request.form['fecha_c']
        _numero_compra = request.form['numero_compra']
        _tipo_comprobante = request.form['tipo_comprobante']
        _iva = request.form['iva']
        _subtotal = request.form['subtotal']
        _impuesto_sub = request.form['impuesto_sub']
        _total_pagar = request.form['total_pagar'] 

        dato = Compras.Registrar_compra_alimento(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id)
        return str(dato)

# controlador para registra el detalle de compra del alimento
@compras.route('/registrar_detalle_compra_alimento', methods=['POST'])
def registrar_detalle_compra_alimento():
    if request.method == 'POST':

        _id = request.form['id']
        _ida = request.form['ida']
        _precio = request.form['precio']
        _cantidad = request.form['cantidad'] 
        _descuento = request.form['descuento'] 
        _total = request.form['total'] 
        _fecha_i = request.form['fecha_i'] 
        _fecha_f = request.form['fecha_f'] 
        _caodigo = request.form['caodigo'] 
        _peso = request.form['peso'] 

        ida = _ida.split(",")
        precio = _precio.split(",")
        cantidad = _cantidad.split(",") 
        descuento = _descuento.split(",")
        total = _total.split(",") 
        fecha_i = _fecha_i.split(",") 
        fecha_f = _fecha_f.split(",")
        caodigo = _caodigo.split(",") 
        peso = _peso.split(",") 

        for valor in zip(ida, precio, cantidad, descuento, total, fecha_i, fecha_f, caodigo, peso):
            dato = Compras.Registrar_detalle_compra_alimento(_id, valor[0], valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], valor[7], valor[8])  
        return jsonify(dato)

# controlador para anular la compra de alimentos
@compras.route('/compra_alimneto_anular', methods=['POST'])
def compra_alimneto_anular():    
    if request.method == 'POST':
        _id = request.form['id']   
        dato = Compras.Anular_compra_alimentos(_id)   
        return str(dato)
    
# controlador para acciones de crear y editar el tipo de insumo
@compras.route('/accion_tipo_insumo', methods=['POST'])
def accion_tipo_insumo():
    if request.method == 'POST':
        
        funcion = request.form['funcion']
        if funcion == 'registra_tipo_insumo':       
            _valor = request.form['valor']
            dato = Compras.Registrartipo_insumo(_valor)
            return jsonify(dato)

        elif funcion == 'editar_tipo_insumo':  
            _id = request.form['id']     
            _dato = request.form['valor']
            dato = Compras.Editar_tipo_insumo(_id,_dato)
            return jsonify(dato)

        elif funcion == 'estado_tipo_insumo':   
            _id = request.form['id']    
            _valor = request.form['dato']
            dato = Compras.Estado_tipo_insumo(_id,_valor)
            return jsonify(dato)

# controlador para listar el tipo de insumo
@compras.route('/listar_tipo_insumo', methods=['GET'])
def listar_tipo_insumo():
    if request.method == 'GET':
        dato = Compras.Listar_tipo_insumo()
        return jsonify(dato)

# controlador para crear el insumo
@compras.route('/registrar_insumo', methods=['POST'])
def registrar_insumo():
    if request.method == 'POST':
        _codigo = request.form['codigo']
        _nombre = request.form['nombre']
        _tipo = request.form['tipo'] 
        _cantidad = request.form['cantidad']
        _precio = request.form['precio'] 
        _detalle = request.form['detalle']
        _presentacion = request.form['presentacion']
        _foto = request.files.get("foto", False)

        if _foto:
            # cerdo con foto
            hora_ac = time.strftime('%Y%m%d%H%M%S_', time.localtime())
            archivo = hora_ac + _foto.filename             
            dato = Compras.Crear_insumo(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, archivo, _presentacion)
            if dato == 1:
                _foto.save(PATH_FILE + archivo)
                return str(dato)
            else:
                return str(dato)        
        else:
            # cerdo sin foto
            archivo = "insumo.jpg"
            dato = Compras.Crear_insumo(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, archivo, _presentacion)
            return str(dato)

# controlador para listar el insumo
@compras.route('/listar_insumos', methods=['GET'])
def listar_insumos():
    if request.method == 'GET':
        dato = Compras.Listar_insumos()
        return jsonify(dato)

# controlador para cambiar el estado del insumo
@compras.route('/estado_insumo', methods=['POST'])
def estado_insumo():
    if request.method == 'POST':   
        _id = request.form['id']    
        _dato = request.form['dato']
        dato = Compras.Estado_insumo(_id,_dato)
        return jsonify(dato)

# controlador para editar el insumo
@compras.route('/editar_insumo', methods=['POST'])
def editar_insumo():
    if request.method == 'POST':
        id = request.form['id']
        _codigo = request.form['codigo']
        _nombre = request.form['nombre']
        _tipo = request.form['tipo'] 
        _cantidad = request.form['cantidad']
        _precio = request.form['precio'] 
        presentacion = request.form['presentacion'] 
        _detalle = request.form['detalle'] 

        dato = Compras.Editar_insumo(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, id, presentacion)
        return str(dato)

# controlador para cambiar la foto del insumo
@compras.route('/cambiar_foto_insumo', methods=['POST'])
def cambiar_foto_insumo():
    if request.method == 'POST':
        try:
            _id = request.form['id']
            foto_ac = request.form['ruta_actual']
            file = request.files.get("foto", False)

            hora_ac = time.strftime('%Y%m%d%H%M%S', time.localtime())
            archivo = hora_ac + file.filename

            data = Compras.Cambiar_foto_insumo(_id, archivo)

            if data == 1:
                file.save(PATH_FILE + archivo)
                # para no eliminar la foto por defecto
                if foto_ac != "insumo.jpg":
                    # esto es paar saber si el archivo existe y elimiarlo
                    if path.isfile(PATH_FILE + foto_ac) == True:
                        remove(PATH_FILE + foto_ac)
                
                return str(data)
            else:
                return str(data)
        except Exception as e:
            error = "Error " + str(e)
            return error

# controlador para registrar la compra del insumo
@compras.route('/registrar_compra_insumo', methods=['POST'])
def registrar_compra_insumo():
    if request.method == 'POST':
        _id = session['id_usu']
        _id_pro = request.form['proveedor']
        _fecha_c = request.form['fecha_c']
        _numero_compra = request.form['numero_compra']
        _tipo_comprobante = request.form['tipo_comprobante']
        _iva = request.form['iva']
        _subtotal = request.form['subtotal']
        _impuesto_sub = request.form['impuesto_sub']
        _total_pagar = request.form['total_pagar'] 

        dato = Compras.Registrar_compra_insumo(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id)
        return str(dato)

# controlador para registra el detalle de compra del insumo
@compras.route('/registrar_detalle_compra_insumo', methods=['POST'])
def registrar_detalle_compra_insumo():
    if request.method == 'POST':

        _id = request.form['id']
        _ida = request.form['ida']
        _precio = request.form['precio']
        _cantidad = request.form['cantidad'] 
        _descuento = request.form['descuento'] 
        _total = request.form['total'] 
        
        _unidad = request.form['unidad']
        _fecha_ini = request.form['fecha_ini']
        _fecha_fin = request.form['fecha_fin'] 
        _codigo = request.form['codigo'] 
        _total_unidad = request.form['total_unidad'] 

        ida = _ida.split(",")
        precio = _precio.split(",")
        cantidad = _cantidad.split(",") 
        descuento = _descuento.split(",")
        total = _total.split(",") 
        unidad = _unidad.split(",")
        fecha_ini = _fecha_ini.split(",") 
        fecha_fin = _fecha_fin.split(",")
        codigo = _codigo.split(",") 
        total_unidad = _total_unidad.split(",") 

        for valor in zip(ida, precio, cantidad, descuento, total, unidad, fecha_ini, fecha_fin, codigo, total_unidad):
            dato = Compras.Registrar_detalle_compra_insumo(_id, valor[0], valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], valor[7], valor[8], valor[9])  
        return jsonify(dato)

# controlador para anular la compra de insumo
@compras.route('/compra_insumo_anular', methods=['POST'])
def compra_insumo_anular():    
    if request.method == 'POST':
        _id = request.form['id']   
        dato = Compras.Compra_insumo_anular(_id)   
        return str(dato)

# controlador para acciones de crear y editar el tipo de medicamento
@compras.route('/accion_tipo_medicamento', methods=['POST'])
def accion_tipo_medicamento():
    if request.method == 'POST':
        
        funcion = request.form['funcion']
        if funcion == 'registra_tipo_medicamento':       
            _valor = request.form['valor']
            dato = Compras.Registrar_tipo_medicamento(_valor)
            return jsonify(dato)

        elif funcion == 'editar_tipo_medicamento':  
            _id = request.form['id']     
            _dato = request.form['valor']
            dato = Compras.Editar_tipo_medicamento(_id,_dato)
            return jsonify(dato)

        elif funcion == 'estado_tipo_medicamento':   
            _id = request.form['id']    
            _valor = request.form['dato']
            dato = Compras.Estado_tipo_medicamento(_id,_valor)
            return jsonify(dato)

# controlador para listar el tipo de medicamento
@compras.route('/listar_tipo_medicamento', methods=['GET'])
def listar_tipo_medicamento():
    if request.method == 'GET':
        dato = Compras.Listar_tipo_medicamento()
        return jsonify(dato)

# controlador para crear el medicamento
@compras.route('/registrar_medicamento', methods=['POST'])
def registrar_medicamento():
    if request.method == 'POST':
        _codigo = request.form['codigo']
        _nombre = request.form['nombre']
        _tipo = request.form['tipo'] 
        _cantidad = request.form['cantidad']
        _precio = request.form['precio'] 
        _detalle = request.form['detalle']
        _presentacion= request.form['presentacion'] 
        _cantidad_unidad = request.form['cantidad_unidad']
        _foto = request.files.get("foto", False)

        if _foto:
            # cerdo con foto
            hora_ac = time.strftime('%Y%m%d%H%M%S_', time.localtime())
            archivo = hora_ac + _foto.filename             
            dato = Compras.Crear_medicamento(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, archivo, _presentacion, _cantidad_unidad)
            if dato == 1:
                _foto.save(PATH_MEDICA + archivo)
                return str(dato)
            else:
                return str(dato)        
        else:
            # cerdo sin foto
            archivo = "medicamento.jpg"
            dato = Compras.Crear_medicamento(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, archivo, _presentacion, _cantidad_unidad)
            return str(dato)

# controlador para listar el insumo
@compras.route('/listar_medicamento', methods=['GET'])
def listar_medicamento():
    if request.method == 'GET':
        dato = Compras.Listar_medicamento()
        return jsonify(dato)

@compras.route('/listar_lote_medicmaneto', methods=['GET'])
def listar_lote_medicmaneto():
    if request.method == 'GET':
        dato = Compras.Listar_lote_medicmaneto()
        return jsonify(dato)
    
@compras.route('/listar_lote_insumos', methods=['GET'])
def listar_lote_insumos():
    if request.method == 'GET':
        dato = Compras.Listar_lote_insumos()
        return jsonify(dato)
    

@compras.route('/eliminar_lote_medicamento', methods=['POST'])
def eliminar_lote_medicamento():
    if request.method == 'POST':   
        _id = request.form['id']     
        dato = Compras.Eliminar_lote_medicamento(_id)
        return jsonify(dato)
    
@compras.route('/eliminar_lote_insumos', methods=['POST'])
def eliminar_lote_insumos():
    if request.method == 'POST':   
        _id = request.form['id']     
        dato = Compras.Eliminar_lote_insumos(_id)
        return jsonify(dato)
    

# controlador para cambiar el estado del medicamento
@compras.route('/estado_medicamento', methods=['POST'])
def estado_medicamento():
    if request.method == 'POST':   
        _id = request.form['id']    
        _dato = request.form['dato']
        dato = Compras.Estado_medicamento(_id,_dato)
        return jsonify(dato)

# controlador para editar el insumo
@compras.route('/editar_medicamento', methods=['POST'])
def editar_medicamento():
    if request.method == 'POST':
        id = request.form['id']
        _codigo = request.form['codigo']
        _nombre = request.form['nombre']
        _tipo = request.form['tipo'] 
        _cantidad = request.form['cantidad']
        _precio = request.form['precio'] 
        _detalle = request.form['detalle'] 
        _presentacion= request.form['presentacion'] 
        _cantidad_unidad = request.form['unidades']

        dato = Compras.Editar_medicamento(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, id, _presentacion, _cantidad_unidad)
        return str(dato)

# controlador para registrar la compra del medicamento
@compras.route('/registrar_compra_medicamentoo', methods=['POST'])
def registrar_compra_medicamentoo():
    if request.method == 'POST':
        _id = session['id_usu']
        _id_pro = request.form['proveedor']
        _fecha_c = request.form['fecha_c']
        _numero_compra = request.form['numero_compra']
        _tipo_comprobante = request.form['tipo_comprobante']
        _iva = request.form['iva']
        _subtotal = request.form['subtotal']
        _impuesto_sub = request.form['impuesto_sub']
        _total_pagar = request.form['total_pagar'] 

        dato = Compras.Registrar_compra_medicamentoo(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id)
        return str(dato)

# controlador para registra el detalle de compra del medicamento
@compras.route('/registrar_detalle_compra_medicamento', methods=['POST'])
def registrar_detalle_compra_medicamento():
    if request.method == 'POST':

        _id = request.form['id']
        _ida = request.form['ida']
        _precio = request.form['precio']
        _cantidad = request.form['cantidad'] 
        _descuento = request.form['descuento'] 
        _total = request.form['total'] 
        
        _unidades = request.form['unidades'] 
        _total_unidades = request.form['total_unidades'] 
        _fecha_i = request.form['fecha_i'] 
        _fecha_f = request.form['fecha_f'] 
        _codigo = request.form['codigo'] 
        
        ida = _ida.split(",")
        precio = _precio.split(",")
        cantidad = _cantidad.split(",") 
        descuento = _descuento.split(",")
        total = _total.split(",") 
        
        unidades = _unidades.split(",")
        total_unidades = _total_unidades.split(",") 
        fecha_i = _fecha_i.split(",")
        fecha_f = _fecha_f.split(",") 
        codigo = _codigo.split(",") 

        for valor in zip(ida, precio, cantidad, descuento, total, unidades, total_unidades, fecha_i, fecha_f, codigo):
            dato = Compras.Registrar_detalle_compra_medicamento(_id, valor[0], valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], valor[7], valor[8], valor[9])  
        return jsonify(dato)

# controlador para anular la compra de medicamento
@compras.route('/compra_medicamento_anular', methods=['POST'])
def compra_medicamento_anular():    
    if request.method == 'POST':
        _id = request.form['id']   
        dato = Compras.Compra_medicamento_anular(_id)   
        return str(dato)

# controlador para cambiar la foto del medicamento
@compras.route('/cambiar_foto_medicamento', methods=['POST'])
def cambiar_foto_medicamento():
    if request.method == 'POST':
        try:
            _id = request.form['id']
            foto_ac = request.form['ruta_actual']
            file = request.files.get("foto", False)

            hora_ac = time.strftime('%Y%m%d%H%M%S', time.localtime())
            archivo = hora_ac + file.filename

            data = Compras.Cambiar_foto_medicamento(_id, archivo)

            if data == 1:
                file.save(PATH_MEDICA + archivo)
                # para no eliminar la foto por defecto
                if foto_ac != "medicamento.jpg":
                    # esto es paar saber si el archivo existe y elimiarlo
                    if path.isfile(PATH_MEDICA + foto_ac) == True:
                        remove(PATH_MEDICA + foto_ac)
                
                return str(data)
            else:
                return str(data)
        except Exception as e:
            error = "Error " + str(e)
            return error

# controlador para registrar la compra de la vacuna
@compras.route('/registrar_compra_vacuna', methods=['POST'])
def registrar_compra_vacuna():
    if request.method == 'POST':
        _id = session['id_usu']
        _id_pro = request.form['proveedor']
        _fecha_c = request.form['fecha_c']
        _numero_compra = request.form['numero_compra']
        _tipo_comprobante = request.form['tipo_comprobante']
        _iva = request.form['iva']
        _subtotal = request.form['subtotal']
        _impuesto_sub = request.form['impuesto_sub']
        _total_pagar = request.form['total_pagar'] 

        dato = Compras.Registrar_compra_vacuna(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id)
        return str(dato)

# controlador para registra el detalle de compra de vacunas
@compras.route('/registrar_detalle_compra_vacuna', methods=['POST'])
def registrar_detalle_compra_vacuna():
    if request.method == 'POST':

        _id = request.form['id']
        _ida = request.form['ida']
        _precio = request.form['precio']
        _cantidad = request.form['cantidad'] 
        _descuento = request.form['descuento'] 
        _total = request.form['total'] 
        
        _fecha_i = request.form['fecha_i'] 
        _fecha_f = request.form['fecha_f'] 
        _codigo = request.form['codigo'] 
        _dosis = request.form['dosis'] 

        ida = _ida.split(",")
        precio = _precio.split(",")
        cantidad = _cantidad.split(",") 
        descuento = _descuento.split(",")
        total = _total.split(",")         
        fecha_i = _fecha_i.split(",") 
        fecha_f = _fecha_f.split(",")
        codigo = _codigo.split(",") 
        dosis = _dosis.split(",") 

        for valor in zip(ida, precio, cantidad, descuento, total, fecha_i, fecha_f, codigo, dosis):
            dato = Compras.Registrar_detalle_compra_vacuna(_id, valor[0], valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], valor[7], valor[8])  
        return jsonify(dato)

# controlador para anular la compra de vacuna
@compras.route('/compra_vacuna_anular', methods=['POST'])
def compra_vacuna_anular():    
    if request.method == 'POST':
        _id = request.form['id']   
        dato = Compras.Compra_vacuna_anular(_id)   
        return str(dato)