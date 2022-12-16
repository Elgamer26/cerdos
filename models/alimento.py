from utils.db import mysql
from datetime import datetime

class Alimento():
    # modelo de listar tipo de alimento
    def Listar_tipio_alimento():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_alimento ORDER BY id DESC')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["tipo_alimento"] = datos[1]
                dic["estado"] = datos[2]          
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para crear el tipo de alimento
    def Registrar_tipo_alimento(_valor):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_alimento WHERE tipo_alimento = "{0}"'. format(_valor))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO tipo_alimento (tipo_alimento) VALUES ("{0}")'.format(_valor))
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
    
    # modelo para estado del tipo alimentos
    def Estado_alimento_tipo(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE tipo_alimento SET estado = "{0}" WHERE id = "{1}"'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el tipo de alimento
    def Editar_tipo_alimento(_id,_valor):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_alimento WHERE tipo_alimento = "{0}" AND id != "{1}"'. format(_valor,_id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE tipo_alimento SET tipo_alimento="{0}" WHERE id="{1}"'.format(_valor,_id))
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
    
    # modelo de listar tipo de alimento
    def Listar_marca_alimento():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM marca_alimento ORDER BY id DESC')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["marca_alimento"] = datos[1]
                dic["estado"] = datos[2]          
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
   
    # modelo para crear la marca de alimento
    def Registrar_marca_alimento(_valor):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM marca_alimento WHERE marca_alimento = "{0}"'. format(_valor))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO marca_alimento (marca_alimento) VALUES ("{0}")'.format(_valor))
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
    
    # modelo para estado de la marcaa alimentos
    def Estado_marca(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE marca_alimento SET estado = "{0}" WHERE id = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar marca de alimento
    def Editar_marca_alimento(_id,_valor):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM marca_alimento WHERE marca_alimento = "{0}" AND id != "{1}"'. format(_valor,_id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE marca_alimento SET marca_alimento="{0}" WHERE id="{1}"'.format(_valor,_id))
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
    
    #### para el seletc del tipo alimento 
    def Traer_tipo_alimento_select():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_alimento WHERE estado = 1')
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    #### para el seletc de la marca alimento 
    def Traer_marca_alimento_select():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM marca_alimento WHERE estado = 1')
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    # modelo para crear el alimento
    def Craer_alimento(_codigo, _nombre, _tipo, _marca, _cantidad, _precio, _peso, _detalle, archivo):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM alimento WHERE codigo = "{0}"'. format(_codigo))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO alimento (codigo, nombre, tipo_id, marca_id, cantidad, precio, peso, detalle, foto) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(_codigo,_nombre,_tipo,_marca,_cantidad,_precio,_peso,_detalle,archivo))
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
    
    # modelo de listar el alimento
    def Listar_alimentos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            alimento.id,
                            alimento.codigo,
                            alimento.nombre,
                            alimento.tipo_id,
                            alimento.marca_id,
                            alimento.cantidad,
                            alimento.precio,
                            alimento.peso,
                            alimento.detalle,
                            alimento.foto,
                            alimento.estado,
                            marca_alimento.marca_alimento,
                            tipo_alimento.tipo_alimento 
                        FROM
                            alimento
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id 
                        ORDER BY
                            alimento.id DESC""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["codigo"] = datos[1]
                dic["nombre"] = datos[2]  
                dic["tipo_id"] = datos[3]
                dic["marca_id"] = datos[4]
                dic["cantidad"] = datos[5]  
                dic["precio"] = datos[6]
                dic["peso"] = datos[7]
                dic["detalle"] = datos[8]  
                dic["foto"] = datos[9]
                dic["estado"] = datos[10]
                dic["marca_alimento"] = datos[11]
                dic["tipo_alimento"] = datos[12]          
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo de listar el alimento lote
    def Listar_lote_alimento():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_alimento.id,
                            alimento.nombre,
                            lote_alimento.cantidad,
                            lote_alimento.fecha_i,
                            lote_alimento.fecha_f,
                            lote_alimento.codigo,
                            DATE(lote_alimento.fecha)
                        FROM
                            alimento
                            INNER JOIN lote_alimento ON alimento.id = lote_alimento.alimento_id 
                        ORDER BY
                            lote_alimento.id DESC""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["nombre"] = datos[1]
                dic["cantidad"] = datos[2]  
                Convert = datetime.strptime(str(datos[3]), '%Y-%m-%d')
                dic["fecha_i"] = Convert.strftime('%Y-%m-%d')                  
                Convert = datetime.strptime(str(datos[4]), '%Y-%m-%d')
                dic["fecha_f"] = Convert.strftime('%Y-%m-%d')   
                dic["codigo"] = datos[5]  
                Convert = datetime.strptime(str(datos[6]), '%Y-%m-%d')
                dic["fecha"] = Convert.strftime('%Y-%m-%d')      
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
   
    # modelo para estado de alimento
    def Estado_alimento(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE alimento SET estado = "{0}" WHERE id = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para eliminar lote de alimento
    def Eliminar_lote_alimento(_id):
        try:
            query = mysql.connection.cursor()
            query.execute('DELETE FROM lote_alimento WHERE id = "{0}"'.format(_id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para cambiar la foto del alimento
    def Cambiar_foto_alimento(_id, archivo):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE alimento SET foto = "{0}" WHERE id = {1}'.format(archivo, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el alimento
    def Editar_alimento(_codigo, _nombre, _tipo, _marca, _cantidad, _precio, _peso, _detalle, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM alimento WHERE codigo = "{0}" AND id != "{1}"'. format(_codigo, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE alimento SET codigo="{0}", nombre="{1}", tipo_id="{2}", marca_id="{3}", cantidad="{4}", precio="{5}", peso="{6}", detalle="{7}" WHERE id="{8}"'.format(_codigo,_nombre,_tipo,_marca,_cantidad,_precio,_peso,_detalle,_id))
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
    
    # modelo de listar tipo de alimentacion
    def Listar_tipio_alimentacion():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_alimentcion ORDER BY id DESC')
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

    # modelo para crear el tipo de alimentacion
    def Registrar_tipo_alimentacion(_valor):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_alimentcion WHERE tipo = "{0}"'. format(_valor))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO tipo_alimentcion (tipo) VALUES ("{0}")'.format(_valor))
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
    
    # modelo para estado del tipo alimentacion
    def Estado_alimentacion(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE tipo_alimentcion SET estado = "{0}" WHERE id = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar del tipo alimentacion
    def Editar_tipo_alimentacion(_id,_valor):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE tipo_alimentcion SET tipo = "{0}" WHERE id = {1}'.format(_valor, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para el select del alimento del cerdo
    def Select_alimento_cerdo(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            alimento.id,
                            alimento.codigo,
                            alimento.nombre,
                            alimento.tipo_id,
                            alimento.marca_id,
                            alimento.cantidad,
                            alimento.precio,
                            alimento.peso,
                            alimento.detalle,
                            alimento.foto,
                            alimento.estado,
                            marca_alimento.marca_alimento,
                            tipo_alimento.tipo_alimento 
                        FROM
                            alimento
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id WHERE alimento.estado = 1 AND alimento.tipo_id = "{0}"
                        ORDER BY
                            alimento.id DESC""".format(_id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
        # modelo para el select del alimento del cerdo
    def Select_alimento_cerdo_lote(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_alimento.id AS id_lote,
                        lote_alimento.codigo,
                        alimento.nombre,
                        lote_alimento.fecha_f,
                        lote_alimento.cantidad as total_kg,
                        alimento.id AS id_alimento 
                    FROM
                        alimento
                        INNER JOIN lote_alimento ON alimento.id = lote_alimento.alimento_id 
                    WHERE
                        alimento.tipo_id = "{0}"
                        ORDER BY lote_alimento.fecha_f ASC""".format(_id))
            data = query.fetchall()
            query.close()
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {}
                    Convert = datetime.strptime(str(datos[3]), '%Y-%m-%d')
                    dic["fecha_f"] = Convert.strftime('%Y-%m-%d')
                    dic["id_lote"] = datos[0]
                    dic["codigo"] = datos[1] 
                    dic["nombre"] = datos[2]
                    dic["total_kg"] = datos[4]
                    dic["id_alimento"] = datos[5]              
                    new_lista.append(dic)
                return new_lista 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
   
    # modelo para traer cantidas kg lotes
    def Traer_cantidad_lote_kg(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_alimento.cantidad
                    FROM
                        lote_alimento 
                        WHERE
                        lote_alimento.id = '{0}'""".format(_id))
            data = query.fetchone()
            query.close()
            if not data:
                return 0
            else:
                return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para traer la cantidad de sacos de alimento
    def Traer_cantida_saco_alimento(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            alimento.cantidad  
                            FROM
                            alimento
                            WHERE alimento.id = '{0}'""".format(_id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo de listar tipo de alimentacion
    def Traer_tipo_alimentacion_select():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_alimentcion WHERE estado = 1')
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para el select de galpon cerdo
    def Select_cerdo_galpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            cerdo.codigo,
                            cerdo.sexo,
                            raza.raza,
                            cerdo.peso,
                            galpon_cerdo.id_galpon,
                            galpon_cerdo.id_cerdo 
                            FROM
                            galpon_cerdo
                            INNER JOIN cerdo ON galpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza 
                            WHERE galpon_cerdo.id_galpon = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para peso del cerdo
    def Traer_peso_cerdo_actual(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT 
                            cerdo.peso
                            FROM cerdo  
                            WHERE cerdo.id_cerdo = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    # controlador para guadar la alimentacion
    def Registrar_toda_alimentacion(_alimento_id, _tipo_id, _fecha_c, _cantidad_kg, _observacion, _semana, _id, _lote_id, _idcerdo):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO alimentacion (alimento_id,tipo_id,cantidad,observacion,semana,usuario_id,id_cerdo) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(_alimento_id,_tipo_id,_cantidad_kg,_observacion,_semana,_id,_idcerdo))
            query.connection.commit()
            
            # # me devuelve el ultimo id insertado
            # id = query.lastrowid
            
            query.execute('UPDATE lote_alimento SET cantidad = cantidad - "{0}" WHERE id = "{1}"'.format(_cantidad_kg, _lote_id))
            query.connection.commit()
            
            query.execute("SELECT cantidad FROM lote_alimento WHERE id='{0}'".format(_lote_id))
            valor = query.fetchone()
            
            if(valor[0] <= int(0)):
                query.execute("DELETE FROM lote_alimento WHERE id='{0}'".format(_lote_id))
                query.connection.commit()

            query.close()
            return 1  # se inserto correcto 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # controlador para registra el detalle de alimentacion del cerdo
    def Guardar_detalle_alimentacion_todo(_id, ida):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO detalle_alimentacion (id_alimentacion,id_cerdo) VALUES ("{0}","{1}")'.format(_id,ida))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar la alimentación
    def Listar_alimentacion():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            tipo_alimentcion.tipo,
                            alimentacion.fecha,
                            CONCAT_WS( ' ', alimento.nombre, tipo_alimento.tipo_alimento ) AS alimento,
                            alimentacion.observacion,
                            alimentacion.cantidad,
                            alimentacion.semana,
                            CONCAT_WS( ' ', cerdo.codigo, ' - ', cerdo.sexo, ' - ', raza.raza ) AS cerdo 
                        FROM
                            alimentacion
                            INNER JOIN tipo_alimentcion ON alimentacion.tipo_id = tipo_alimentcion.id
                            INNER JOIN alimento ON alimentacion.alimento_id = alimento.id
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id
                            INNER JOIN cerdo ON alimentacion.id_cerdo = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza 
                        ORDER BY
                            alimentacion.id DESC""")
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listar la alimentación por fechas
    def Listar_alimentacion_fecha(f_i,f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            tipo_alimentcion.tipo,
                            alimentacion.fecha,
                            CONCAT_WS( ' ', alimento.nombre, tipo_alimento.tipo_alimento ) AS alimento,
                            alimentacion.observacion,
                            alimentacion.cantidad,
                            alimentacion.semana,
                            CONCAT_WS( ' ', cerdo.codigo, ' - ', cerdo.sexo, ' - ', raza.raza ) AS cerdo 
                        FROM
                            alimentacion
                            INNER JOIN tipo_alimentcion ON alimentacion.tipo_id = tipo_alimentcion.id
                            INNER JOIN alimento ON alimentacion.alimento_id = alimento.id
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id
                            INNER JOIN cerdo ON alimentacion.id_cerdo = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza 
                        WHERE
                            DATE( alimentacion.fecha ) BETWEEN '{0}' AND '{1}' 
                        ORDER BY
                            alimentacion.id DESC""".format(f_i,f_f))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para registra el peso del cerdo
    def Guardar_peso_cerdo(id,peso_pasado,metodo,observacion,etapa_fase,nuevo_pesaje,perimetro_t,largo_c,semana):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO peso_cerdo (cerdo_id,peso_pasado,metodo,observacion,nuevo_pesaje,perimetro_t,largo_c,etapa_fase,semana) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(id,peso_pasado,metodo,observacion,nuevo_pesaje,perimetro_t,largo_c,etapa_fase,semana))
            query.connection.commit()
        
            query.execute('UPDATE cerdo SET peso="{0}", etapa="{1}" WHERE id_cerdo="{2}"'.format(nuevo_pesaje,etapa_fase,id))
            query.connection.commit()

            query.close()
            return 1  # se inserto correcto        
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

   # modelo para listar el pesaje del cerdo por fecha
    def Listar_pesaje_cerdo_fecha(f_i, f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            peso_cerdo.peso_id,
                            CONCAT_WS( ' ', cerdo.codigo, cerdo.sexo, raza.raza ) AS cerdo,
                            peso_cerdo.fecha,
                            peso_cerdo.metodo,
                            peso_cerdo.estado,
                            peso_cerdo.observacion,
                            peso_cerdo.peso_a,
                            peso_cerdo.peso_b,
                            peso_cerdo.p_t,
                            peso_cerdo.l_c,
                            peso_cerdo.p_v,
                            peso_cerdo.estado_ 
                        FROM
                            peso_cerdo
                            INNER JOIN cerdo ON peso_cerdo.cerdo_id = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza 
                            WHERE peso_cerdo.fecha BETWEEN '{0}' AND '{1}'
                        ORDER BY
                            peso_cerdo.peso_id DESC""".format(f_i,f_f))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para traer los datos del pessaje del cerdo
    def Traer_pesos_cerdo(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            peso_cerdo.peso_id,
                            peso_cerdo.fecha,
                            peso_cerdo.metodo,
                            peso_cerdo.estado,
                            peso_cerdo.observacion,
                            peso_cerdo.peso_a,
                            peso_cerdo.peso_b,
                            peso_cerdo.p_t,
                            peso_cerdo.l_c,
                            peso_cerdo.p_v,
                            peso_cerdo.estado_ 
                        FROM
                            peso_cerdo
                            INNER JOIN cerdo ON peso_cerdo.cerdo_id = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE peso_cerdo.cerdo_id = "{0}"
                        ORDER BY
                            peso_cerdo.peso_id DESC""".format(_id))
            data = query.fetchall()
            query.close() 
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {}
                    Convert = datetime.strptime(str(datos[1]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d')
                    dic["metodo"] = datos[2]
                    dic["estado_cerdo"] = datos[3] 
                    dic["observacion"] = datos[4]
                    dic["peso_a"] = datos[5]
                    dic["peso_b"] = datos[6]
                    dic["p_t"] = datos[7]              
                    dic["l_c"] = datos[8]
                    dic["p_v"] = datos[9]              
                    new_lista.append(dic)
                return {"data": new_lista} 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para traer los datos de la alimentacion del cerdo
    def traer_alimentos_del_cerdo(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            detalle_alimentacion.id_cerdo,
                            tipo_alimentcion.tipo,
                            alimentacion.fecha,
                            CONCAT_WS( ' ', 'Alimento: ', alimento.nombre, ' - Tipo: ', tipo_alimento.tipo_alimento, ' - Marca: ', marca_alimento.marca_alimento ) AS alimento,
                            alimentacion.observacion,
                            alimentacion.id 
                            FROM
                                detalle_alimentacion
                                INNER JOIN alimentacion ON detalle_alimentacion.id_alimentacion = alimentacion.id
                                INNER JOIN tipo_alimentcion ON alimentacion.tipo_id = tipo_alimentcion.id
                                INNER JOIN alimento ON alimentacion.alimento_id = alimento.id
                                INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                                INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id 
                            WHERE
                                detalle_alimentacion.id_cerdo = '{0}' 
                            ORDER BY
                            alimentacion.id DESC""".format(_id))
            data = query.fetchall()
            query.close() 
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {}
                    Convert = datetime.strptime(str(datos[2]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d')
                    dic["tipo_alimentcion"] = datos[1]
                    dic["alimento"] = datos[3] 
                    dic["observacion"] = datos[4]            
                    new_lista.append(dic)
                return {"data": new_lista} 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
     # modelo para eliminar peso
    def Eliminar_peso(_id):
        try:
            query = mysql.connection.cursor()
            query.execute('DELETE FROM peso_cerdo WHERE peso_id = {0}'.format(_id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    
    
    
    ####################
    ################ corecciones
    def Listar_aliento_cerdo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            tipo_alimentcion.tipo,
                            DATE( alimentacion.fecha),
                            CONCAT_WS( ' ',  alimento.nombre, tipo_alimento.tipo_alimento ) AS alimento,
                            alimentacion.observacion,
                            alimentacion.id,
                            alimentacion.id_cerdo,
                            TIME( alimentacion.fecha),
                            alimentacion.cantidad,
                            alimentacion.semana 
                        FROM
                            alimentacion
                            INNER JOIN tipo_alimentcion ON alimentacion.tipo_id = tipo_alimentcion.id
                            INNER JOIN alimento ON alimentacion.alimento_id = alimento.id
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id 
                        WHERE
                            alimentacion.id_cerdo = '{0}' 
                        ORDER BY
                            alimentacion.id DESC""". format(id))
            data = query.fetchall()
            query.close()
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    dic["alimento"] = datos[2]
                    dic["tipo"] = datos[0]
                    Convert = datetime.strptime(str(datos[1]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d')        
                    dic["cantidad"] = datos[7]
                    dic["observacion"] = datos[3]
                    dic["semana"] = datos[8] 
                    Convert = datetime.strptime(str(datos[6]), '%H:%M:%S')
                    dic["hora"] = Convert.strftime('%H:%M:%S')  
                    new_lista.append(dic)
                return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Listar_aliento_cerdo_seguimiento(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            tipo_alimentcion.tipo,
                            DATE( alimentacion.fecha),
                            CONCAT_WS( ' ',  alimento.nombre, tipo_alimento.tipo_alimento ) AS alimento,
                            alimentacion.observacion,
                            alimentacion.id,
                            alimentacion.id_cerdo,
                            TIME( alimentacion.fecha),
                            alimentacion.cantidad,
                            alimentacion.semana 
                        FROM
                            alimentacion
                            INNER JOIN tipo_alimentcion ON alimentacion.tipo_id = tipo_alimentcion.id
                            INNER JOIN alimento ON alimentacion.alimento_id = alimento.id
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id 
                        WHERE
                            alimentacion.id_cerdo = '{0}' 
                        ORDER BY
                            alimentacion.id DESC""". format(id))
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["alimento"] = datos[2]
                dic["tipo"] = datos[0]
                Convert = datetime.strptime(str(datos[1]), '%Y-%m-%d')
                dic["fecha"] = Convert.strftime('%Y-%m-%d')        
                dic["cantidad"] = datos[7]
                dic["observacion"] = datos[3]
                dic["semana"] = datos[8] 
                Convert = datetime.strptime(str(datos[6]), '%H:%M:%S')
                dic["hora"] = Convert.strftime('%H:%M:%S')  
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Listar_pesaje_cerdo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                peso_cerdo.cerdo_id,
                DATE( peso_cerdo.fecha ),
                TIME( peso_cerdo.fecha ),
                peso_cerdo.metodo,
                peso_cerdo.peso_pasado,
                peso_cerdo.nuevo_pesaje,
                peso_cerdo.etapa_fase,
                peso_cerdo.perimetro_t,
                peso_cerdo.largo_c,
                peso_cerdo.observacion,
                peso_cerdo.semana
            FROM
                peso_cerdo 
            WHERE
                peso_cerdo.cerdo_id = '{0}'
            ORDER BY
                peso_cerdo.fecha DESC""". format(id))
            data = query.fetchall()
            query.close()
            
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    Convert = datetime.strptime(str(datos[1]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d') 
                    Convert = datetime.strptime(str(datos[2]), '%H:%M:%S')
                    dic["hora"] = Convert.strftime('%H:%M:%S')    
                    dic["metodo"] = datos[3]
                    dic["peso_pasado"] = datos[4]                     
                    dic["nuevo_pesaje"] = datos[5]
                    dic["etapa_fase"] = datos[6]
                    dic["perimetro_t"] = datos[7]                    
                    dic["largo_c"] = datos[8]
                    dic["observacion"] = datos[9] 
                    dic["semana"] = datos[10] 
                    new_lista.append(dic)
                return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
     # modelo para listar el pesaje del cerdo
    def Listar_pesaje_cerdo_seguimeinto(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                peso_cerdo.cerdo_id,
                DATE( peso_cerdo.fecha ),
                TIME( peso_cerdo.fecha ),
                peso_cerdo.metodo,
                peso_cerdo.peso_pasado,
                peso_cerdo.nuevo_pesaje,
                peso_cerdo.etapa_fase,
                peso_cerdo.perimetro_t,
                peso_cerdo.largo_c,
                peso_cerdo.observacion,
                peso_cerdo.semana
            FROM
                peso_cerdo 
            WHERE
                peso_cerdo.cerdo_id = '{0}'
            ORDER BY
                peso_cerdo.fecha DESC""". format(id))
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                Convert = datetime.strptime(str(datos[1]), '%Y-%m-%d')
                dic["fecha"] = Convert.strftime('%Y-%m-%d') 
                Convert = datetime.strptime(str(datos[2]), '%H:%M:%S')
                dic["hora"] = Convert.strftime('%H:%M:%S')    
                dic["metodo"] = datos[3]
                dic["peso_pasado"] = datos[4]                     
                dic["nuevo_pesaje"] = datos[5]
                dic["etapa_fase"] = datos[6]
                dic["perimetro_t"] = datos[7]                    
                dic["largo_c"] = datos[8]
                dic["observacion"] = datos[9] 
                dic["semana"] = datos[10] 
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Listar_vacunasa_cerdo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        DATE(vacunacion.fecha),
                        TIME(vacunacion.fecha),
                        vacuna.nombre,
                        tipo_vacuna.tipo_vacuna,
                        vacunacion.dosis,
                        vacunacion.semana 
                        FROM
                            vacunacion
                            INNER JOIN vacuna ON vacunacion.vacuna_id = vacuna.id
                            INNER JOIN tipo_vacuna ON vacuna.tipo_id = tipo_vacuna.id 
                        WHERE
                            vacunacion.cerdo_id = '{0}' 
                        ORDER BY
                        vacunacion.fecha DESC""". format(id))
            data = query.fetchall()
            query.close()
            
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    Convert = datetime.strptime(str(datos[0]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d') 
                    Convert = datetime.strptime(str(datos[1]), '%H:%M:%S')
                    dic["hora"] = Convert.strftime('%H:%M:%S')    
                    dic["nombre"] = datos[2]
                    dic["tipo_vacuna"] = datos[3]                     
                    dic["dosis"] = datos[4]
                    dic["semana"] = datos[5]                  
                    new_lista.append(dic)
                return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Listar_vacunasa_cerdo_seguimineto(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        DATE(vacunacion.fecha),
                        TIME(vacunacion.fecha),
                        vacuna.nombre,
                        tipo_vacuna.tipo_vacuna,
                        vacunacion.dosis,
                        vacunacion.semana,
                        CONCAT_WS( ' ', vacuna.nombre,' - ',tipo_vacuna.tipo_vacuna)
                        FROM
                            vacunacion
                            INNER JOIN vacuna ON vacunacion.vacuna_id = vacuna.id
                            INNER JOIN tipo_vacuna ON vacuna.tipo_id = tipo_vacuna.id 
                        WHERE
                            vacunacion.cerdo_id = '{0}' 
                        ORDER BY
                        vacunacion.fecha DESC""". format(id))
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                Convert = datetime.strptime(str(datos[0]), '%Y-%m-%d')
                dic["fecha"] = Convert.strftime('%Y-%m-%d') 
                Convert = datetime.strptime(str(datos[1]), '%H:%M:%S')
                dic["hora"] = Convert.strftime('%H:%M:%S')    
                dic["nombre"] = datos[2]
                dic["tipo_vacuna"] = datos[3]                     
                dic["dosis"] = datos[4]
                dic["semana"] = datos[5]  
                dic["vacuna"] = datos[6]                  
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Ver_cerdos_muertos_galpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            muertes.id,
                            CONCAT_WS( ' ', cerdo.codigo, raza.raza, cerdo.sexo ) AS cerdo,
                            muertes.fecha,
                            muertes.motivo, 
                            muertes.hora,
                            muertes.semana,
                            DATE( muertes.f_registro ) AS fecha_r,
                            TIME( muertes.f_registro ) AS hora_r 
                        FROM
                            cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza
                            INNER JOIN muertes ON cerdo.id_cerdo = muertes.id_cerdo 
                        WHERE
                            muertes.id_galpon = '{0}' 
                        ORDER BY
                            muertes.f_registro DESC""". format(id))
            data = query.fetchall()
            query.close()
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    dic["id"] = datos[0]
                    dic["cerdo"] = datos[1]           
                    Convert = datetime.strptime(str(datos[2]), '%Y-%m-%d')
                    dic["fecha_m"] = Convert.strftime('%Y-%m-%d') 
                    dic["motivo"] = datos[3]                     
                    Convert = datetime.strptime(str(datos[4]), '%H:%M:%S')
                    dic["hora_m"] = Convert.strftime('%H:%M:%S')  
                    dic["semana"] = datos[5]                       
                    Convert = datetime.strptime(str(datos[6]), '%Y-%m-%d')
                    dic["fecha_r"] = Convert.strftime('%Y-%m-%d') 
                    Convert = datetime.strptime(str(datos[7]), '%H:%M:%S')
                    dic["hora_r"] = Convert.strftime('%H:%M:%S')            
                    new_lista.append(dic)
                return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Select_vacuna_lote_all(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_vacuna.codigo,
                            vacuna.nombre,
                            lote_vacuna.fecha_f,
                            lote_vacuna.cantidad,
                            lote_vacuna.id AS id_l,
                            vacuna.id AS id_v,
                            tipo_vacuna.id 
                        FROM
                            vacuna
                            INNER JOIN lote_vacuna ON vacuna.id = lote_vacuna.vacuna_id
                            INNER JOIN tipo_vacuna ON vacuna.tipo_id = tipo_vacuna.id 
                        WHERE
                            tipo_vacuna.id = '{0}' 
                        ORDER BY
                            lote_vacuna.fecha_f ASC """.format(id))
            data = query.fetchall()
            query.close()
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    dic["codigo"] = datos[0]
                    dic["nombre"] = datos[1]
                    Convert = datetime.strptime(str(datos[2]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d')        
                    dic["cantidad"] = datos[3]
                    dic["id_l"] = datos[4]
                    dic["id_v"] = datos[5]  
                    new_lista.append(dic)
                return new_lista
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Select_desparasitante_lote_all(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_medicamento.codigo,
                        medicamento.nombre,
                        lote_medicamento.fecha_f,
                        lote_medicamento.cantidad,                        
                        lote_medicamento.id AS id_lote,
                        medicamento.id AS id_me,
                        medicamento.tipo_id 
                    FROM
                        tipo_medicamento
                        INNER JOIN medicamento ON tipo_medicamento.id = medicamento.tipo_id
                        INNER JOIN lote_medicamento ON medicamento.id = lote_medicamento.medicamento_id 
                    WHERE
                        medicamento.tipo_id = "{0}" 
                    ORDER BY
                        lote_medicamento.fecha_f ASC""".format(id))
            data = query.fetchall()
            query.close()
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    dic["codigo"] = datos[0]
                    dic["nombre"] = datos[1]
                    Convert = datetime.strptime(str(datos[2]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d')        
                    dic["cantidad"] = datos[3]
                    dic["id_l"] = datos[4]
                    dic["id_m"] = datos[5]  
                    new_lista.append(dic)
                return new_lista
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Traer_cantidad_dosis_lote(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_vacuna.cantidad
                            FROM
                                lote_vacuna 
                            WHERE
                            lote_vacuna.id = '{0}' """.format(id))
            data = query.fetchone()
            query.close()
            if not data:
                return 0
            else: 
                return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Traer_cantidad_desparasitante_lote(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_medicamento.cantidad 
                    FROM
                        lote_medicamento 
                    WHERE
                        lote_medicamento.id = '{0}'""".format(id))
            data = query.fetchone()
            query.close()
            if not data:
                return 0
            else: 
                return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Guardar_vacunasaa_cerdoo(_id_v, _id_l, _cantidad, _semana, _id_c):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO vacunacion (vacuna_id,semana,cerdo_id,dosis) VALUES ("{0}","{1}","{2}","{3}")'.format(_id_v,_semana,_id_c,_cantidad))
            query.connection.commit()
            
            # me devuelve el ultimo id insertado
            #id = query.lastrowid
            
            query.execute('UPDATE lote_vacuna SET cantidad = cantidad - "{0}" WHERE id = "{1}"'.format(_cantidad, _id_l))
            query.connection.commit()
            
            query.execute("SELECT cantidad FROM lote_vacuna WHERE id='{0}'".format(_id_l))
            valor = query.fetchone()
            
            if(valor[0] <= int(0)):
                query.execute("DELETE FROM lote_vacuna WHERE id='{0}'".format(_id_l))
                query.connection.commit()

            query.close()
            return 1  # se inserto correcto 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Guardar_vacunasaa_cerdoo_todo(_id_v, _id_l, _cantidad, _semana, _id_c, id_galpon_cerdo, fecha_vacuna_t):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO vacunacion (vacuna_id,semana,cerdo_id,dosis) VALUES ("{0}","{1}","{2}","{3}")'.format(_id_v,_semana,_id_c,_cantidad))
            query.connection.commit()
            
            # me devuelve el ultimo id insertado
            #id = query.lastrowid
            
            query.execute('UPDATE lote_vacuna SET cantidad=cantidad-"{0}" WHERE id = "{1}"'.format(_cantidad, _id_l))
            query.connection.commit()
            
            query.execute("SELECT cantidad FROM lote_vacuna WHERE id='{0}'".format(_id_l))
            valor = query.fetchone()
            
            if(valor[0] <= int(0)):
                query.execute("DELETE FROM lote_vacuna WHERE id='{0}'".format(_id_l))
                query.connection.commit()
                
            query.execute("DELETE FROM calendario WHERE tipo='Vacuna' AND galpon_id='{0}' AND start <= '{1}'".format(id_galpon_cerdo, fecha_vacuna_t))
            query.connection.commit()

            query.close()
            return 1  # se inserto correcto 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Guardar_muerte_cerdo(id_cerdo, ig_galpon, fecha, hora, motivo_muerte, semana):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO muertes (id_cerdo,fecha,motivo,id_galpon,hora,semana) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}")'.format(id_cerdo,fecha,motivo_muerte,ig_galpon,hora,semana))
            query.connection.commit()

            query.execute('UPDATE cerdo SET estado = 2 WHERE id_cerdo = {0}'.format(id_cerdo))
            query.connection.commit()

            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Guardar_desparasitantee_cerdoo(_id_d, _id_l, _cantidad, _semana, _id_c):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO desparasitacion (medicamento_id,semana,cerdo_id,cantidad) VALUES ("{0}","{1}","{2}","{3}")'.format(_id_d,_semana,_id_c,_cantidad))
            query.connection.commit()
                        
            query.execute('UPDATE lote_medicamento SET cantidad = cantidad - "{0}" WHERE id = "{1}"'.format(_cantidad, _id_l))
            query.connection.commit()
            
            query.execute("SELECT cantidad FROM lote_medicamento WHERE id='{0}'".format(_id_l))
            valor = query.fetchone()
            
            if(valor[0] <= int(0)):
                query.execute("DELETE FROM lote_medicamento WHERE id='{0}'".format(_id_l))
                query.connection.commit()

            query.close()
            return 1  # se inserto correcto 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Guardar_desparasitantee_cerdoo_todo(_id_d, _id_l, _cantidad, _semana, _id_c, id_galpon_cerdo, fecha_desparasitacion_t):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO desparasitacion (medicamento_id,semana,cerdo_id,cantidad) VALUES ("{0}","{1}","{2}","{3}")'.format(_id_d,_semana,_id_c,_cantidad))
            query.connection.commit()
                        
            query.execute('UPDATE lote_medicamento SET cantidad = cantidad - "{0}" WHERE id = "{1}"'.format(_cantidad, _id_l))
            query.connection.commit()
            
            query.execute("SELECT cantidad FROM lote_medicamento WHERE id='{0}'".format(_id_l))
            valor = query.fetchone()
            
            if(valor[0] <= int(0)):
                query.execute("DELETE FROM lote_medicamento WHERE id='{0}'".format(_id_l))
                query.connection.commit()
            
            query.execute("DELETE FROM calendario WHERE tipo='Desparasitación' AND galpon_id='{0}' AND start <= '{1}'".format(id_galpon_cerdo, fecha_desparasitacion_t))
            query.connection.commit()

            query.close()
            return 1  # se inserto correcto 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Listar_desparasitantess_cerdo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            DATE( desparasitacion.fecha ) AS fecha,
                            TIME( desparasitacion.fecha ) AS tiempo,
                            medicamento.nombre,
                            tipo_medicamento.tipo,
                            desparasitacion.cantidad,
                            desparasitacion.semana 
                        FROM
                            desparasitacion
                            INNER JOIN medicamento ON desparasitacion.medicamento_id = medicamento.id
                            INNER JOIN tipo_medicamento ON medicamento.tipo_id = tipo_medicamento.id 
                        WHERE
                            desparasitacion.cerdo_id = "{0}" 
                        ORDER BY
                            desparasitacion.fecha DESC""". format(id))
            data = query.fetchall()
            query.close()
            
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    Convert = datetime.strptime(str(datos[0]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d') 
                    Convert = datetime.strptime(str(datos[1]), '%H:%M:%S')
                    dic["hora"] = Convert.strftime('%H:%M:%S')    
                    dic["nombre"] = datos[2]
                    dic["tipo"] = datos[3]                     
                    dic["cantidad"] = datos[4]
                    dic["semana"] = datos[5]                  
                    new_lista.append(dic)
                return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Listar_desparasitantess_cerdo_seguimiento(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            DATE( desparasitacion.fecha ) AS fecha,
                            TIME( desparasitacion.fecha ) AS tiempo,
                            medicamento.nombre,
                            tipo_medicamento.tipo,
                            desparasitacion.cantidad,
                            desparasitacion.semana,
                            concat_ws(' ', medicamento.nombre,' - ',
                            tipo_medicamento.tipo)
                        FROM
                            desparasitacion
                            INNER JOIN medicamento ON desparasitacion.medicamento_id = medicamento.id
                            INNER JOIN tipo_medicamento ON medicamento.tipo_id = tipo_medicamento.id 
                        WHERE
                            desparasitacion.cerdo_id = "{0}" 
                        ORDER BY
                            desparasitacion.fecha DESC""". format(id))
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                Convert = datetime.strptime(str(datos[0]), '%Y-%m-%d')
                dic["fecha"] = Convert.strftime('%Y-%m-%d') 
                Convert = datetime.strptime(str(datos[1]), '%H:%M:%S')
                dic["hora"] = Convert.strftime('%H:%M:%S')    
                dic["nombre"] = datos[2]
                dic["tipo"] = datos[3]                     
                dic["cantidad"] = datos[4]
                dic["semana"] = datos[5]   
                dic["medicamaneto"] = datos[6]                  
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    #################
    ############
    def Listar_medicamento_lote_tratamiento():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_medicamento.codigo,
                        medicamento.nombre,
                        lote_medicamento.fecha_f,
                        lote_medicamento.cantidad,                        
                        lote_medicamento.id AS id_lote,
                        medicamento.id AS id_me,
                        medicamento.tipo_id 
                    FROM
                        tipo_medicamento
                        INNER JOIN medicamento ON tipo_medicamento.id = medicamento.tipo_id
                        INNER JOIN lote_medicamento ON medicamento.id = lote_medicamento.medicamento_id 
                    ORDER BY
                        lote_medicamento.fecha_f ASC""")
            data = query.fetchall()
            query.close()
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    dic["codigo"] = datos[0]
                    dic["nombre"] = datos[1]
                    Convert = datetime.strptime(str(datos[2]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d')        
                    dic["cantidad"] = datos[3]
                    dic["id_l"] = datos[4]
                    dic["id_m"] = datos[5]  
                    new_lista.append(dic)
                return new_lista
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Listar_insumo_lote_tratamiento():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_insumo.codigo,
                            insumo.nombre,
                            lote_insumo.fecha_f,
                            lote_insumo.cantidad,
                            lote_insumo.id AS id_lote,
                            insumo.id AS id_in,
                            tipo_insumo.tipo 
                        FROM
                            lote_insumo
                            INNER JOIN insumo ON lote_insumo.insumo_id = insumo.id
                            INNER JOIN tipo_insumo ON insumo.tipo_id = tipo_insumo.id 
                        ORDER BY
                            lote_insumo.fecha_f ASC""")
            data = query.fetchall()
            query.close()
            if not data:
                return 0
            else:
                new_lista = []
                for datos in data:
                    dic = {} 
                    dic["codigo"] = datos[0]
                    dic["nombre"] = datos[1]
                    Convert = datetime.strptime(str(datos[2]), '%Y-%m-%d')
                    dic["fecha"] = Convert.strftime('%Y-%m-%d')        
                    dic["cantidad"] = datos[3]
                    dic["id_l"] = datos[4]
                    dic["id_in"] = datos[5] 
                    dic["tipo"] = datos[6]  
                    new_lista.append(dic)
                return new_lista
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Traer_cantidad_dosis_lote_disponibles(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_insumo.cantidad 
                    FROM
                        lote_insumo 
                    WHERE
                        lote_insumo.id='{0}'""".format(id))
            data = query.fetchone()
            query.close()
            if not data:
                return 0
            else:
                return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0