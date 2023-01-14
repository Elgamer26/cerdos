from utils.db import mysql 

class Reportes():
     #modelo para traer los datos de la empresa
    def Traer_empresa():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            empresa.nombre, 
                            empresa.telefono, 
                            empresa.correo, 
                            empresa.direccion,
                            empresa.foto
                        FROM
                            empresa""")
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    #modelo para traer el galpon de los cerdo
    def Listar_galpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            galpon.id_galpon,
                            galpon.numero, 
                            galpon.capacidad, 
                            COUNT(galpon_cerdo.id_cerdo) as cerdo,
                            tipo_galpon.tipo_galpon 
                            FROM
                            galpon
                            INNER JOIN galpon_cerdo ON galpon.id_galpon = galpon_cerdo.id_galpon
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo  WHERE galpon.id_galpon = "{0}"
                            GROUP BY
                            galpon_cerdo.id_galpon""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer los cerdos del galpon
    def Cerdo_galpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            DATE(galpon_cerdo.fecha) as fecha,
                            cerdo.codigo,
                            cerdo.sexo,
                            raza.raza, 
                            cerdo.peso
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
 
    ######################### COMPRAS ALIMENTOS

    #modelo para listar la compra del alimento
    def Listar_compra_alimento(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_alimento.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon) AS proveedor,
                            proveedor.ruc,
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
                            INNER JOIN proveedor ON compra_alimento.proveedor_id = proveedor.id WHERE compra_alimento.id='{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer el detalle de la compra
    def Detalle_compra_alimento(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            detalle_compra_alimento.compra_alimento_id,
                            alimento.codigo,
                            alimento.nombre,
                            detalle_compra_alimento.precio,
                            detalle_compra_alimento.cantidad,
                            detalle_compra_alimento.descuento,
                            detalle_compra_alimento.total,
                            detalle_compra_alimento.estado 
                        FROM
                            detalle_compra_alimento
                            INNER JOIN alimento ON detalle_compra_alimento.alimento_id = alimento.id 
                        WHERE
                            detalle_compra_alimento.compra_alimento_id = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    ######################### ALIMENTACION

    # modelo para listar la alimentación
    def Listar_alimentacion(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        alimentacion.id,
                        CONCAT_WS( " ", alimento.nombre, " - ", tipo_alimento.tipo_alimento ) AS alimento,
                        CONCAT_WS( " ", usuario.nombres ) AS usuario,
                        alimentacion.fecha,
                        alimentacion.cantidad,
                        alimentacion.observacion,
                        alimentacion.estado 
                        FROM
                        alimentacion
                        INNER JOIN alimento ON alimentacion.alimento_id = alimento.id
                        INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                        INNER JOIN usuario ON alimentacion.usuario_id = usuario.usuario_id WHERE alimentacion.id='{0}'""".format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listar los cerdos alimentados
    def Cerdos_alimentados(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS( " ", cerdo.codigo, " - ", cerdo.nombre, " - ", raza.raza ) AS cerdo,
                        detalle_alimentacion.peso 
                       FROM
                        detalle_alimentacion
                        INNER JOIN cerdo ON detalle_alimentacion.id_cerdo = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                        WHERE detalle_alimentacion.id_alimentacion = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ######################### COMPRAS INSUMOS

    #modelo para listar la compra del insumo
    def Listar_compra_insumos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_insumo.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon) AS proveedor,
                            proveedor.ruc,
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
                            INNER JOIN proveedor ON compra_insumo.proveedor_id = proveedor.id WHERE compra_insumo.id='{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer el detalle de la compra
    def Detalle_compra_insumos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            detalle_compra_insumo.compra_insumo_id,
                            insumo.codigo,
                            insumo.nombre,
                            detalle_compra_insumo.precio,
                            detalle_compra_insumo.cantidad,
                            detalle_compra_insumo.descuento,
                            detalle_compra_insumo.total,
                            detalle_compra_insumo.estado 
                        FROM
                            detalle_compra_insumo
                            INNER JOIN insumo ON detalle_compra_insumo.insumo_id = insumo.id 
                        WHERE
                            detalle_compra_insumo.compra_insumo_id = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    ######################### COMPRAS MEDICINAS

    #modelo para listar la compra del medicamento
    def Listar_compra_medicinas(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_medicamento.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon) AS proveedor,
                            proveedor.ruc,
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
                            INNER JOIN proveedor ON compra_medicamento.proveedor_id = proveedor.id WHERE compra_medicamento.id='{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer el detalle de la compra
    def Detalle_compra_medicamneto(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            detalle_compra_medicamento.compra_medicamento_id,
                            medicamento.codigo,
                            medicamento.nombre,
                            detalle_compra_medicamento.precio,
                            detalle_compra_medicamento.cantidad,
                            detalle_compra_medicamento.descuento,
                            detalle_compra_medicamento.total,
                            detalle_compra_medicamento.estado 
                        FROM
                            detalle_compra_medicamento
                            INNER JOIN medicamento ON detalle_compra_medicamento.medicamento_id = medicamento.id 
                        WHERE
                            detalle_compra_medicamento.compra_medicamento_id = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    ######################### TRATAMIENDOS HISTORIA

    # modelo para listado de trataiendos de los cerdos
    def tratamiendo_cerdo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        tratamiento_cerdos.id,
                        tratamiento_cerdos.enfer_cerdo_id,
                        CONCAT_WS( ' ', 'Código: ', cerdo.codigo, '- Sexo: ', cerdo.sexo, '- Raza: ', raza.raza ) AS cerdo,
                        CONCAT_WS( ' ', veterinario.nombre, veterinario.apellido ) AS veterinario,
                        tratamiento_cerdos.peso,
                        tratamiento_cerdos.fecha_i,
                        tratamiento_cerdos.fecha_f,
                        tratamiento_cerdos.observacion,
                        enfermedad_cerdo.fecha,
                        enfermedad_cerdo.sintomas,
                        enfermedad_cerdo.diagnostico 
                    FROM
                        tratamiento_cerdos
                        INNER JOIN enfermedad_cerdo ON tratamiento_cerdos.enfer_cerdo_id = enfermedad_cerdo.id
                        INNER JOIN veterinario ON enfermedad_cerdo.veterinario_id = veterinario.id
                        INNER JOIN cerdo ON enfermedad_cerdo.cerdo_id = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                    WHERE
                        tratamiento_cerdos.id = '{0}'""".format(id))
            data = query.fetchone()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Detalle_enfermedad(idd):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        detalle_enfermedad_cerdo.cerdo_enfermedad_id,
                        enfermedad.nombre 
                        FROM
                            detalle_enfermedad_cerdo
                            INNER JOIN enfermedad ON detalle_enfermedad_cerdo.enfermedad_id = enfermedad.id 
                        WHERE
                            detalle_enfermedad_cerdo.cerdo_enfermedad_id = '{0}'""".format(idd))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ######################### INFORME COMPA ALIMENTOS POR FECHAS

    # modelo para listado las compras de alimentos por fecha
    def Informe_compras_alimento(f_i, f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                    compra_alimento.fecha,
                    compra_alimento.numero_compra,
                    compra_alimento.iva,
                    compra_alimento.subtotal,
                    compra_alimento.impuesto,
                    compra_alimento.total 
                FROM
                    compra_alimento 
                WHERE
                    compra_alimento.estado = 1 AND DATE(compra_alimento.fecha) BETWEEN '{0}' AND '{1}' """.format(f_i,f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ######################### INFORME COMPA INSUMOS POR FECHAS

    # modelo para listado las compras de insumos por fecha
    def Informe_compras_insumo(f_i, f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        compra_insumo.fecha,
                        compra_insumo.numero_compra,
                        compra_insumo.iva,
                        compra_insumo.subtotal,
                        compra_insumo.impuesto,
                        compra_insumo.total 
                    FROM
                        compra_insumo 
                    WHERE
                        compra_insumo.estado = 1 
                        AND DATE( compra_insumo.fecha ) BETWEEN '{0}' AND '{1}' """.format(f_i,f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ######################### INFORME COMPA MEDICAMENTO POR FECHAS

    # modelo para listado las compras de medicamentos por fecha
    def Informe_compras_medicamentos(f_i, f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        compra_medicamento.fecha,
                        compra_medicamento.numero_compra,
                        compra_medicamento.iva,
                        compra_medicamento.subtotal,
                        compra_medicamento.impuesto,
                        compra_medicamento.total 
                    FROM
                        compra_medicamento 
                    WHERE
                        compra_medicamento.estado = 1 
                        AND DATE( compra_medicamento.fecha ) BETWEEN '{0}' AND '{1}' """.format(f_i,f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ######################### INFORME COMPA VACUNAS POR FECHAS

    # modelo para listado las compras de vacunas por fecha
    def Informe_compras_vacunas(f_i, f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        compra_vacuna.fecha,
                        compra_vacuna.numero_compra,
                        compra_vacuna.iva,
                        compra_vacuna.subtotal,
                        compra_vacuna.impuesto,
                        compra_vacuna.total 
                    FROM
                        compra_vacuna 
                    WHERE
                        compra_vacuna.estado = 1 
                        AND DATE( compra_vacuna.fecha ) BETWEEN '{0}' AND '{1}' """.format(f_i,f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ######################### INFORME CONTROL DE PESO DEL CERDO POR FECHAS

    # modelo para listar el cerdo
    def Cerdos_reporte(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        cerdo.id_cerdo,
                        CONCAT_WS( ' ', cerdo.codigo, '-', cerdo.sexo, '-', raza.raza ) AS cerdo,
                        cerdo.peso,
                        galpon.numero 
                    FROM
                        cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza
                        INNER JOIN galpon_cerdo ON cerdo.id_cerdo = galpon_cerdo.id_cerdo
                        INNER JOIN galpon ON galpon_cerdo.id_galpon = galpon.id_galpon WHERE 
                        cerdo.estado = 1 AND cerdo.id_cerdo = '{0}' """.format(id))
            data = query.fetchone()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listado los pesos del cerdo por fechas
    def Informe_control_peso(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        peso_cerdo.cerdo_id,
                        DATE( peso_cerdo.fecha ) AS fecha,
                        TIME( peso_cerdo.fecha ) AS hora,
                        peso_cerdo.metodo,
                        peso_cerdo.nuevo_pesaje,
                        peso_cerdo.etapa_fase,
                        peso_cerdo.perimetro_t,
                        peso_cerdo.largo_c,
                        peso_cerdo.semana 
                    FROM
                        peso_cerdo 
                    WHERE
                        peso_cerdo.cerdo_id = '{0}' 
                    ORDER BY
                        peso_cerdo.fecha ASC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ######################### INFORME DE CERDOS

    # modelo para listar los cerdo por razas
    def Cerdos_por_raza(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        cerdo.codigo,
                        cerdo.nombre,
                        cerdo.sexo,
                        raza.raza,
                        cerdo.peso,
                        galpon.numero 
                        FROM
                            raza
                            INNER JOIN cerdo ON raza.id_raza = cerdo.raza
                            INNER JOIN galpon_cerdo ON cerdo.id_cerdo = galpon_cerdo.id_cerdo
                            INNER JOIN galpon ON galpon_cerdo.id_galpon = galpon.id_galpon 
                        WHERE
                        cerdo.estado = 1 
                        AND cerdo.raza = '{0}' """.format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listar todos los cerdo
    def Cerdos_full():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        cerdo.codigo,
                        cerdo.nombre,
                        cerdo.sexo,
                        raza.raza,
                        cerdo.peso,
                        galpon.numero 
                        FROM
                            raza
                            INNER JOIN cerdo ON raza.id_raza = cerdo.raza
                            INNER JOIN galpon_cerdo ON cerdo.id_cerdo = galpon_cerdo.id_cerdo
                            INNER JOIN galpon ON galpon_cerdo.id_galpon = galpon.id_galpon 
                        WHERE
                        cerdo.estado = 1""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
  
    ######################### COMPRAS VACUNAS

    #modelo para listar la compra de la vacuns
    def Listar_compra_vacuna(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_vacuna.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon) AS proveedor,
                            proveedor.ruc,
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
                            INNER JOIN proveedor ON compra_vacuna.proveedor_id = proveedor.id WHERE compra_vacuna.id='{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer el detalle de la compra
    def Detalle_compra_vacuna(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            detalle_compra_vacuna.compra_vacuna_id,
                            vacuna.codigo,
                            vacuna.nombre,
                            detalle_compra_vacuna.precio,
                            detalle_compra_vacuna.cantidad,
                            detalle_compra_vacuna.descuento,
                            detalle_compra_vacuna.total,
                            detalle_compra_vacuna.estado 
                        FROM
                            detalle_compra_vacuna
                            INNER JOIN vacuna ON detalle_compra_vacuna.vacuna_id = vacuna.id 
                        WHERE
                            detalle_compra_vacuna.compra_vacuna_id = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    ######################### VACUNACION DEL CERDO

    #modelo para listar la vacunacion del cerdo
    def vacunacion_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        vacunacion.id,
                        concat_ws(' ',  cerdo.codigo, ' - ',
                        cerdo.sexo, ' - ',
                        raza.raza) as cerdo,
                        vacunacion.fecha,
                        vacunacion.observacion,
                        vacunacion.estado 
                        FROM
                        vacunacion
                        INNER JOIN cerdo ON vacunacion.cerdo_id = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE vacunacion.id='{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer el detalle de la vacunacion
    def Detalle_vacunacion_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS( ' ', vacuna.nombre, ' - ', tipo_vacuna.tipo_vacuna ) AS vacuna,
                        detalle_vacunacion.cantidad,
                        detalle_vacunacion.motivo 
                    FROM
                        detalle_vacunacion
                        INNER JOIN vacuna ON detalle_vacunacion.vacuna_id = vacuna.id
                        INNER JOIN tipo_vacuna ON vacuna.tipo_id = tipo_vacuna.id 
                    WHERE
                        detalle_vacunacion.vacunacion_id='{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    ######################### DESPARASITACION DEL CERDO

    #modelo para listar la desparasitacion del cerdo
    def desparasitacion_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        desparasitacion.id,
                        concat_ws(' ',  cerdo.codigo, ' - ',
                        cerdo.sexo, ' - ',
                        raza.raza) as cerdo,
                        desparasitacion.fecha,
                        desparasitacion.observacion,
                        desparasitacion.estado 
                        FROM
                        desparasitacion
                        INNER JOIN cerdo ON desparasitacion.cerdo_id = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE desparasitacion.id='{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer el detalle de la desparasitacion
    def Detalle_desparasitacion_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS( ' ', medicamento.nombre, ' - ', tipo_medicamento.tipo ) AS medicina,
                        detalle_desparasitacion.cantidad,
                        detalle_desparasitacion.motivo 
                        FROM
                            detalle_desparasitacion
                            INNER JOIN medicamento ON detalle_desparasitacion.medicina_id = medicamento.id
                            INNER JOIN tipo_medicamento ON medicamento.tipo_id = tipo_medicamento.id 
                        WHERE
                        detalle_desparasitacion.desparasitacion_id='{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
     ######################### INFORME DE CERDOS COSTO DE PRODUCCION

    def Listar_cerdo_reporte(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            cerdo.codigo,
                            cerdo.nombre,
                            cerdo.sexo,
                            raza.raza,
                            cerdo.peso,
                            cerdo.etapa,
                            cerdo.costo,
                            cerdo.id_cerdo,
                            cerdo.tipo_ingreso
                        FROM
                            raza
                            INNER JOIN cerdo ON raza.id_raza = cerdo.raza 
                        WHERE
                            cerdo.id_cerdo='{0}'""".format(id))
            data = query.fetchone()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Semanas_alimento(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            CONCAT_WS(' ', 'Costo de alimentación semana', alimentacion.semana) as semana, 
                            ROUND(SUM(( alimento.precio / alimento.peso ) * alimentacion.cantidad), 2) AS total
                        FROM
                            alimentacion
                            INNER JOIN
                            alimento
                            ON 
                                alimentacion.alimento_id = alimento.id
                        WHERE
                            alimentacion.id_cerdo='{0}'
                        GROUP BY
                            alimentacion.semana 	
                        ORDER BY alimentacion.semana asc""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Semanas_vacunas(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS(' ', 'Costo de vacuna semana', vacunacion.semana) as semana,  
                        ROUND(SUM(( vacuna.precio / vacuna.cantidad_dosis ) * vacunacion.dosis), 2) AS total
                    FROM
                        vacunacion
                        INNER JOIN
                        vacuna
                        ON 
                            vacunacion.vacuna_id = vacuna.id WHERE vacunacion.cerdo_id='{0}'
                            GROUP BY
                        vacunacion.semana 	
                    ORDER BY vacunacion.semana asc""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Semanas_desparasitar(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                    CONCAT_WS(' ', 'Costo de desparasitación semana', desparasitacion.semana) AS semana, 
                    ROUND(SUM(( medicamento.precio / medicamento.unidades ) * desparasitacion.cantidad), 2) AS total
                FROM
                    desparasitacion
                    INNER JOIN
                    medicamento
                    ON 
                        desparasitacion.medicamento_id = medicamento.id
                WHERE
                    desparasitacion.cerdo_id='{0}'
                GROUP BY
                    desparasitacion.semana
                ORDER BY
                    desparasitacion.semana ASC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Lote_medicamento_todo():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_medicamento.codigo,
                            medicamento.nombre,
                            tipo_medicamento.tipo,
                            lote_medicamento.cantidad,
                            lote_medicamento.fecha_i,
                            lote_medicamento.fecha_f,
                            medicamento.presentacion 
                        FROM
                            lote_medicamento
                            INNER JOIN medicamento ON lote_medicamento.medicamento_id = medicamento.id
                            INNER JOIN tipo_medicamento ON medicamento.tipo_id = tipo_medicamento.id 
                        ORDER BY
                            lote_medicamento.fecha_f ASC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Lote_medicamento_tipo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_medicamento.codigo,
                            medicamento.nombre,
                            tipo_medicamento.tipo,
                            lote_medicamento.cantidad,
                            lote_medicamento.fecha_i,
                            lote_medicamento.fecha_f,
                            medicamento.presentacion 
                        FROM
                            lote_medicamento
                            INNER JOIN medicamento ON lote_medicamento.medicamento_id = medicamento.id
                            INNER JOIN tipo_medicamento ON medicamento.tipo_id = tipo_medicamento.id 
                            WHERE tipo_medicamento.id="{0}"
                        ORDER BY
                            lote_medicamento.fecha_f ASC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Lote_insumos_todo():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_insumo.codigo,
                            insumo.codigo,
                            tipo_insumo.tipo,
                            lote_insumo.cantidad,
                            lote_insumo.fecha_i,
                            lote_insumo.fecha_f 
                        FROM
                            lote_insumo
                            INNER JOIN insumo ON lote_insumo.insumo_id = insumo.id
                            INNER JOIN tipo_insumo ON insumo.tipo_id = tipo_insumo.id 
                        ORDER BY
                            lote_insumo.fecha_f ASC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Lote_insumo_tipo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_insumo.codigo,
                        insumo.codigo,
                        tipo_insumo.tipo,
                        lote_insumo.cantidad,
                        lote_insumo.fecha_i,
                        lote_insumo.fecha_f 
                    FROM
                        lote_insumo
                        INNER JOIN insumo ON lote_insumo.insumo_id = insumo.id
                        INNER JOIN tipo_insumo ON insumo.tipo_id = tipo_insumo.id 
                        WHERE 	tipo_insumo.id = '{0}'
                    ORDER BY
                        lote_insumo.fecha_f ASC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Lote_alimento_todo():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_alimento.codigo,
                            alimento.nombre,
                            tipo_alimento.tipo_alimento,
                            lote_alimento.cantidad,
                            lote_alimento.fecha_i,
                            lote_alimento.fecha_f 
                        FROM
                            lote_alimento
                            INNER JOIN alimento ON lote_alimento.alimento_id = alimento.id
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id 
                        ORDER BY
                            lote_alimento.fecha_f ASC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Lote_alimento_tipo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            lote_alimento.codigo,
                            alimento.nombre,
                            tipo_alimento.tipo_alimento,
                            lote_alimento.cantidad,
                            lote_alimento.fecha_i,
                            lote_alimento.fecha_f 
                        FROM
                            lote_alimento
                            INNER JOIN alimento ON lote_alimento.alimento_id = alimento.id
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id 
                            WHERE tipo_alimento.id = '{0}'
                        ORDER BY
                            lote_alimento.fecha_f ASC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Lote_vacuna_todo():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_vacuna.codigo,
                        vacuna.nombre,
                        tipo_vacuna.tipo_vacuna,
                        lote_vacuna.cantidad,
                        lote_vacuna.fecha_i,
                        lote_vacuna.fecha_f 
                    FROM
                        lote_vacuna
                        INNER JOIN vacuna ON lote_vacuna.vacuna_id = vacuna.id
                        INNER JOIN tipo_vacuna ON tipo_vacuna.id = vacuna.tipo_id 
                    ORDER BY
                        lote_vacuna.fecha_f ASC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Lote_vacuna_tipo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        lote_vacuna.codigo,
                        vacuna.nombre,
                        tipo_vacuna.tipo_vacuna,
                        lote_vacuna.cantidad,
                        lote_vacuna.fecha_i,
                        lote_vacuna.fecha_f 
                    FROM
                        lote_vacuna
                        INNER JOIN vacuna ON lote_vacuna.vacuna_id = vacuna.id
                        INNER JOIN tipo_vacuna ON tipo_vacuna.id = vacuna.tipo_id 
                        WHERE tipo_vacuna.id = '{0}'
                    ORDER BY
                        lote_vacuna.fecha_f ASC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Cerdos_disponibes():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            cerdo.codigo, 
                            cerdo.sexo, 
                            raza.raza, 
                            cerdo.peso, 
                            cerdo.etapa, 
                            cerdo.costo, 
                            cerdo.tipo_ingreso, 
                            raza.id_raza
                        FROM
                            cerdo
                            INNER JOIN
                            raza
                            ON 
                                cerdo.raza = raza.id_raza WHERE cerdo.estado = 1""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0 
    
    def Cerdos_disponibes_raza(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            cerdo.codigo, 
                            cerdo.sexo, 
                            raza.raza, 
                            cerdo.peso, 
                            cerdo.etapa, 
                            cerdo.costo, 
                            cerdo.tipo_ingreso, 
                            raza.id_raza
                        FROM
                            cerdo
                            INNER JOIN
                            raza
                            ON 
                                cerdo.raza = raza.id_raza WHERE raza.id_raza='{0}' AND cerdo.estado = 1""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0 

    ######################### INFORME DE CERDOS POR GALPON

    def Listar_galpon_cerdo(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            cerdo.codigo,
                            cerdo.sexo,
                            raza.raza,
                            cerdo.peso,
                            cerdo.etapa,
                            cerdo.costo,
                            cerdo.tipo_ingreso,
                            raza.id_raza,
                            detallegalpon_cerdo.id_galpon 
                        FROM
                            cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza
                            INNER JOIN detallegalpon_cerdo ON cerdo.id_cerdo = detallegalpon_cerdo.id_cerdo 
                        WHERE
                            detallegalpon_cerdo.id_galpon = '{0}' AND cerdo.estado = 1""". format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    def Galpon_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            galpon_cerdo_new.id,
                            galpon.numero,
                            tipo_galpon.tipo_galpon,
                            galpon_cerdo_new.fecha_i,
                            galpon_cerdo_new.fecha_f,
                            galpon_cerdo_new.semana,
                            galpon_cerdo_new.estado 
                        FROM
                            galpon_cerdo_new
                            INNER JOIN galpon ON galpon_cerdo_new.id_galpon = galpon.id_galpon
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo 
                        WHERE galpon_cerdo_new.id = '{0}'""".format(id))
            data = query.fetchone()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ##################### INFORME DE VACUNACION DEL LOS CERDOS 
    
    def Informe_vacunas_cerdos_semana(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            DATE( vacunacion.fecha ),
                            TIME( vacunacion.fecha ),
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
                            vacunacion.fecha DESC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ##################### INFORME DE DESPARASITANTES DEL LOS CERDOS 
    
    def Informe_desparasitantes_cerdos_semana(id):       
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
                            desparasitacion.fecha DESC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ##################### INFORME DE ALIMENTACION DEL LOS CERDOS 
    
    def Informe_alimntacion_cerdo(id):   
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            alimentacion.fecha,
                            TIME(alimentacion.fecha) AS hora,
                            alimentacion.semana,
                            alimento.nombre,
                            tipo_alimento.tipo_alimento,
                            tipo_alimentcion.tipo,
                            alimentacion.cantidad
                        FROM
                            alimentacion
                            INNER JOIN alimento ON alimentacion.alimento_id = alimento.id
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN tipo_alimentcion ON alimentacion.tipo_id = tipo_alimentcion.id 
                        WHERE
                            alimentacion.id_cerdo = '{0}' 
                        ORDER BY
                            alimentacion.fecha ASC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0    

    ##################### INFORME DE ENFERMEDADES DEL LOS CERDOS 
    
    def Informe_enfermedades_cerdo(id):   
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        enfermedad_cerdo.cerdo_id,
                        enfermedad_cerdo.fecha,
                        detalle_enfermedad_cerdo.enfermedad_id,
                        enfermedad.nombre,
                        enfermedad_cerdo.estado AS espera 
                    FROM
                        enfermedad_cerdo
                        INNER JOIN detalle_enfermedad_cerdo ON enfermedad_cerdo.id = detalle_enfermedad_cerdo.cerdo_enfermedad_id
                        INNER JOIN enfermedad ON enfermedad.id = detalle_enfermedad_cerdo.enfermedad_id 
                    WHERE
                        enfermedad_cerdo.cerdo_id = '{0}' 
                    ORDER BY
                        enfermedad_cerdo.fecha ASC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0   

    ##################### INFORME DE TRATAMIENTOS DEL LOS CERDOS 
    
    def Informe_tratamientos_cerdo(id):   
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        enfermedad_cerdo.cerdo_id,
                        tipo_tratamiento.nombre,
                        tratamiento_cerdos.fecha_i,
                        tratamiento_cerdos.fecha_f,
                        tratamiento_cerdos.peso,
                        tratamiento_cerdos.fecha 
                    FROM
                        tipo_tratamiento
                        INNER JOIN detalle_enfermedad_tratmiento ON tipo_tratamiento.id = detalle_enfermedad_tratmiento.tipo_id
                        INNER JOIN tratamiento_cerdos ON tratamiento_cerdos.id = detalle_enfermedad_tratmiento.tratamiento_id
                        INNER JOIN enfermedad_cerdo ON tratamiento_cerdos.enfer_cerdo_id = enfermedad_cerdo.id
                        WHERE enfermedad_cerdo.cerdo_id = '{0}'
                        ORDER BY tratamiento_cerdos.fecha DESC""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0 
    
    ##################### INFORME DE MUERTES DE CERDOS 
    
    def Informe_cerdo_muertos():   
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS( ' ', muertes.fecha, muertes.hora ) AS FEHA_HORA,
                        muertes.semana,
                         CONCAT_WS( ' ',cerdo.codigo,
                        cerdo.sexo,
                        raza.raza ) AS CERDO, 
                        cerdo.peso	
                    FROM
                        muertes
                        INNER JOIN cerdo ON muertes.id_cerdo = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                    ORDER BY
                        muertes.f_registro DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0  
    
    def Informe_cerdo_muertos_fecha(f_i, f_f): 
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS( ' ', muertes.fecha, muertes.hora ) AS FEHA_HORA,
                        muertes.semana,
                         CONCAT_WS( ' ',cerdo.codigo,
                        cerdo.sexo,
                        raza.raza ) AS CERDO, 
                        cerdo.peso	
                    FROM
                        muertes
                        INNER JOIN cerdo ON muertes.id_cerdo = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                        WHERE muertes.fecha BETWEEN '{0}' AND '{1}'
                    ORDER BY
                        muertes.f_registro DESC""".format(f_i, f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0  

    def Detalle_costo_produccion_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""CALL costro_produccion_cerdo({0})""".format(id))
            data = query.fetchone()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0 

    def Listar_ventas_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
	                venta_cerdos.id,
                    CONCAT_WS( ' ', cliente.nombres, cliente.apellidos ) AS cliente,
                    cliente.cedula,
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
                WHERE venta_cerdos.id = '{0}'""".format(id))
            data = query.fetchone()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Detalle_venta_cerdos(id):
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

    def Informe_ventas_cerdos(f_i, f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT 
                    venta_cerdos.fecha,
                    venta_cerdos.numero_venta, 
                    venta_cerdos.iva,
                    venta_cerdos.subtotal,
                    venta_cerdos.impuesto,
                    venta_cerdos.total,
                    venta_cerdos.estado 
                FROM
                    venta_cerdos
                    INNER JOIN cliente ON venta_cerdos.cliente_id = cliente.id 
                WHERE venta_cerdos.estado = 1 
                AND DATE(venta_cerdos.fecha) BETWEEN '{0}' AND '{1}'""".format(f_i, f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    def Informe_cerdos_vendidos(f_i, f_f):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        venta_cerdos.fecha,
                        venta_cerdos.numero_venta,
                        raza.raza,
                        cerdo.sexo,
                        detalle_venta_cerdos.peso,
                        detalle_venta_cerdos.precio,
                        detalle_venta_cerdos.total 
                    FROM
                        detalle_venta_cerdos
                        INNER JOIN venta_cerdos ON detalle_venta_cerdos.id_venta = venta_cerdos.id
                        INNER JOIN cerdo ON detalle_venta_cerdos.id_cerdo = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                    WHERE
                        venta_cerdos.estado = 1 AND DATE(venta_cerdos.fecha) BETWEEN '{0}' AND '{1}'
                    ORDER BY
                        venta_cerdos.fecha ASC""".format(f_i, f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Listado_pedidos_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        pedidos_cerdo.id,
                        pedidos_cerdo.numero_pedido,
                        CONCAT_WS( ' ', pedidos_cerdo.nombre, pedidos_cerdo.apellido ) AS cliente,
                        pedidos_cerdo.telefono,
                        pedidos_cerdo.correo,
                        pedidos_cerdo.direccion,
                        pedidos_cerdo.subtotal,
                        pedidos_cerdo.impuesto,
                        pedidos_cerdo.total,
                        pedidos_cerdo.iva,
                        DATE( pedidos_cerdo.fecha_pedido ),
                        pedidos_cerdo.estado,
                        pedidos_cerdo.cedula
                    FROM
                        pedidos_cerdo 
                    WHERE pedidos_cerdo.id = '{0}'""".format(id))
            data = query.fetchone()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Detalle_pedidos_cerdos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                    CONCAT_WS( ' ', cerdo.codigo, cerdo.sexo, raza.raza ) AS cerdo,
                    detalle_pedido_cerdo.peso,
                    detalle_pedido_cerdo.precio,
                    detalle_pedido_cerdo.total,
                    detalle_pedido_cerdo.id_pedido 
                    FROM
                    cerdo
                    INNER JOIN raza ON cerdo.raza = raza.id_raza
                    INNER JOIN detalle_pedido_cerdo ON cerdo.id_cerdo = detalle_pedido_cerdo.id_cerdo
                    WHERE detalle_pedido_cerdo.id_pedido = '{0}'""".format(id))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Informe_pedidos_cerdos(f_i, f_f, estado):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        pedidos_cerdo.id,
                        pedidos_cerdo.numero_pedido, 
                        pedidos_cerdo.subtotal,
                        pedidos_cerdo.impuesto,
                        pedidos_cerdo.total,
                        pedidos_cerdo.iva,
                        DATE( pedidos_cerdo.fecha_pedido ),
                        pedidos_cerdo.estado
                    FROM
                        pedidos_cerdo 
                    WHERE pedidos_cerdo.estado = '{0}' 
                    AND DATE( pedidos_cerdo.fecha_pedido ) BETWEEN '{1}' AND '{2}'""".format(estado, f_i, f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    def Informe_cerdos_pedidos(f_i, f_f, estado):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS( ' ', raza.raza, cerdo.sexo ) AS cerdo,
                        detalle_pedido_cerdo.peso,
                        detalle_pedido_cerdo.precio,
                        detalle_pedido_cerdo.total,  
                        DATE( pedidos_cerdo.fecha_pedido ),
                        pedidos_cerdo.numero_pedido 
                    FROM
                        cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza
                        INNER JOIN detalle_pedido_cerdo ON cerdo.id_cerdo = detalle_pedido_cerdo.id_cerdo
                        INNER JOIN pedidos_cerdo ON detalle_pedido_cerdo.id_pedido = pedidos_cerdo.id 
                    WHERE
                        pedidos_cerdo.estado = '{0}' 
                        AND DATE( pedidos_cerdo.fecha_pedido ) BETWEEN '{1}' 
                        AND '{2}'""".format(estado, f_i, f_f))
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0