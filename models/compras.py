from utils.db import mysql
from datetime import datetime

class Compras():
    # modelo para registrar el proveedor
    def Registrar_proveedor(_razon_social, _ruc, _telefonoo, _correo, _descripcion, _encargdo, _telefonoo_en, _direccion):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM proveedor WHERE ruc = "{0}"'. format(_ruc))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO proveedor (razon,ruc,telefono,correo,descripcion,encargado,telefono_en,direccion) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}")'.format(_razon_social,_ruc,_telefonoo,_correo,_descripcion,_encargdo,_telefonoo_en,_direccion))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo de listar el proveedor
    def Listado_proveedores():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM proveedor')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["razon"] = datos[1]
                dic["ruc"] = datos[2] 
                dic["telefono"] = datos[3]
                dic["correo"] = datos[4]
                dic["descripcion"] = datos[5] 
                dic["encargado"] = datos[6]
                dic["telefono_en"] = datos[7]
                dic["direccion"] = datos[8] 
                dic["estado"] = datos[9]       
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado del proveedor
    def Estado_proveedor(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE proveedor SET estado = "{0}" WHERE id = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el proveedor
    def Editar_proveedor(_razon_social, _ruc, _telefonoo, _correo, _descripcion, _encargdo, _telefonoo_en, _direccion, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM proveedor WHERE ruc="{0}" AND id != "{1}"'. format(_ruc, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE proveedor SET razon="{0}",ruc="{1}",telefono="{2}",correo="{3}",descripcion="{4}",encargado="{5}",telefono_en="{6}",direccion="{7}" WHERE id="{8}"'.format(_razon_social,_ruc,_telefonoo,_correo,_descripcion,_encargdo,_telefonoo_en,_direccion,_id))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo del select del proveedor
    def Select_proveedor():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM proveedor WHERE estado = 1')
            data = query.fetchall()
            query.close()             
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listar los alimentos para la compra
    def Table_alimentos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            alimento.id,
                            alimento.codigo,
                            alimento.nombre, 
                            alimento.cantidad,
                            alimento.precio,
                            alimento.peso, 
                            alimento.foto, 
                            marca_alimento.marca_alimento,
                            tipo_alimento.tipo_alimento 
                        FROM
                            alimento
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id WHERE alimento.estado = 1
                        ORDER BY
                            alimento.id DESC""")
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
   
    # controlador para registrar la compra
    def Registrar_compra_alimento(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM compra_alimento WHERE numero_compra = "{0}"'. format(_numero_compra))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO compra_alimento (usuario_id,proveedor_id,fecha,numero_compra,documento,iva,subtotal,impuesto,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(_id,_id_pro,_fecha_c,_numero_compra,_tipo_comprobante,_iva,_subtotal,_impuesto_sub,_total_pagar))
                query.connection.commit()
                # me devuelve el ultimo id insertado
                id = query.lastrowid
                query.close()
                return id  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # controlador para registra el detalle de compra del alimento
    def Registrar_detalle_compra_alimento(_id, ida, precio, cantidad, descuento, total, fecha_i, fecha_f, codigo, peso):
        try:
            query = mysql.connection.cursor()         
            query.execute('INSERT INTO detalle_compra_alimento (compra_alimento_id,alimento_id,precio,cantidad,descuento,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}")'.format(_id,ida,precio,cantidad,descuento,total))
            query.connection.commit()
            query.execute('INSERT INTO lote_alimento (alimento_id,cantidad,fecha_i,fecha_f,codigo) VALUES ("{0}","{1}","{2}","{3}","{4}")'.format(ida,peso,fecha_i,fecha_f,codigo))
            query.connection.commit()
            # query.execute('UPDATE alimento SET cantidad = cantidad + "{0}" WHERE id = "{1}" '.format(cantidad,ida))
            # query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar las compras de alimentos
    def Listar_compras_alimentos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_alimento.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon, ' - ', proveedor.ruc ) AS proveedor,
                            compra_alimento.fecha,
                            compra_alimento.numero_compra,
                            compra_alimento.documento,
                            compra_alimento.iva,
                            compra_alimento.subtotal,
                            compra_alimento.impuesto,
                            compra_alimento.total,
                            compra_alimento.estado 
                        FROM
                            compra_alimento
                            INNER JOIN usuario ON compra_alimento.usuario_id = usuario.usuario_id
                            INNER JOIN proveedor ON compra_alimento.proveedor_id = proveedor.id 
                        ORDER BY
                            compra_alimento.id DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para anular la compra de alimentos
    def Anular_compra_alimentos(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT 
                            detalle_compra_alimento.alimento_id,
                            detalle_compra_alimento.cantidad 
                            FROM
                            detalle_compra_alimento
                            WHERE
                            detalle_compra_alimento.compra_alimento_id = '{0}'""".format(_id))
            data = query.fetchall()
            
            for dato in data: 
                query.execute('UPDATE alimento SET cantidad = cantidad - {0} WHERE id = "{1}"'.format(dato[1], str(dato[0])))
                query.connection.commit()

            query.execute('UPDATE compra_alimento SET estado = 0 WHERE id = {0}'.format(_id))
            query.connection.commit()

            query.execute('UPDATE detalle_compra_alimento SET estado = 0 WHERE id = "{0}"'.format(_id))
            query.connection.commit()
            query.close() 
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para registrar el tipo de insumo
    def Registrartipo_insumo(_valor):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_insumo WHERE tipo = "{0}"'. format(_valor))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO tipo_insumo (tipo) VALUES ("{0}")'.format(_valor))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el tipo de insumo
    def Editar_tipo_insumo(_id,_dato):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_insumo WHERE tipo = "{0}" AND id != "{1}"'. format(_dato, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE tipo_insumo SET tipo = "{0}" WHERE id = "{1}"'.format(_dato, _id))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
   # modelo para cambiar el estado del insumo
    def Estado_tipo_insumo(_id,_dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE tipo_insumo SET estado = "{0}" WHERE id = "{1}"'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar el tipo de insumo
    def Listar_tipo_insumo():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_insumo ORDER BY id DESC')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["tipo"] = datos[1] 
                dic["estado"] = datos[2]       
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para combo del tipo de insumo
    def Combo_tipo_insumo():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_insumo WHERE estado = 1')
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registrar el insumo
    def Crear_insumo(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, archivo):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM insumo WHERE codigo = "{0}"'. format(_codigo))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO insumo (codigo,nombre,tipo_id,cantidad,precio,detalle,foto) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(_codigo,_nombre,_tipo,_cantidad,_precio,_detalle,archivo))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar el insumo
    def Listar_insumos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            insumo.id,
                            insumo.codigo,
                            insumo.nombre,
                            insumo.tipo_id,
                            tipo_insumo.tipo,
                            insumo.cantidad,
                            insumo.precio,
                            insumo.detalle,
                            insumo.foto,
                            insumo.estado 
                        FROM
                            insumo
                            INNER JOIN tipo_insumo ON insumo.tipo_id = tipo_insumo.id ORDER BY insumo.id DESC""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["codigo"] = datos[1]
                dic["nombre"] = datos[2] 
                dic["tipo_id"] = datos[3]
                dic["tipo"] = datos[4]
                dic["cantidad"] = datos[5] 
                dic["precio"] = datos[6]
                dic["detalle"] = datos[7]
                dic["foto"] = datos[8] 
                dic["estado"] = datos[9]       
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para cambiar el estado del insumo
    def Estado_insumo(_id,_dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE insumo SET estado = "{0}" WHERE id = "{1}"'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el insumo
    def Editar_insumo(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM insumo WHERE codigo="{0}" AND id!="{1}"'. format(_codigo,id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE insumo SET codigo="{0}",nombre="{1}",tipo_id="{2}",cantidad="{3}",precio="{4}",detalle="{5}"WHERE id = "{6}"'.format(_codigo,_nombre,_tipo,_cantidad,_precio,_detalle,id))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para cambiar la foto del insumo
    def Cambiar_foto_insumo(_id,archivo):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE insumo SET foto = "{0}" WHERE id = "{1}"'.format(archivo, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar el insumo en la tabla de compra
    def Table_insumos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            insumo.id,
                            insumo.codigo,
                            insumo.nombre,
                            insumo.tipo_id,
                            tipo_insumo.tipo,
                            insumo.cantidad,
                            insumo.precio,
                            insumo.detalle,
                            insumo.foto,
                            insumo.estado 
                            FROM
                            insumo
                            INNER JOIN tipo_insumo ON insumo.tipo_id = tipo_insumo.id WHERE insumo.estado = 1""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registrar la compra del insumo
    def Registrar_compra_insumo(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM compra_insumo WHERE numero_compra = "{0}"'. format(_numero_compra))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO compra_insumo (usuario_id,proveedor_id,fecha,numero_compra,documento,iva,subtotal,impuesto,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(_id,_id_pro,_fecha_c,_numero_compra,_tipo_comprobante,_iva,_subtotal,_impuesto_sub,_total_pagar))
                query.connection.commit()
                # me devuelve el ultimo id insertado
                id = query.lastrowid
                query.close()
                return id  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registra el detalle de compra del insumo
    def Registrar_detalle_compra_insumo(_id, ida, precio, cantidad, descuento, total, unidad, fecha_ini, fecha_fin, codigo, total_unidad):
        try:
            query = mysql.connection.cursor()         
            query.execute('INSERT INTO detalle_compra_insumo (compra_insumo_id,insumo_id,precio,cantidad,descuento,total,unidad) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(_id,ida,precio,cantidad,descuento,total,unidad))
            query.connection.commit()
            
            query.execute('INSERT INTO lote_insumo (insumo_id,cantidad,fecha_i,fecha_f,codigo) VALUES ("{0}","{1}","{2}","{3}","{4}")'.format(ida,total_unidad,fecha_ini,fecha_fin,codigo))
            query.connection.commit()
            # query.execute('UPDATE insumo SET cantidad = cantidad + "{0}" WHERE id = "{1}" '.format(cantidad,ida))
            # query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar las compras de insumo
    def Listar_compras_insumos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_insumo.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon, ' - ', proveedor.ruc ) AS proveedor,
                            compra_insumo.fecha,
                            compra_insumo.numero_compra,
                            compra_insumo.documento,
                            compra_insumo.iva,
                            compra_insumo.subtotal,
                            compra_insumo.impuesto,
                            compra_insumo.total,
                            compra_insumo.estado 
                        FROM
                            compra_insumo
                            INNER JOIN usuario ON compra_insumo.usuario_id = usuario.usuario_id
                            INNER JOIN proveedor ON compra_insumo.proveedor_id = proveedor.id 
                        ORDER BY
                            compra_insumo.id DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para anular la compra de insumo
    def Compra_insumo_anular(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        detalle_compra_insumo.insumo_id,
                        detalle_compra_insumo.cantidad 
                        FROM
                            detalle_compra_insumo 
                        WHERE
                        detalle_compra_insumo.compra_insumo_id = '{0}'""".format(_id))
            data = query.fetchall()
            
            for dato in data: 
                query.execute('UPDATE insumo SET cantidad = cantidad - {0} WHERE id = "{1}"'.format(dato[1], str(dato[0])))
                query.connection.commit()

            query.execute('UPDATE compra_insumo SET estado = 0 WHERE id = {0}'.format(_id))
            query.connection.commit()

            query.execute('UPDATE detalle_compra_insumo SET estado = 0 WHERE id = "{0}"'.format(_id))
            query.connection.commit()
            query.close() 
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para registrar el tipo de medicamento
    def Registrar_tipo_medicamento(_valor):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_medicamento WHERE tipo = "{0}"'. format(_valor))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO tipo_medicamento (tipo) VALUES ("{0}")'.format(_valor))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar el tipo medicamento
    def Listar_tipo_medicamento():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_medicamento ORDER BY id DESC')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["tipo"] = datos[1] 
                dic["estado"] = datos[2]       
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para cambiar el estado del medicamento
    def Estado_tipo_medicamento(_id,_dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE tipo_medicamento SET estado = "{0}" WHERE id = "{1}"'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el tipo de medicamento
    def Editar_tipo_medicamento(_id,_dato):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_medicamento WHERE tipo = "{0}" AND id != "{1}"'. format(_dato,_id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE tipo_medicamento SET tipo = "{0}" WHERE id = "{1}"'.format(_dato,_id))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para combo del tipo de medicamento
    def Combo_tipo_medicamento():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_medicamento WHERE estado = 1')
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registrar el medicamento
    def Crear_medicamento(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, archivo, _presentacion, _cantidad_unidad):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM medicamento WHERE codigo = "{0}"'. format(_codigo))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO medicamento (codigo,nombre,tipo_id,cantidad,precio,detalle,foto,presentacion,unidades) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(_codigo,_nombre,_tipo,_cantidad,_precio,_detalle,archivo,_presentacion,_cantidad_unidad))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar el medicamento
    def Listar_medicamento():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            medicamento.id,
                            medicamento.codigo,
                            medicamento.nombre,
                            medicamento.tipo_id,
                            tipo_medicamento.tipo,
                            medicamento.cantidad,
                            medicamento.precio,
                            medicamento.detalle,
                            medicamento.foto,
                            medicamento.estado,                            
                            medicamento.presentacion,
                            medicamento.unidades 
                        FROM
                            medicamento
                            INNER JOIN tipo_medicamento ON medicamento.tipo_id = tipo_medicamento.id ORDER BY medicamento.id DESC""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["codigo"] = datos[1]
                dic["nombre"] = datos[2] 
                dic["tipo_id"] = datos[3]
                dic["tipo"] = datos[4]
                dic["cantidad"] = datos[5] 
                dic["precio"] = datos[6]
                dic["detalle"] = datos[7]
                dic["foto"] = datos[8] 
                dic["estado"] = datos[9]   
                dic["presentacion"] = datos[10]   
                dic["unidades"] = datos[11]       
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Listar_lote_medicmaneto():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_medicamento.id,
                        CONCAT_WS( ' ', medicamento.nombre, tipo_medicamento.tipo ) AS medicamento,
                        lote_medicamento.cantidad,
                        lote_medicamento.fecha_i,
                        lote_medicamento.fecha_f,
                        lote_medicamento.codigo,
                        DATE( lote_medicamento.fecha ) AS fecha,
                        TIME( lote_medicamento.fecha ) AS hora 
                    FROM
                        tipo_medicamento
                        INNER JOIN medicamento ON tipo_medicamento.id = medicamento.tipo_id
                        INNER JOIN lote_medicamento ON medicamento.id = lote_medicamento.medicamento_id 
                    ORDER BY
                        lote_medicamento.id DESC""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["medicamento"] = datos[1] 
                dic["cantidad"] = datos[2]           
                Convert = datetime.strptime(str(datos[3]), '%Y-%m-%d')
                dic["fecha_i"] = Convert.strftime('%Y-%m-%d') 
                Convert = datetime.strptime(str(datos[4]), '%Y-%m-%d')
                dic["fecha_f"] = Convert.strftime('%Y-%m-%d') 
                dic["codigo"] = datos[5]  
                Convert = datetime.strptime(str(datos[6]), '%Y-%m-%d')
                dic["fecha"] = Convert.strftime('%Y-%m-%d')              
                Convert = datetime.strptime(str(datos[7]), '%H:%M:%S')
                dic["hora"] = Convert.strftime('%H:%M:%S')            
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Eliminar_lote_medicamento(_id):
        try:
            query = mysql.connection.cursor()
            query.execute('DELETE FROM lote_medicamento WHERE id="{0}"'.format(_id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Listar_lote_insumos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_insumo.id,
                        insumo.nombre,
                        lote_insumo.cantidad,
                        lote_insumo.fecha_i,
                        lote_insumo.fecha_f,
                        lote_insumo.codigo,
                        DATE( lote_insumo.fecha ) AS fecha_crear,
                        TIME( lote_insumo.fecha ) AS hora,
                        CONCAT_WS( ' ', insumo.nombre, tipo_insumo.tipo ) AS insumo
                    FROM
                        tipo_insumo
                        INNER JOIN insumo ON tipo_insumo.id = insumo.tipo_id
                        INNER JOIN lote_insumo ON insumo.id = lote_insumo.insumo_id 
                    ORDER BY
                        lote_insumo.id DESC""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["insumo"] = datos[1] 
                dic["cantidad"] = datos[2]           
                Convert = datetime.strptime(str(datos[3]), '%Y-%m-%d')
                dic["fecha_i"] = Convert.strftime('%Y-%m-%d') 
                Convert = datetime.strptime(str(datos[4]), '%Y-%m-%d')
                dic["fecha_f"] = Convert.strftime('%Y-%m-%d') 
                dic["codigo"] = datos[5]  
                Convert = datetime.strptime(str(datos[6]), '%Y-%m-%d')
                dic["fecha"] = Convert.strftime('%Y-%m-%d')              
                Convert = datetime.strptime(str(datos[7]), '%H:%M:%S')
                dic["hora"] = Convert.strftime('%H:%M:%S')            
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Eliminar_lote_insumos(_id):
        try:
            query = mysql.connection.cursor()
            query.execute('DELETE FROM lote_insumo WHERE id="{0}"'.format(_id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    # modelo para cambiar el estado del medicamento
    def Estado_medicamento(_id,_dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE medicamento SET estado = "{0}" WHERE id = "{1}"'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el medicamento
    def Editar_medicamento(_codigo, _nombre, _tipo, _cantidad, _precio, _detalle, id, _presentacion, _cantidad_unidad):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM medicamento WHERE codigo="{0}" AND id!="{1}"'. format(_codigo,id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE medicamento SET codigo="{0}",nombre="{1}",tipo_id="{2}",cantidad="{3}",precio="{4}",detalle="{5}",presentacion="{6}",unidades="{7}" WHERE id="{8}"'.format(_codigo,_nombre,_tipo,_cantidad,_precio,_detalle,_presentacion,_cantidad_unidad,id))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar el insumo en la tabla de compra
    def Table_medicamento():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            medicamento.id,
                            medicamento.codigo,
                            medicamento.nombre,
                            medicamento.tipo_id,
                            tipo_medicamento.tipo,
                            medicamento.cantidad,
                            medicamento.precio,
                            medicamento.detalle,
                            medicamento.foto,
                            medicamento.estado,
                            medicamento.presentacion,
                            medicamento.unidades 
                            FROM
                            medicamento
                            INNER JOIN tipo_medicamento ON medicamento.tipo_id = tipo_medicamento.id WHERE medicamento.estado = 1 
                            ORDER BY medicamento.id ASC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registrar la compra del medicamento
    def Registrar_compra_medicamentoo(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM compra_medicamento WHERE numero_compra = "{0}"'. format(_numero_compra))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO compra_medicamento (usuario_id,proveedor_id,fecha,numero_compra,documento,iva,subtotal,impuesto,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(_id,_id_pro,_fecha_c,_numero_compra,_tipo_comprobante,_iva,_subtotal,_impuesto_sub,_total_pagar))
                query.connection.commit()
                # me devuelve el ultimo id insertado
                id = query.lastrowid
                query.close()
                return id  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registra el detalle de compra del medicamento
    def Registrar_detalle_compra_medicamento(_id, ida, precio, cantidad, descuento, total, unidades, total_unidades, fecha_i, fecha_f, codigo):
        try:
            query = mysql.connection.cursor()         
            query.execute('INSERT INTO detalle_compra_medicamento (compra_medicamento_id,medicamento_id,precio,cantidad,descuento,total,unidad) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(_id,ida,precio,cantidad,descuento,total,unidades))
            query.connection.commit()
            
            query.execute('INSERT INTO lote_medicamento (medicamento_id,cantidad,fecha_i,fecha_f,codigo) VALUES ("{0}","{1}","{2}","{3}","{4}")'.format(ida,total_unidades,fecha_i,fecha_f,codigo))
            query.connection.commit()

            # query.execute('UPDATE medicamento SET cantidad = cantidad + "{0}" WHERE id = "{1}" '.format(cantidad,ida))
            # query.connection.commit()

            query.close()
            return 1  # se inserto correcto

        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar las compras de medicamento
    def Listar_compras_medicamento():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_medicamento.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon, ' - ', proveedor.ruc ) AS proveedor,
                            compra_medicamento.fecha,
                            compra_medicamento.numero_compra,
                            compra_medicamento.documento,
                            compra_medicamento.iva,
                            compra_medicamento.subtotal,
                            compra_medicamento.impuesto,
                            compra_medicamento.total,
                            compra_medicamento.estado 
                        FROM
                            compra_medicamento
                            INNER JOIN usuario ON compra_medicamento.usuario_id = usuario.usuario_id
                            INNER JOIN proveedor ON compra_medicamento.proveedor_id = proveedor.id 
                        ORDER BY
                            compra_medicamento.id DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para anular la compra de medicamento
    def Compra_medicamento_anular(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        detalle_compra_medicamento.medicamento_id,
                        detalle_compra_medicamento.cantidad 
                        FROM
                        detalle_compra_medicamento 
                        WHERE
                        detalle_compra_medicamento.compra_medicamento_id = '{0}'""".format(_id))
            data = query.fetchall()
            
            for dato in data: 
                print(dato)
                query.execute('UPDATE medicamento SET cantidad = cantidad - {0} WHERE id = "{1}"'.format(dato[1], str(dato[0])))
                query.connection.commit()

            query.execute('UPDATE compra_medicamento SET estado = 0 WHERE id = {0}'.format(_id))
            query.connection.commit()

            query.execute('UPDATE detalle_compra_medicamento SET estado = 0 WHERE compra_medicamento_id = "{0}"'.format(_id))
            query.connection.commit()
            query.close() 
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para cambiar la foto del medicamento
    def Cambiar_foto_medicamento(_id,archivo):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE medicamento SET foto = "{0}" WHERE id = "{1}"'.format(archivo, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registrar la compra de la vacuna
    def Registrar_compra_vacuna(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM compra_vacuna WHERE numero_compra = "{0}"'. format(_numero_compra))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO compra_vacuna (usuario_id,proveedor_id,fecha,numero_compra,documento,iva,subtotal,impuesto,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(_id,_id_pro,_fecha_c,_numero_compra,_tipo_comprobante,_iva,_subtotal,_impuesto_sub,_total_pagar))
                query.connection.commit()
                # me devuelve el ultimo id insertado
                id = query.lastrowid
                query.close()
                return id  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registra el detalle de compra de vacuna
    def Registrar_detalle_compra_vacuna(_id, ida, precio, cantidad, descuento, total, fecha_i, fecha_f, codigo, dosis):
        try:
            query = mysql.connection.cursor()         
            query.execute('INSERT INTO detalle_compra_vacuna (compra_vacuna_id,vacuna_id,precio,cantidad,descuento,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}")'.format(_id,ida,precio,cantidad,descuento,total))
            query.connection.commit()
            
            query.execute('INSERT INTO lote_vacuna (vacuna_id,cantidad,fecha_i,fecha_f,codigo) VALUES ("{0}","{1}","{2}","{3}","{4}")'.format(ida,dosis,fecha_i,fecha_f,codigo))
            query.connection.commit()

            # query.execute('UPDATE vacuna SET cantidad = cantidad + "{0}" WHERE id = "{1}" '.format(cantidad,ida))
            # query.connection.commit()

            query.close()
            return 1  # se inserto correcto

        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar las compras de vacunas
    def Listar_compras_vacunas():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_vacuna.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon, ' - ', proveedor.ruc ) AS proveedor,
                            compra_vacuna.fecha,
                            compra_vacuna.numero_compra,
                            compra_vacuna.documento,
                            compra_vacuna.iva,
                            compra_vacuna.subtotal,
                            compra_vacuna.impuesto,
                            compra_vacuna.total,
                            compra_vacuna.estado 
                        FROM
                            compra_vacuna
                            INNER JOIN usuario ON compra_vacuna.usuario_id = usuario.usuario_id
                            INNER JOIN proveedor ON compra_vacuna.proveedor_id = proveedor.id 
                        ORDER BY
                            compra_vacuna.id DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para anular la compra de vacuna
    def Compra_vacuna_anular(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT 
                            detalle_compra_vacuna.vacuna_id,
                            detalle_compra_vacuna.cantidad 
                            FROM
                            detalle_compra_vacuna
                            WHERE
                            detalle_compra_vacuna.compra_vacuna_id = '{0}'""".format(_id))
            data_d = query.fetchall()
            
            for dato in data_d: 
                query.execute('UPDATE vacuna SET cantidad = cantidad - {0} WHERE id = "{1}"'.format(dato[1], str(dato[0])))
                query.connection.commit()

            query.execute('UPDATE compra_vacuna SET estado = 0 WHERE id = {0}'.format(_id))
            query.connection.commit()

            query.execute('UPDATE detalle_compra_vacuna SET estado = 0 WHERE compra_vacuna_id = "{0}"'.format(_id))
            query.connection.commit()
            query.close() 
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
