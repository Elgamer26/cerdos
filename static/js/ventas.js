var tabla_cliente;

function registra_cliente() {
    var nombres = $("#nombres_cli").val();
    var apellidos = $("#apellidos_cli").val();
    var domicilio = $("#domicilio_cli").val();
    var telefono = $("#telefono_cli").val();
    var cedula = $("#cedula_clie").val();
    var correo = $("#correo_cli").val();

    if (
        nombres.length == 0 ||
        nombres.trim() == "" ||
        apellidos.length == 0 ||
        apellidos.trim() == "" ||
        domicilio.length == 0 ||
        domicilio.trim() == "" ||
        telefono.length == 0 ||
        telefono.trim() == "" ||
        correo.length == 0 ||
        correo.trim() == "" ||
        cedula.length == 0 ||
        cedula.trim() == ""
    ) {
        validar_registros_cliente(
            nombres,
            apellidos,
            domicilio,
            telefono,
            correo,
            cedula
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#nombre_cli_oblig").html("");
        $("#apellidos_cli_obligg").html("");
        $("#domicilio_cli_obligg").html("");
        $("#telefono_cli_obligg").html("");
        $("#correo_cli_obligg").html("");
        $("#cedula_clie_obligg").html("");
    }

    if (!G_correo_create_cli) {
        $("#correo_cli_obligg").html("Ingrese un correo correcto");
        return swal.fire(
            "Correo incorrecto",
            "Ingrese un correo correcto",
            "warning"
        );
    } else {
        $("#correo_cli_obligg").html("");
    }

    $.ajax({
        type: "POST",
        url: "/venta/registro_cliente",
        data: { nombres: nombres, apellidos: apellidos, domicilio: domicilio, telefono: telefono, cedula: cedula, correo: correo },
        success: function (response) {
            if (response == 1) {
                cargar_contenido('contenido_principal', '/cliente');
                return Swal.fire(
                    "Cliente registrado",
                    "Clienre registrado con éxito",
                    "success"
                );
            } else if (response == 2) {
                $(".card-success").LoadingOverlay("hide");
                return Swal.fire(
                    "Cédua ya existe",
                    "La cédula " + cedula + ", ya existe en el sistema",
                    "warning"
                );
            } else {
                $(".card-success").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "E ciente no fue registrado en el sistema",
                    "error"
                );
            }
        },

        beforeSend: function () {
            $(".card-success").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
}

function validar_registros_cliente(
    nombres,
    apellidos,
    domicilio,
    telefono,
    correo,
    cedula
) {
    if (nombres.length == 0 || nombres.trim() == "") {
        $("#nombre_cli_oblig").html("Ingrese los nombres");
    } else {
        $("#nombre_cli_oblig").html("");
    }

    if (apellidos.length == 0 || apellidos.trim() == "") {
        $("#apellidos_cli_obligg").html("Ingrese los apellidos");
    } else {
        $("#apellidos_cli_obligg").html("");
    }

    if (domicilio.length == 0 || domicilio.trim() == "") {
        $("#domicilio_cli_obligg").html("Ingrese el domicilio");
    } else {
        $("#domicilio_cli_obligg").html("");
    }

    if (telefono.length == 0 || telefono.trim() == "") {
        $("#telefono_cli_obligg").html("Ingrese el teléfono");
    } else {
        $("#telefono_cli_obligg").html("");
    }

    if (correo.length == 0 || correo.trim() == "") {
        $("#correo_cli_obligg").html("Ingrese el correo");
    } else {
        $("#correo_cli_obligg").html("");
    }

    if (cedula.length == 0 || cedula.trim() == "") {
        $("#cedula_clie_obligg").html("Ingrese la cédula");
    } else {
        $("#cedula_clie_obligg").html("");
    }
}

function listado_clientes() {
    tabla_cliente = $("#tabla_cliente_").DataTable({
        ordering: true,
        paging: true,
        aProcessing: true,
        aServerSide: true,
        searching: { regex: true },
        lengthMenu: [
            [10, 25, 50, 100, -1],
            [10, 25, 50, 100, "All"],
        ],
        pageLength: 10,
        destroy: true,
        async: false,
        processing: true,

        ajax: {
            url: "/venta/listar_cliente",
            type: "GET",
        },
        //hay que poner la misma cantidad de columnas y tambien en el html
        columns: [
            { defaultContent: "" },
            {
                data: "estado",
                render: function (data, type, row) {
                    if (data == 1) {
                        return `<button style='font-size:10px;' type='button' class='inactivar btn btn-outline-danger' title='Inactivar el cliente'><i class='fa fa-times' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='editar btn btn-outline-primary' title='Editar el cliente'><i class='fa fa-edit' style='font-size: 15px;'></i></button>`;
                    } else {
                        return `<button style='font-size:10px;' type='button' class='activar btn btn-outline-success' title='Activar el cliente'><i class='fa fa-check' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='editar btn btn-outline-primary' title='Editar el cliente'><i class='fa fa-edit' style='font-size: 15px;'></i></button>`;
                    }
                },
            },
            { data: "nombres" },
            { data: "apellidos" },
            { data: "cedula" },
            { data: "correo" },
            { data: "domicilio" },
            { data: "telefono" },
            {
                data: "estado",
                render: function (data, type, row) {
                    if (data == 1) {
                        return "<span class='badge badge-success'>ACTIVO</span>";
                    } else {
                        return "<span class='badge badge-danger'>INACTIVO</span>";
                    }
                },
            },
        ],

        language: {
            rows: "%d fila seleccionada",
            processing: "Tratamiento en curso...",
            search: "Buscar&nbsp;:",
            lengthMenu: "Agrupar en _MENU_ items",
            info: "Mostrando los item (_START_ al _END_) de un total _TOTAL_ items",
            infoEmpty: "No existe datos.",
            infoFiltered: "(filtrado de _MAX_ elementos en total)",
            infoPostFix: "",
            loadingRecords: "Cargando...",
            zeroRecords: "No se encontro resultados en tu busqueda",
            emptyTable: "No hay datos disponibles en la tabla",
            paginate: {
                first: "Primero",
                previous: "Anterior",
                next: "Siguiente",
                last: "Ultimo",
            },
            select: {
                rows: "%d fila seleccionada",
            },
            aria: {
                sortAscending: ": active para ordenar la columa en orden ascendente",
                sortDescending: ": active para ordenar la columna en orden descendente",
            },
        },
        select: true,
        responsive: "true",
    });

    //esto es para crearn un contador para la tabla este contador es automatico
    tabla_cliente.on("draw.dt", function () {
        var pageinfo = $("#tabla_cliente_").DataTable().page.info();
        tabla_cliente
            .column(0, { page: "current" })
            .nodes()
            .each(function (cell, i) {
                cell.innerHTML = i + 1 + pageinfo.start;
            });
    });
}

$("#tabla_cliente_").on("click", ".inactivar", function () {
    //esto esta extrayendo los datos de la tabla el (data)
    var data = tabla_cliente.row($(this).parents("tr")).data(); //a que fila deteta que doy click
    //esta condicion es importante para el responsibe porque salda un error si no lo pongo
    if (tabla_cliente.row(this).child.isShown()) {
        //esto es cuando esta en tamaño responsibo
        var data = tabla_cliente.row(this).data();
    }
    var dato = 0;
    var id = data.id;

    Swal.fire({
        title: "Cambiar estado?",
        text: "El estado del cliente se cambiará!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, cambiar!",
    }).then((result) => {
        if (result.isConfirmed) {
            cambiar_estado_cliente(id, dato);
        }
    });
});

$("#tabla_cliente_").on("click", ".activar", function () {
    //esto esta extrayendo los datos de la tabla el (data)
    var data = tabla_cliente.row($(this).parents("tr")).data(); //a que fila deteta que doy click
    //esta condicion es importante para el responsibe porque salda un error si no lo pongo
    if (tabla_cliente.row(this).child.isShown()) {
        //esto es cuando esta en tamaño responsibo
        var data = tabla_cliente.row(this).data();
    }
    var dato = 1;
    var id = data.id;

    Swal.fire({
        title: "Cambiar estado?",
        text: "El estado del cliente se cambiará!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, cambiar!",
    }).then((result) => {
        if (result.isConfirmed) {
            cambiar_estado_cliente(id, dato);
        }
    });
});

function cambiar_estado_cliente(id, dato) {
    var res = "";
    if (dato == 1) {
        res = "activo";
    } else {
        res = "inactivo";
    }

    $.ajax({
        url: "/venta/cambiar_estado_cliente",
        type: "POST",
        data: { id: id, dato: dato },
    }).done(function (response) {
        if (response > 0) {
            if (response == 1) {
                tabla_cliente.ajax.reload();
                return Swal.fire(
                    "Estado de cliente",
                    "EL estado se " + res + " con éxtio",
                    "success"
                );
            }
        } else {
            return Swal.fire(
                "Estado de cliente",
                "No se pudo cambiar el estado, error en la matrix",
                "error"
            );
        }
    });
}

$("#tabla_cliente_").on("click", ".editar", function () {
    //esto esta extrayendo los datos de la tabla el (data)
    var data = tabla_cliente.row($(this).parents("tr")).data(); //a que fila deteta que doy click
    //esta condicion es importante para el responsibe porque salda un error si no lo pongo
    if (tabla_cliente.row(this).child.isShown()) {
        //esto es cuando esta en tamaño responsibo
        var data = tabla_cliente.row(this).data();
    }

    $("#id_cliente").val(data.id);
    $("#nombres_cli").val(data.nombres);
    $("#apellidos_cli").val(data.apellidos);
    $("#domicilio_cli").val(data.domicilio);
    $("#telefono_cli").val(data.telefono);
    $("#cedula_clie").val(data.cedula);
    $("#correo_cli").val(data.correo);

    $("#correo_cli").css("border", "1px solid green");

    $("#nombre_cli_oblig").html("");
    $("#apellidos_cli_obligg").html("");
    $("#domicilio_cli_obligg").html("");
    $("#telefono_cli_obligg").html("");
    $("#correo_cli_obligg").html("");
    $("#cedula_clie_obligg").html("");

    $("#modaleditar_cliente").modal({ backdrop: "static", keyboard: false });
    $("#modaleditar_cliente").modal("show");
});

function editar_cliente() {
    var id = $("#id_cliente").val();
    var nombres = $("#nombres_cli").val();
    var apellidos = $("#apellidos_cli").val();
    var domicilio = $("#domicilio_cli").val();
    var telefono = $("#telefono_cli").val();
    var cedula = $("#cedula_clie").val();
    var correo = $("#correo_cli").val();

    if (
        nombres.length == 0 ||
        nombres.trim() == "" ||
        apellidos.length == 0 ||
        apellidos.trim() == "" ||
        domicilio.length == 0 ||
        domicilio.trim() == "" ||
        telefono.length == 0 ||
        telefono.trim() == "" ||
        correo.length == 0 ||
        correo.trim() == "" ||
        cedula.length == 0 ||
        cedula.trim() == ""
    ) {
        validar_editar_cliente(
            nombres,
            apellidos,
            domicilio,
            telefono,
            correo,
            cedula
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#nombre_cli_oblig").html("");
        $("#apellidos_cli_obligg").html("");
        $("#domicilio_cli_obligg").html("");
        $("#telefono_cli_obligg").html("");
        $("#correo_cli_obligg").html("");
        $("#cedula_clie_obligg").html("");
    }

    if (!G_correo_editar_cli) {
        $("#correo_cli_obligg").html("Ingrese un correo correcto");
        return swal.fire(
            "Correo incorrecto",
            "Ingrese un correo correcto",
            "warning"
        );
    } else {
        $("#correo_cli_obligg").html("");
    }

    $.ajax({
        type: "POST",
        url: "/venta/editar_cliente",
        data: { nombres: nombres, apellidos: apellidos, domicilio: domicilio, telefono: telefono, cedula: cedula, correo: correo, id: id },
        success: function (response) {
            if (response == 1) {
                tabla_cliente.ajax.reload();
                $("#modaleditar_cliente").modal("hide");
                return Swal.fire(
                    "Cliente editado",
                    "Clienre editado con éxito",
                    "success"
                );
            } else if (response == 2) {
                $(".card-success").LoadingOverlay("hide");
                return Swal.fire(
                    "Cédua ya existe",
                    "La cédula " + cedula + ", ya existe en el sistema",
                    "warning"
                );
            } else {
                $(".card-success").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "E ciente no fue editado en el sistema",
                    "error"
                );
            }
        },

        beforeSend: function () {
            $(".card-success").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
}

function validar_editar_cliente(
    nombres,
    apellidos,
    domicilio,
    telefono,
    correo,
    cedula
) {
    if (nombres.length == 0 || nombres.trim() == "") {
        $("#nombre_cli_oblig").html("Ingrese los nombres");
    } else {
        $("#nombre_cli_oblig").html("");
    }

    if (apellidos.length == 0 || apellidos.trim() == "") {
        $("#apellidos_cli_obligg").html("Ingrese los apellidos");
    } else {
        $("#apellidos_cli_obligg").html("");
    }

    if (domicilio.length == 0 || domicilio.trim() == "") {
        $("#domicilio_cli_obligg").html("Ingrese el domicilio");
    } else {
        $("#domicilio_cli_obligg").html("");
    }

    if (telefono.length == 0 || telefono.trim() == "") {
        $("#telefono_cli_obligg").html("Ingrese el teléfono");
    } else {
        $("#telefono_cli_obligg").html("");
    }

    if (correo.length == 0 || correo.trim() == "") {
        $("#correo_cli_obligg").html("Ingrese el correo");
    } else {
        $("#correo_cli_obligg").html("");
    }

    if (cedula.length == 0 || cedula.trim() == "") {
        $("#cedula_clie_obligg").html("Ingrese la cédula");
    } else {
        $("#cedula_clie_obligg").html("");
    }
}

//// VENTA DE CERDO 
function registra_venta_cerdo() {
    Swal.fire({
        title: 'Guardar venta de cerdo?',
        text: "La venta se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_venta_cerdo();
        }
    })
}

function guardar_venta_cerdo() {
    var cliente = $("#cliente").val();
    var fecha_c = $("#fecha_c").val();
    var numero_venta = $("#numero_venta").val();
    var tipo_comprobante = $("#tipo_comprobante").val();
    var iva = $("#iva").val();

    var subtotal = $("#subtotal").val();
    var impuesto_sub = $("#impuesto_sub").val();
    var total_pagar = $("#total_pagar").val();
    var count = 0;

    if (cliente == "0" ||
        numero_venta.length == 0 ||
        numero_venta.trim() == "" ||
        iva.length == 0 ||
        iva.trim() == "") {

        validar_registro_compra_medicamento(cliente, numero_venta, iva);
        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#cliente_obligg").html("");
        $("#numero_v_obligg").html("");
        $("#ivaa_obligg").html("");
    }

    $("#tabla_venta_cerdo tbody#tbody_tabla_venta_cerdo tr").each(function () {
        count++;
    }
    );

    if (count == 0) {
        $("#unir_no_hay").html('<span class="badge badge-danger"><b>.:No hay cerdos en el detalle de venta:.</b></span>');
        return swal.fire(
            "Detalle vacío",
            "No hay cerdos en el detalle de venta",
            "warning"
        );
    } else {
        $("#unir_no_hay").html("");
    }

    var formdata = new FormData();
    formdata.append("cliente", cliente);
    formdata.append("fecha_c", fecha_c);
    formdata.append("numero_venta", numero_venta);
    formdata.append("tipo_comprobante", tipo_comprobante);
    formdata.append("iva", iva);
    formdata.append("subtotal", subtotal);
    formdata.append("impuesto_sub", impuesto_sub);
    formdata.append("total_pagar", total_pagar);

    $.ajax({
        url: "/venta/registra_veenta_cerdos",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {
            if (resp > 0) {
                if (resp != 2) {
                    guardar_detalle_venta_cerdos(parseInt(resp));
                } else {
                    $(".card-success").LoadingOverlay("hide");
                    return Swal.fire(
                        "Número de venta ya existe",
                        "El número de venta: '" + numero_venta + "', ya existe en el sistema",
                        "warning"
                    );
                }

            } else {

                $(".card-success").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo crear la compra, falla en la matrix",
                    "error"
                );
            }
        },

        beforeSend: function () {
            $(".card-success").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function validar_registro_compra_medicamento(cliente, numero_venta, iva) {
    if (cliente == "0") {
        $("#cliente_obligg").html("Seleccione el cliente");
    } else {
        $("#cliente_obligg").html("");
    }

    if (numero_venta.length == 0 || numero_venta.trim() == "") {
        $("#numero_v_obligg").html("Ingrese número venta");
    } else {
        $("#numero_v_obligg").html("");
    }

    if (iva.length == 0 || iva.trim() == "") {
        $("#ivaa_obligg").html("Ingrese el iva");
    } else {
        $("#ivaa_obligg").html("");
    }
}

function guardar_detalle_venta_cerdos(id) {
    var count = 0;
    var arrego_idcerdo = new Array();
    var arreglo_peso = new Array();
    var arreglo_precio = new Array();
    var arreglo_total = new Array();

    $("#tabla_venta_cerdo tbody#tbody_tabla_venta_cerdo tr").each(
        function () {
            arrego_idcerdo.push($(this).find("td").eq(0).text());
            arreglo_peso.push($(this).find("td").eq(3).text());
            arreglo_precio.push($(this).find("#cantida_a").val());
            arreglo_total.push($(this).find("td").eq(5).text());
            count++;
        }
    );

    //aqui combierto el arreglo a un string
    var idc = arrego_idcerdo.toString();
    var peso = arreglo_peso.toString();
    var precio = arreglo_precio.toString();
    var total = arreglo_total.toString();

    if (count == 0) {
        return false;
    }

    $.ajax({
        url: "/venta/registrar_detalle_venta_cerdo",
        type: "POST",
        async: true,
        data: {
            id: id,
            idc: idc,
            peso: peso,
            precio: precio,
            total: total,
        },
    }).done(function (resp) {
        if (resp > 0) {
            if (resp == 1) {
                Swal.fire({
                    title: "Venta realizada con éxito",
                    text: "Desea imprimir la venta??",
                    icon: "warning",
                    showCancelButton: true,
                    showConfirmButton: true,
                    allowOutsideClick: false,
                    confirmButtonColor: "#3085d6",
                    cancelButtonColor: "#d33",
                    confirmButtonText: "Si, Imprimir!!",
                }).then((result) => {
                    if (result.value) {
                        window.open("/reporte/venta_cerdos_factura/" + parseInt(id) + "#zoom=100%", "Reporte de venta", "scrollbards=No");
                        cargar_contenido('contenido_principal', '/venta_cerdos');
                    }
                });
                cargar_contenido('contenido_principal', '/venta_cerdos');
            }
        } else {

            return Swal.fire(
                "Error",
                "No se pudo crear el detalle de venta, falla en la matrix" + resp,
                "error"
            );

        }
    });
}

function anular_venta_cerdos(id) {
    Swal.fire({
        title: "Anular la venta de cerdo?",
        text: "La venta se anulará!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, anular!",
    }).then((result) => {
        if (result.isConfirmed) {
            venta_cerdo_anular(id);
        }
    });
}

function venta_cerdo_anular(id) {
    $.ajax({
        url: "/venta/venta_cerdo_anular",
        type: "POST",
        data: { id: id },
    }).done(function (response) {
        if (response > 0) {
            if (response == 1) {
                cargar_contenido('contenido_principal', '/venta_cerdos');
                return Swal.fire(
                    "Venta de cerdo anulada",
                    "La venta se anulo con éxtio",
                    "success"
                );
            }
        } else {
            return Swal.fire(
                "Error",
                "No se pudo anular la venta, error en la matrix",
                "error"
            );
        }
    });
}

//// envio de correo
function envio_correo(id) {
    alertify.warning('Enviando factura de venta al correo del cliente');
    $.ajax({
        url: "/venta/envio_correo_venta",
        type: "POST",
        data: { id: id },
        async: true,
    }).done(function (response) {
        console.log(response);
        if (response != 1) {
            alertify.error('Error al envio de correo');
        }
        return false;
    });
}