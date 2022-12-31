from utils.db import mysql

class Venta():
    def Registrar_cliente(nombres, apellidos, domicilio, telefono, cedula, correo):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM cliente WHERE cedula = "{0}"'. format(cedula))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO cliente (nombres,apellidos,domicilio,telefono,cedula,correo) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}")'.format(nombres,apellidos,domicilio,telefono,cedula,correo))
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
    
    def Listar_cliente():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT * FROM cliente ORDER BY id DESC""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id"] = datos[0]
                dic["nombres"] = datos[1]
                dic["apellidos"] = datos[2]
                dic["domicilio"] = datos[3]
                dic["telefono"] = datos[4]
                dic["cedula"] = datos[5]
                dic["correo"] = datos[6]
                dic["estado"] = datos[7]                        
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Cambiar_estado_cliente(id, dato):
        try:
            query = mysql.connection.cursor() 
            query.execute('UPDATE cliente SET estado="{0}" WHERE id="{1}"'.format(dato,id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto 
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Editar_cliente(nombres, apellidos, domicilio, telefono, cedula, correo, id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM cliente WHERE cedula="{0}" AND id!="{1}"'. format(cedula,id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE cliente SET nombres="{0}",apellidos="{1}",domicilio="{2}",telefono="{3}",cedula="{4}",correo="{5}" WHERE id="{6}"'.format(nombres,apellidos,domicilio,telefono,cedula,correo,id))
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
    
    def Listar_cerdos_vender():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        cerdo.id_cerdo,
                        cerdo.codigo,
                        cerdo.nombre,
                        cerdo.sexo,
                        raza.raza,
                        cerdo.peso,
                        cerdo.estado,
                        cerdo.etapa,
                        cerdo.costo,
	                    cerdo.foto
                    FROM
                        cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                    WHERE
                        cerdo.estado = 1 
                        AND cerdo.galpon = 'si' ORDER BY cerdo.peso DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Registra_veenta_cerdos(cliente, fecha_c, numero_venta, tipo_comprobante, iva, subtotal, impuesto_sub, total_pagar):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM venta_cerdos WHERE numero_venta = "{0}"'. format(numero_venta))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO venta_cerdos (cliente_id,fecha,numero_venta,documento,iva,subtotal,impuesto,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}")'.format(cliente,fecha_c,numero_venta,tipo_comprobante,iva,subtotal,impuesto_sub,total_pagar))
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

    def Registrar_detalle_venta_cerdo(id, idc, peso, precio, total):
        try:
            query = mysql.connection.cursor()
            query.execute('INSERT INTO detalle_venta_cerdos (id_venta,id_cerdo,peso,precio,total) VALUES ("{0}","{1}","{2}","{3}","{4}")'.format(id,idc,peso,precio,total))
            query.connection.commit()
            
            query.execute('UPDATE cerdo SET estado=3 WHERE id_cerdo="{0}"'.format(idc))
            query.connection.commit()
            
            query.close()
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Listar_ventas_cerdos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
	                venta_cerdos.id,
                    CONCAT_WS( ' ', cliente.nombres, cliente.apellidos ) AS cliente,
                    venta_cerdos.fecha,
                    venta_cerdos.numero_venta,
                    venta_cerdos.documento,
                    venta_cerdos.iva,
                    venta_cerdos.subtotal,
                    venta_cerdos.impuesto,
                    venta_cerdos.total,
                    venta_cerdos.estado 
                FROM
                    venta_cerdos
                    INNER JOIN cliente ON venta_cerdos.cliente_id = cliente.id 
                ORDER BY
                    venta_cerdos.id DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def venta_cerdo_anular(id):
        try:
            query = mysql.connection.cursor()
            query.execute("UPDATE venta_cerdos SET estado=0 WHERE id='{0}'".format(id))
            query.connection.commit()
            
            query.execute("""UPDATE detalle_venta_cerdos
                    INNER JOIN cerdo ON detalle_venta_cerdos.id_cerdo = cerdo.id_cerdo 
                    SET cerdo.estado=1 
                    WHERE detalle_venta_cerdos.id_venta = '{0}'""".format(id))
            query.connection.commit()
            
            query.close()
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Cabecera_factura(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
	                venta_cerdos.id,
                    CONCAT_WS( ' ', cliente.nombres, cliente.apellidos ) AS cliente,
                    cliente.correo,
                    venta_cerdos.fecha,
                    cliente.cedula,
                    venta_cerdos.numero_venta,
                    venta_cerdos.documento,
                    venta_cerdos.iva,
                    venta_cerdos.subtotal,
                    venta_cerdos.impuesto,
                    venta_cerdos.total,
                    venta_cerdos.estado                    
                FROM
                    venta_cerdos
                    INNER JOIN cliente ON venta_cerdos.cliente_id = cliente.id 
                WHERE venta_cerdos.id={0}""".format(id))
            data = query.fetchone()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Detalle_venta(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS( ' ', cerdo.codigo, cerdo.sexo, raza.raza ) AS cerdo,
                        detalle_venta_cerdos.peso,
                        detalle_venta_cerdos.precio,
                        detalle_venta_cerdos.total
                    FROM
                        detalle_venta_cerdos
                        INNER JOIN cerdo ON detalle_venta_cerdos.id_cerdo = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                    WHERE
                        detalle_venta_cerdos.id_venta = '{0}'""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0