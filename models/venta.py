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
    