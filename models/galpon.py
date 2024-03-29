from utils.db import mysql
from datetime import datetime

class Galpon():
    # modelo para crear tipo de galpo
    def Crear_tipo_galpo(_tipo_g):
        try:
            query = mysql.connection.cursor()
            query.execute( 'SELECT * FROM tipo_galpon WHERE tipo_galpon = "{0}"'. format(_tipo_g))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO tipo_galpon (tipo_galpon) VALUES ("{0}")'.format(_tipo_g))
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

    # modelo de listar tipo de galpon
    def Listar_cerdo_galpon_LIST():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            galpon.id_galpon,
                            galpon.numero, 
                            galpon.capacidad,
                            galpon.observacion, 
                            COUNT(galpon_cerdo.id_cerdo) as cerdo,
                            tipo_galpon.tipo_galpon 
                            FROM
                            galpon
                            INNER JOIN galpon_cerdo ON galpon.id_galpon = galpon_cerdo.id_galpon
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo 
                            GROUP BY
                            galpon_cerdo.id_galpon ORDER BY id_galpon DESC""")
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    ######################
    ####################
    # modelo de listar tipo de galpon new
    def Listar_cerdos_en_galpon():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            galpon_cerdo_new.id,
                            galpon.numero,
                            tipo_galpon.tipo_galpon,
                            galpon.capacidad,
                            galpon_cerdo_new.fecha_i,
                            galpon_cerdo_new.fecha_f,
                            galpon_cerdo_new.semana,
                            COUNT( detallegalpon_cerdo.id ) AS cantidad,
                            galpon.observacion,
                            galpon_cerdo_new.id_galpon,
                            COUNT( detallegalpon_cerdo.id_cerdo ) 
                        FROM
                            galpon_cerdo_new
                            INNER JOIN detallegalpon_cerdo ON galpon_cerdo_new.id = detallegalpon_cerdo.id_galpon
                            INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN galpon ON galpon_cerdo_new.id_galpon = galpon.id_galpon
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza 
                        GROUP BY
                            galpon_cerdo_new.id_galpon 
                        ORDER BY galpon_cerdo_new.id
                        DESC""")
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ####################
    # modelo de buscar el galpon new
    def Listar_galpon_cerdos_buscar(valor):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            galpon_cerdo_new.id,
                            galpon.numero,
                            tipo_galpon.tipo_galpon,
                            galpon.capacidad,
                            galpon_cerdo_new.fecha_i,
                            galpon_cerdo_new.fecha_f,
                            galpon_cerdo_new.semana,
                            COUNT( detallegalpon_cerdo.id ) AS cantidad,
                            galpon.observacion,
                            galpon_cerdo_new.id_galpon,
                            COUNT( detallegalpon_cerdo.id_cerdo ) 
                        FROM
                            galpon_cerdo_new
                            INNER JOIN detallegalpon_cerdo ON galpon_cerdo_new.id = detallegalpon_cerdo.id_galpon
                            INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN galpon ON galpon_cerdo_new.id_galpon = galpon.id_galpon
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza 
                            WHERE galpon.numero LIKE '%{0}%' OR tipo_galpon.tipo_galpon LIKE '%{0}%'
                        GROUP BY
                            galpon_cerdo_new.id_galpon 
                        ORDER BY
                            galpon_cerdo_new.id DESC""".format(valor))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0


    # modelo para listar los cerdos del galpon
    def Listar_cerdos_galpon_tabla(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            galpon_cerdo.fecha,
                            cerdo.codigo,
                            cerdo.sexo,
                            raza.raza,
                            cerdo.foto,
                            cerdo.peso,
                            cerdo.origen,
                            galpon_cerdo.id_galpon_cerdo,
                            galpon_cerdo.id_galpon,
                            galpon_cerdo.id_cerdo 
                        FROM
                            galpon_cerdo
                            INNER JOIN cerdo ON galpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE galpon_cerdo.id_galpon = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    # modelo para listar los cerdos del galpon
    def Listar_cerdos_galpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            galpon_cerdo.fecha,
                            cerdo.codigo,
                            cerdo.sexo,
                            raza.raza,
                            cerdo.foto,
                            cerdo.peso,
                            cerdo.origen,
                            galpon_cerdo.id_galpon_cerdo,
                            galpon_cerdo.id_galpon,
                            galpon_cerdo.id_cerdo 
                        FROM
                            galpon_cerdo
                            INNER JOIN cerdo ON galpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE galpon_cerdo.id_galpon = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                Convert = datetime.strptime(str(datos[0]), '%Y-%m-%d')
                dic["fecha"] = Convert.strftime('%Y-%m-%d')
                dic["codigo"] = datos[1]
                dic["sexo"] = datos[2]
                dic["raza"] = datos[3]
                dic["foto"] = datos[4]
                dic["peso"] = datos[5]
                dic["origen"] = datos[6]
                dic["id_galpon_cerdo"] = datos[7] 
                dic["id_galpon"] = datos[8]
                dic["id_cerdo"] = datos[9]           
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    ########################################

    # modelo de listar tipo de galpon
    def Listar_tipo_galpon():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_galpon ORDER BY id_tipo DESC')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id"] = datos[0]
                dic["tipo_galpon"] = datos[1]
                dic["estado"] = datos[2]
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado de la raza
    def Estado_tipo_g(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE tipo_galpon SET estado = "{0}" WHERE id_tipo = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el tipo de galpon
    def Editar_tipo_g(_tipo_g, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_galpon WHERE tipo_galpon = "{0}" AND id_tipo != "{1}"'. format(_tipo_g, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE tipo_galpon SET tipo_galpon = "{0}" WHERE id_tipo = "{1}"'.format(_tipo_g, _id))
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

    # modelo de listar tipo de galpon combo
    def Traer_tipo_galpon_combo():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_galpon WHERE estado = 1')
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para crear galpon
    def Crear_galpon(_numero, _id_tipo, _capacidad, _observacion):
        try:
            query = mysql.connection.cursor()
            query.execute( 'SELECT * FROM galpon WHERE numero = "{0}"'. format(_numero))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO galpon (numero, id_tipo, capacidad, observacion) VALUES ("{0}","{1}","{2}","{3}")'.format(_numero, _id_tipo, _capacidad, _observacion))
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

    # modelo de listar galpon
    def Listar_galpon():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        galpon.id_galpon,
                        galpon.numero,
                        galpon.id_tipo,
                        tipo_galpon.tipo_galpon,
                        galpon.capacidad,
                        galpon.observacion,
                        galpon.estado,
                        galpon.disponible
                        FROM
                        tipo_galpon
                        INNER JOIN galpon ON tipo_galpon.id_tipo = galpon.id_tipo ORDER BY id_galpon DESC""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id"] = datos[0]
                dic["numero"] = datos[1]
                dic["id_tipo"] = datos[2]
                dic["tipo_galpon"] = datos[3]
                dic["capacidad"] = datos[4]
                dic["observacion"] = datos[5]
                dic["estado"] = datos[6]
                dic["disponible"] = datos[7]
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para estado del galpon
    def Estado_galpon(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE galpon SET estado = "{0}" WHERE id_galpon = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para editar galpon
    def Editar_galpon(_id, _numero, _id_tipo, _capacidad, _observacion):
        try:
            query = mysql.connection.cursor()
            query.execute( 'SELECT * FROM galpon WHERE numero = "{0}" AND id_galpon != "{1}"'. format(_numero, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE galpon SET numero="{0}", id_tipo="{1}", capacidad="{2}", observacion="{3}" WHERE id_galpon="{4}"'.format(_numero, _id_tipo, _capacidad, _observacion, _id))
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

    # modelo de listar galpon combo
    def Listar_galpon_combo():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        detallegalpon_cerdo.id_galpon,
                        tipo_galpon.tipo_galpon,
                        galpon.numero,
                        galpon_cerdo_new.fecha_i,
                        galpon_cerdo_new.fecha_f 
                        FROM
                            detallegalpon_cerdo
                            INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN galpon_cerdo_new ON detallegalpon_cerdo.id_galpon = galpon_cerdo_new.id
                            INNER JOIN galpon ON galpon_cerdo_new.id_galpon = galpon.id_galpon
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo 
                        GROUP BY
                            detallegalpon_cerdo.id_galpon""")
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listar no cerdos que no tienen galpon
    def Listar_cerdo_galpon():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
            cerdo.id_cerdo, cerdo.codigo, cerdo.nombre, cerdo.sexo, raza.raza, cerdo.raza,
            cerdo.peso, cerdo.origen, cerdo.fecha, cerdo.detalle,
            cerdo.foto, cerdo.estado, cerdo.galpon 
            FROM cerdo INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE cerdo.galpon ='no' AND cerdo.estado = 1""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id"] = datos[0]
                dic["codigo"] = datos[1]
                dic["nombre"] = datos[2]
                dic["sexo"] = datos[3]
                dic["raza"] = datos[4]
                dic["raza_id"] = datos[5]
                dic["peso"] = datos[6]
                dic["origen"] = datos[7]
                dic["detalle"] = datos[9]
                dic["foto"] = datos[10]
                dic["estado"] = datos[11]                
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para traer la capacidad y disponibilidad
    def Traer_disponible_capacidad(_id):
        try:
            query = mysql.connection.cursor()
            query.execute( 'CALL sp_capacidad_disponible({0})'. format(_id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    ##### coreccion
    ########
    # modelo para traer la capacidad y disponibilidad
    def Traer_capacidad_galponn(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        galpon.capacidad 
                        FROM
                            galpon 
                        WHERE
                        galpon.id_galpon = '{0}'""". format(_id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    ##############    

    # modelo para registra el galpn con el cerdo
    def Registrar_cerdo_galpon(_id, id_c, fecha):
        try:
            query = mysql.connection.cursor() 
            query.execute('INSERT INTO galpon_cerdo (id_galpon, id_cerdo, fecha) VALUES ("{0}","{1}","{2}")'.format(_id, id_c, fecha))
            query.connection.commit()      

            query.execute('UPDATE cerdo SET galpon = "si" WHERE id_cerdo = "{0}"'.format(id_c))
            query.connection.commit()      

            query.close()
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ####################
    # modelo para registra el galpn con el cerdo
    def Registrar_cerdo_galpon_new(id_galpon, fecha_i, fecha_f, semanas):
        try:
            query = mysql.connection.cursor() 
            query.execute('INSERT INTO galpon_cerdo_new (id_galpon, fecha_i, fecha_f, semana) VALUES ("{0}","{1}","{2}","{3}")'.format(id_galpon, fecha_i, fecha_f, semanas))
            query.connection.commit()    
        
            id = query.lastrowid 
            
            query.execute('UPDATE galpon SET disponible = 0 WHERE id_galpon = "{0}"'.format(id_galpon))
            query.connection.commit()      
            
            query.close()
            return id
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para registra el detalle galpn con el cerdo
    def Registrar_detalle_cerdo_galpon(_id, id_c, fecha):
        try:
            query = mysql.connection.cursor() 
            query.execute('INSERT INTO detallegalpon_cerdo (id_galpon, id_cerdo, fecha) VALUES ("{0}","{1}","{2}")'.format(_id, id_c, fecha))
            query.connection.commit()      

            query.execute('UPDATE cerdo SET galpon = "si" WHERE id_cerdo = "{0}"'.format(id_c))
            query.connection.commit()      

            query.close()
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    #####################

    # modelo para pasar el cerdo a otro galpon
    def Editar_cerdo_galpon(_id_a, _id_n, id_c, fecha, id_f, _text):
        try:
            query = mysql.connection.cursor() 
            query.execute('UPDATE galpon_cerdo SET fecha="{0}", id_galpon="{1}" WHERE id_galpon="{2}" AND id_cerdo="{3}"'.format(fecha, _id_n, _id_a, id_c))
            query.connection.commit()      

            query.execute('INSERT INTO movimientos (id_g_c, fecha, hasta) VALUES ("{0}","{1}","{2}")'.format(id_f, fecha, _text))
            query.connection.commit()      

            query.close()
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para movimientos de cerdos de galpones
    def Movimientos_cerdo():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            movimientos.fecha AS fecha_m,
                            movimientos.hasta AS galpn_actual,
                            CONCAT_WS(" ", "N°: ", galpon.numero, " Tipo: ", tipo_galpon.tipo_galpon ) AS galpon_nuevo,
                            cerdo.codigo,
                            cerdo.sexo,
                            raza.raza,
                            cerdo.foto,
                            cerdo.nombre 
                            FROM
                            movimientos
                            INNER JOIN galpon_cerdo ON movimientos.id_g_c = galpon_cerdo.id_galpon_cerdo
                            INNER JOIN galpon ON galpon_cerdo.id_galpon = galpon.id_galpon
                            INNER JOIN cerdo ON galpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo ORDER BY movimientos.id_m DESC""")
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para movimientos de cerdos de galpones por fechas
    def Movimientos_cerdo_fecha(f_i, f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            movimientos.fecha AS fecha_m,
                            movimientos.hasta AS galpn_actual,
                            CONCAT_WS(" ", "N°: ", galpon.numero, " Tipo: ", tipo_galpon.tipo_galpon ) AS galpon_nuevo,
                            cerdo.codigo,
                            cerdo.sexo,
                            raza.raza,
                            cerdo.foto,
                            cerdo.nombre 
                            FROM
                            movimientos
                            INNER JOIN galpon_cerdo ON movimientos.id_g_c = galpon_cerdo.id_galpon_cerdo
                            INNER JOIN galpon ON galpon_cerdo.id_galpon = galpon.id_galpon
                            INNER JOIN cerdo ON galpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo 
                            WHERE movimientos.fecha between "{0}" AND "{1}" ORDER BY movimientos.id_m DESC""".format(f_i, f_f))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listar el cerdo dentro de un galpon
    def Select_cerdos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
            cerdo.id_cerdo, cerdo.codigo, cerdo.nombre, cerdo.sexo, raza.raza, cerdo.raza,
            cerdo.peso, cerdo.origen, cerdo.fecha, cerdo.detalle,
            cerdo.foto, cerdo.estado, cerdo.galpon 
            FROM cerdo INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE cerdo.galpon ='si' AND cerdo.estado = 1""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Combo_cerdo_tratados_list():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        cerdo.id_cerdo,
                        CONCAT_WS( ' ', 'Código: ', cerdo.codigo, '- Sexo: ', cerdo.sexo, '- Raza: ', raza.raza ) AS cerdo,
                        cerdo.estado 
                    FROM
                        tratamiento_cerdos
                        INNER JOIN enfermedad_cerdo ON tratamiento_cerdos.enfer_cerdo_id = enfermedad_cerdo.id
                        INNER JOIN cerdo ON enfermedad_cerdo.cerdo_id = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                    WHERE
                        cerdo.estado = 1 
                    GROUP BY
                        cerdo.id_cerdo 
                    ORDER BY
                        tratamiento_cerdos.id DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0


    #####
    #####################################
    #### corecciones
    def Listar_galpo_cerdo_id(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        galpon_cerdo_new.id,
                        galpon_cerdo_new.id_galpon,
                        galpon_cerdo_new.fecha_i,
                        galpon_cerdo_new.fecha_f,
                        galpon_cerdo_new.semana,
                        galpon.capacidad,
                        CONCAT_WS( ' ', galpon.numero, ' - ', tipo_galpon.tipo_galpon ) AS galpon,
                        galpon.observacion
                    FROM
                        galpon_cerdo_new
                        INNER JOIN galpon ON galpon_cerdo_new.id_galpon = galpon.id_galpon
                        INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo 
                    WHERE
                        galpon_cerdo_new.id = '{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Traer_cerdo_dentro_galpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
            detallegalpon_cerdo.id_galpon,
            detallegalpon_cerdo.id_cerdo,
            cerdo.codigo,
            cerdo.nombre,
            cerdo.sexo,
            raza.raza,
            cerdo.peso,
            cerdo.etapa,
            cerdo.estado 
            FROM
            detallegalpon_cerdo
            INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo
            INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE detallegalpon_cerdo.id_galpon = '{0}' AND cerdo.estado = 1""". format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Traer_cerdo_dentro_galpon_buscar(id, valor):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
            detallegalpon_cerdo.id_galpon,
            detallegalpon_cerdo.id_cerdo,
            cerdo.codigo,
            cerdo.nombre,
            cerdo.sexo,
            raza.raza,
            cerdo.peso,
            cerdo.etapa,
            cerdo.estado 
            FROM
            detallegalpon_cerdo
            INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo
            INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE cerdo.codigo LIKE '%{0}%'
            AND detallegalpon_cerdo.id_galpon='{1}' AND cerdo.estado = 1""". format(valor, id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

#            OR cerdo.nombre LIKE '%"{0}"% OR cerdo.sexo LIKE '%"{0}"% OR cerdo.etapa LIKE '%"{0}"% OR cerdo.raza LIKE '%"{0}"%
    def Hembras_Machos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""CALL Machoo_Hembra('{0}')""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Traer_cantidad_cerdos_glpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        COUNT( detallegalpon_cerdo.id_cerdo ) AS cerdos
                        FROM
                        detallegalpon_cerdo
                        INNER JOIN galpon_cerdo_new ON detallegalpon_cerdo.id_galpon = galpon_cerdo_new.id
                        INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo 
                        WHERE
                        galpon_cerdo_new.id_galpon = '{0}' AND 	cerdo.estado = 1
                        GROUP BY
                        galpon_cerdo_new.id_galpon""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ##################### MOVER CERDOS A OTRO GALPON

    def Guardar_cerdos_movimiento(id_anterior, id_cergo_galpon, galpon_nuevo):
        try:
            query = mysql.connection.cursor() 
            query.execute("UPDATE galpon_cerdo_new SET id_galpon='{0}' WHERE id='{1}'".format(galpon_nuevo, id_cergo_galpon))
            query.connection.commit() 
            
            query.execute("UPDATE galpon SET disponible=0 WHERE id_galpon='{0}'".format(galpon_nuevo))
            query.connection.commit()      

            query.execute("UPDATE galpon SET disponible=1 WHERE id_galpon='{0}'".format(id_anterior))
            query.connection.commit()    

            query.close()
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Listar_galpon_combooo():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        galpon.id_galpon,
                        galpon.numero,
                        galpon.id_tipo,
                        tipo_galpon.tipo_galpon,
                        galpon.capacidad,
                        galpon.observacion,
                        galpon.estado,
                        galpon.disponible
                        FROM
                        tipo_galpon
                        INNER JOIN galpon ON tipo_galpon.id_tipo = galpon.id_tipo ORDER BY id_galpon DESC""")
            data = query.fetchall()
            query.close()  
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    