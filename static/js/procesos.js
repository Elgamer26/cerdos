var tabla_alimentos_c;

////////////// buscar cerdo en galpon
$("#inpu_buscar_cerdo").on("keyup", function () {
    let valor = $(this).val();
    if (valor != "" || valor.length != 0 || valor.trim() != "") {
        buscar_cerdo_galpon(valor);
    } else {
        traer_detalle_galpon_cerdo();
    }
})

///////////////// alimentacion del cerdo todo el galpon
function registrar_toda_alimentacion() {
    Swal.fire({
        title: 'Guardar alimentación de todo el galpón?',
        text: "La alimentación se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_la_alimentacion_toda();
        }
    })
}

function guardar_la_alimentacion_toda() {
    var alimento_id = $("#alimento_t").val();
    var tipo_id = $("#tipo_alimentacion_t").val();
    var fecha_c = $("#fecha_alimentaion_t").val();
    var cantidad_kg = $("#cantidad_kg_t").val();
    var observacion = $("#observacion_t").val();
    var semana = $("#semana_alimentacion_t").val();
    var disponibles_kg = $("#disponibles_kg_t").val();
    var total = $("#racion_ali").val();
    var desc = alimento_id.split(" - ");
    var count = 0;

    if (
        alimento_id.length == 0 ||
        alimento_id == "0" ||
        tipo_id.length == 0 ||
        tipo_id == "0" ||
        fecha_c.length == 0 ||
        fecha_c.trim() == "0" ||
        cantidad_kg == "0" ||
        cantidad_kg.trim() == "0" ||
        observacion.length == 0 ||
        observacion.trim() == ""
    ) {
        valida_registro_alimentacion_toda(
            alimento_id,
            tipo_id,
            fecha_c,
            cantidad_kg,
            observacion
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#alimento_t_obligg").html("");
        $("#tipo_alimentacion_t_obligg").html("");
        $("#fecha_to_obligg").html("");
        $("#cantidad_kg_t_obligg").html("");
        $("#observacion_t_obligg").html("");
    }

    if (disponibles_kg.length == 0 || disponibles_kg.trim() == "" || disponibles_kg == "0") {
        return swal.fire(
            "No hay cantidad dosponible de Kg",
            "No hay cantidad disponible de Kg",
            "warning"
        );
    }

    if (parseInt(total) > parseInt(disponibles_kg)) {
        $("#disponibles_kg_t_obligg").html("XXX");
        $("#racion_ali_obligg").html("XXX");
        return swal.fire(
            "Cantidad total supera lo disponible",
            "La cantidad total: " + total + " Kg, supera lo disponible: " + disponibles_kg + " Kg",
            "warning"
        );
    } else {
        $("#disponibles_kg_t_obligg").html("");
        $("#racion_ali_obligg").html("");
    }

    var count = 0;
    var arrego_cerdo_id = new Array();

    $("#tabla_galpo_cerdo tbody#tbody_tabla_galpo_cerdo tr").each(
        function () {
            arrego_cerdo_id.push($(this).find("td").eq(0).text());
            count++;
        }
    );

    if (count == 0) {
        return swal.fire(
            "No hay cerdos",
            "No hay cerdos dentro del galpón",
            "warning"
        );
    }

    //aqui combierto el arreglo a un string
    var id_c = arrego_cerdo_id.toString();

    var formdata = new FormData();
    formdata.append("alimento_id", desc[0]);
    formdata.append("lote_id", desc[1]);
    formdata.append("tipo_id", tipo_id);
    formdata.append("fecha_c", fecha_c);
    formdata.append("cantidad_kg", cantidad_kg);
    formdata.append("observacion", observacion);
    formdata.append("semana", semana);
    formdata.append("id_c", id_c);

    $.ajax({
        url: "/alimento/registrar_toda_alimentacion_full",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {
            if (resp > 0) {

                if (resp == 1) {
                    $("#cantidad_kg_t").val("");
                    $("#observacion_t").val("");

                    listar_alimento_t($("#tipo_alimento_t").val());
                    $("#disponibles_kg_t").val("");
                    $("#racion_ali").val("");

                    $("#modal_alimenar_todo_galpon").modal("hide");
                    $(".card_aiment_todo").LoadingOverlay("hide");
                    return Swal.fire(
                        "Alimentación exitosa",
                        "La alimentación de todo el galón se registro con exito",
                        "success"
                    );
                }

            } else {
                $(".card_aiment_todo").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo guardar el registro, falla en la matrix",
                    "error"
                );
            }
        },

        beforeSend: function () {
            $(".card_aiment_todo").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function valida_registro_alimentacion_toda(
    alimento_id,
    tipo_id,
    fecha_c,
    cantidad_kg,
    observacion
) {
    if (alimento_id.length == 0 || alimento_id == "0") {
        $("#alimento_t_obligg").html("Seleccione el alimento");
    } else {
        $("#alimento_t_obligg").html("");
    }

    if (tipo_id.length == 0 || tipo_id == "0") {
        $("#tipo_alimentacion_t_obligg").html("Seleccione el tipo alimentación");
    } else {
        $("#tipo_alimentacion_t_obligg").html("");
    }

    if (fecha_c.length == 0 || fecha_c.trim() == "") {
        $("#fecha_to_obligg").html("Ingrese la fecha");
    } else {
        $("#fecha_to_obligg").html("");
    }

    if (cantidad_kg == "0" || cantidad_kg.trim() == "") {
        $("#cantidad_kg_t_obligg").html("Ingrese la cantidad Kg");
    } else {
        $("#cantidad_kg_t_obligg").html("");
    }

    if (observacion.length == 0 || observacion.trim() == "") {
        $("#observacion_t_obligg").html("Ingrese la observación");
    } else {
        $("#observacion_t_obligg").html("");
    }
}

function guardar_detalle_alimentacion_todo(id) {
    var count = 0;
    var arrego_cerdo_id = new Array();

    $("#tabla_galpo_cerdo tbody#tbody_tabla_galpo_cerdo tr").each(
        function () {
            arrego_cerdo_id.push($(this).find("td").eq(0).text());
            count++;
        }
    );

    //aqui combierto el arreglo a un string
    var id_c = arrego_cerdo_id.toString();

    if (count == 0) {
        return false;
    }

    $.ajax({
        url: "/alimento/guardar_detalle_alimentacion_todo",
        type: "POST",
        data: {
            id: id,
            id_c: id_c
        },
    }).done(function (resp) {

        if (resp > 0) {
            if (resp == 1) {
                $("#cantidad_kg_t").val("0");
                $("#observacion_t").val("");

                listar_alimento_t($("#tipo_alimento_t").val());
                $("#disponibles_kg_t").val("");
                $("#racion_ali").val("");

                $("#modal_alimenar_todo_galpon").modal("hide");
                $(".card_aiment_todo").LoadingOverlay("hide");
                return Swal.fire(
                    "Alimentación exitosa",
                    "La alimentación de todo el galón se registro con exito",
                    "success"
                );
            }
        } else {
            $(".card_aiment_todo").LoadingOverlay("hide");
            return Swal.fire(
                "Error",
                "No se pudo crear el detalle de alimentación, falla en la matrix",
                "error"
            );

        }
    });
}

///////////////// alimentacion del cerdo unitaria
function registrar_unitaria_alimentacion() {
    Swal.fire({
        title: 'Guardar alimentación del cerdo?',
        text: "La alimentación se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_la_alimentacion_unitaria();
        }
    })
}

function guardar_la_alimentacion_unitaria() {
    var alimento_id = $("#alimento").val();
    // var alimento = $("#alimento option:selected").text();
    var tipo_id = $("#tipo_alimentacion").val();
    var fecha_c = $("#fecha_alimentaion").val();
    var cantidad_kg = $("#cantidad_kg").val();
    var observacion = $("#observacion_a_u").val();
    var semana = $("#semana_alimentacion").val();
    var disponibles_kg = $("#disponibles_kg").val();
    var desc = alimento_id.split(" - ");
    var idcerdo = $("#id_cerdo").val();

    if (
        alimento_id.length == 0 ||
        alimento_id == "0" ||
        tipo_id.length == 0 ||
        tipo_id == "0" ||
        fecha_c.length == 0 ||
        fecha_c.trim() == "0" ||
        cantidad_kg == "0" ||
        cantidad_kg.trim() == "0" ||
        observacion.length == 0 ||
        observacion.trim() == ""
    ) {
        valida_registro_alimentacion_unitaria(
            alimento_id,
            tipo_id,
            fecha_c,
            cantidad_kg,
            observacion
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#alimento_obligg").html("");
        $("#tipo_alimentacion_obligg").html("");
        $("#fecha_alimentaion").html("");
        $("#cantidad_kg_obligg").html("");
        $("#observacion_a_u_obligg").html("");
    }

    if (disponibles_kg.length == 0 || disponibles_kg.trim() == "" || disponibles_kg == "0") {
        return swal.fire(
            "No hay cantidad dosponible de Kg",
            "No hay cantidad disponible de Kg",
            "warning"
        );
    }

    if (parseInt(cantidad_kg) > parseInt(disponibles_kg)) {
        $("#disponibles_kg_obligg").html("XXX");
        $("#cantidad_kg_obligg").html("XXX");
        return swal.fire(
            "Cantidad supera lo disponible",
            "La cantidad: " + cantidad_kg + " Kg, supera los disponible: " + disponibles_kg + " Kg",
            "warning"
        );
    } else {
        $("#disponibles_kg_obligg").html("");
        $("#cantidad_kg_obligg").html("");
    }

    var formdata = new FormData();
    formdata.append("alimento_id", desc[0]);
    formdata.append("lote_id", desc[1]);
    formdata.append("tipo_id", tipo_id);
    formdata.append("fecha_c", fecha_c);
    formdata.append("cantidad_kg", cantidad_kg);
    formdata.append("observacion", observacion);
    formdata.append("semana", semana);
    formdata.append("idcerdo", idcerdo);

    $.ajax({
        url: "/alimento/registrar_toda_alimentacion",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {
            // console.log(resp);
            if (resp > 0) {

                if (resp == 1) {

                    listar_alimento($("#tipo_alimento").val());
                    $("#disponibles_kg").val("");

                    $("#cantidad_kg").val("0");
                    $("#observacion_a_u").val("");
                    $("#modaal_cerdo_alimentar").modal("hide");
                    $(".card_aiment_uni").LoadingOverlay("hide");
                    return Swal.fire(
                        "Alimentación exitosa",
                        "La alimentación del cerdo se registro con exito",
                        "success"
                    );
                }

            } else {
                $(".card_aiment_uni").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo guardar el registro, falla en la matrix",
                    "error"
                );
            }
        },

        beforeSend: function () {
            $(".card_aiment_uni").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function valida_registro_alimentacion_unitaria(
    alimento_id,
    tipo_id,
    fecha_c,
    cantidad_kg,
    observacion
) {
    if (alimento_id.length == 0 || alimento_id == "0") {
        $("#alimento_obligg").html("Seleccione el alimento");
    } else {
        $("#alimento_obligg").html("");
    }

    if (tipo_id.length == 0 || tipo_id == "0") {
        $("#tipo_alimentacion_obligg").html("Seleccione el tipo alimentación");
    } else {
        $("#tipo_alimentacion_obligg").html("");
    }

    if (fecha_c.length == 0 || fecha_c.trim() == "") {
        $("#fecha_alimentaion").html("Ingrese la fecha");
    } else {
        $("#fecha_alimentaion").html("");
    }

    if (cantidad_kg == "0" || cantidad_kg.trim() == "") {
        $("#cantidad_kg_obligg").html("Ingrese la cantidad Kg");
    } else {
        $("#cantidad_kg_obligg").html("");
    }

    if (observacion.length == 0 || observacion.trim() == "") {
        $("#observacion_a_u_obligg").html("Ingrese la observación");
    } else {
        $("#observacion_t_obligg").html("");
    }
}

function guardar_detalle_alimentacion_uniitaria(id) {
    var idcerdo = $("#id_cerdo").val();

    $.ajax({
        url: "/alimento/guardar_detalle_alimentacion_uni",
        type: "POST",
        data: {
            id: id,
            idcerdo: idcerdo
        },
    }).done(function (resp) {

        if (resp > 0) {
            if (resp == 1) {

                listar_alimento($("#tipo_alimento").val());
                $("#disponibles_kg").val("");

                $("#cantidad_kg").val("0");
                $("#observacion_a_u").val("");
                $("#modaal_cerdo_alimentar").modal("hide");
                $(".card_aiment_uni").LoadingOverlay("hide");
                return Swal.fire(
                    "Alimentación exitosa",
                    "La alimentación del cerdo se registro con exito",
                    "success"
                );
            }
        } else {
            $(".card_aiment_uni").LoadingOverlay("hide");
            return Swal.fire(
                "Error",
                "No se pudo crear el detalle de alimentación, falla en la matrix",
                "error"
            );

        }

    });
}


///////////////// pesaje de los cerdos
function registra_pesaje() {
    Swal.fire({
        title: 'Guardar pesaje del cerdo?',
        text: "El pesaje se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_pesaje_cedo_cerdo();
        }
    })
}

function guardar_pesaje_cedo_cerdo() {
    var id = $("#id_cerdo_p").val();
    var semana = $("#semana_alimentacion_p").val();
    var peso_actual = $("#peso_actual").val();
    var metodo = $("#metodo").val();
    var observacion = $("#observacion").val();
    var etapa_fase = $("#etapa_fase").val();
    var nuevo_pesaje = $("#nuevo_pesaje").val();

    var perimetro_t = $("#perimetro_t").val();
    var largo_c = $("#largo_c").val();

    if (
        observacion.length == 0 ||
        observacion.trim() == "" ||
        nuevo_pesaje.length == 0 ||
        nuevo_pesaje.trim() == "" ||
        nuevo_pesaje == "0"

    ) {
        valida_registro_pesaje_cerdoo(
            observacion,
            nuevo_pesaje
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#nuevo_pesaje_obligg").html("");
        $("#observacion_obligg").html("");
    }

    var formdata = new FormData();
    formdata.append("id", id);
    formdata.append("semana", semana);
    formdata.append("peso_actual", peso_actual);
    formdata.append("metodo", metodo);
    formdata.append("observacion", observacion);
    formdata.append("etapa_fase", etapa_fase);
    formdata.append("nuevo_pesaje", nuevo_pesaje);

    formdata.append("perimetro_t", perimetro_t);
    formdata.append("largo_c", largo_c);

    $.ajax({
        url: "/alimento/guardar_pesaje_cerdo",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {

            if (resp == 1) {

                $("#nuevo_pesaje").val("");
                $("#observacion").val("");
                $(".peso_cerdo_old").LoadingOverlay("hide");
                $("#modal_pesaje").modal("hide");

                traer_detalle_galpon_cerdo();

                return Swal.fire(
                    "Registro guardado",
                    "El peso del cerdo de guardó con exito",
                    "success"
                );

            } else {

                $(".peso_cerdo_old").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo guardar el peso, falla en la matrix",
                    "error"
                );

            }
        },

        beforeSend: function () {
            $(".peso_cerdo_old").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function valida_registro_pesaje_cerdoo(
    observacion,
    nuevo_pesaje
) {
    if (observacion.length == 0 || observacion.trim() == "") {
        $("#observacion_obligg").html("Ingrese la observación");
    } else {
        $("#observacion_obligg").html("");
    }

    if (nuevo_pesaje.length == 0 || nuevo_pesaje.trim() == "" || nuevo_pesaje == "0") {
        $("#nuevo_pesaje_obligg").html("Ingrese el nuevo pesaje");
    } else {
        $("#tipo_alimentacion_obligg").html("");
    }
}

///////////////// vacunas del cerdo
function registrar_vacuncacion_cerdo() {
    Swal.fire({
        title: 'Guardar vacuna del cerdo?',
        text: "La vacuna se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_vacunasaa_cerdoo();
        }
    })
}

function guardar_vacunasaa_cerdoo() {
    var id_c = $("#id_cerdo_v").val();
    var id_vacuna = $("#vacuna").val();
    var semana = $("#semana_vacuna").val();
    var cantidad = $("#cantidad_dosis").val();
    var dosis_disponible = $("#dosis_disponible").val();
    var desc = id_vacuna.split(" - ");

    if (
        id_vacuna.length == 0 ||
        id_vacuna == "0" ||
        cantidad.length == 0 ||
        cantidad.trim() == ""
    ) {
        validar_registro_vacunacion_cerddo(
            id_vacuna,
            cantidad
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#cantidad_dosis_obligg").html("");
        $("#vacuna_obligg").html("");
    }

    if (parseInt(cantidad) > parseInt(dosis_disponible)) {
        $("#dosis_disponible_obligg").html("XXX");
        $("#cantidad_dosis_obligg").html("XXX");
        return swal.fire(
            "Cantidad supera la dosis disponible",
            "La cantidad: " + cantidad + " de dosis, supera las dosis disponibles: " + dosis_disponible + "",
            "warning"
        );
    } else {
        $("#dosis_disponible_obligg").html("");
        $("#cantidad_dosis_obligg").html("");
    }

    var formdata = new FormData();
    formdata.append("id_vacuna", desc[0]);
    formdata.append("id_lote", desc[1]);
    formdata.append("cantidad", cantidad);
    formdata.append("semana", semana);
    formdata.append("id_c", id_c);

    $.ajax({
        url: "/alimento/guardar_vacunasaa_cerdoo",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {

            if (resp == 1) {

                $("#cantidad_dosis").val("");
                $("#dosis_disponible").val("");
                listar_vacunas_lote($("#tipo_vacuna").val());
                $(".vacunacion_cerdo").LoadingOverlay("hide");
                $("#modal_vacunancion_cerdo").modal("hide");

                return Swal.fire(
                    "Registro guardado",
                    "La vacuna del cerdo de guardó con exito",
                    "success"
                );

            } else {

                $(".vacunacion_cerdo").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo guardar la vacuna, falla en la matrix",
                    "error"
                );

            }
        },

        beforeSend: function () {
            $(".vacunacion_cerdo").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function validar_registro_vacunacion_cerddo(
    id_vacuna,
    cantidad
) {
    if (id_vacuna.length == 0 || id_vacuna == "0") {
        $("#vacuna_obligg").html("Ingrese la vacuna");
    } else {
        $("#vacuna_obligg").html("");
    }

    if (cantidad.length == 0 || cantidad.trim() == "") {
        $("#cantidad_dosis_obligg").html("Ingrese cantidad de dosis");
    } else {
        $("#cantidad_dosis_obligg").html("");
    }
}

///////////////// vacunas todo el galpon
function registrar_todo_vacuncacion_cerdo() {
    Swal.fire({
        title: 'Guardar vacunas de todo el galpón?',
        text: "Las vacunas se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_vacunasaa_cerdoo_todoo();
        }
    })
}

function guardar_vacunasaa_cerdoo_todoo() {
    var id_vacuna = $("#vacuna_t").val();
    var semana = $("#semana_vacuna_t").val();
    var cantidad = $("#cantidad_dosis_t").val();
    var dosis_disponible = $("#dosis_disponible_t").val();
    var total_dosis = $("#total_dosis").val();
    var desc = id_vacuna.split(" - ");

    if (
        id_vacuna.length == 0 ||
        id_vacuna == "0" ||
        cantidad.length == 0 ||
        cantidad.trim() == "" ||
        cantidad == "0"
    ) {
        validar_registro_vacunacion_cerddo_todo(
            id_vacuna,
            cantidad
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#cantidad_dosis_t_obligg").html("");
        $("#vacuna_t_obligg").html("");
    }

    if (parseInt(total_dosis) > parseInt(dosis_disponible)) {
        $("#dosis_disponible_t_obligg").html("XXX");
        $("#total_dosis_obligg").html("XXX");
        return swal.fire(
            "Total supera la dosis disponible",
            "El total: " + cantidad + " de dosis, supera las dosis disponibles: " + dosis_disponible + "",
            "warning"
        );
    } else {
        $("#dosis_disponible_t_obligg").html("");
        $("#total_dosis_obligg").html("");
    }

    var count = 0;
    var arrego_cerdo_id = new Array();

    $("#tabla_galpo_cerdo tbody#tbody_tabla_galpo_cerdo tr").each(
        function () {
            arrego_cerdo_id.push($(this).find("td").eq(0).text());
            count++;
        }
    );

    if (count == 0) {
        return swal.fire(
            "No hay cerdos",
            "No hay cerdos dentro del galpón",
            "warning"
        );
    }

    //aqui combierto el arreglo a un string
    var id_c = arrego_cerdo_id.toString();

    var formdata = new FormData();
    formdata.append("id_vacuna", desc[0]);
    formdata.append("id_lote", desc[1]);
    formdata.append("cantidad", cantidad);
    formdata.append("semana", semana);
    formdata.append("id_c", id_c);

    $.ajax({
        url: "/alimento/guardar_vacunasaa_cerdoo_todo",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {

            if (resp == 1) {

                $("#cantidad_dosis_t").val("");
                $("#dosis_disponible_t").val("");
                $("#total_dosis").val("");

                listar_vacunas_lote_t($("#tipo_vacuna_t").val());
                $(".vacunacion_cerdo_total").LoadingOverlay("hide");
                $("#modal_vacunancion_cerdo_t").modal("hide");

                return Swal.fire(
                    "Registro guardado",
                    "Las vacunas de los cerdos se guardó con exito",
                    "success"
                );

            } else {

                $(".vacunacion_cerdo_total").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo guardar la vacuna, falla en la matrix",
                    "error"
                );

            }
        },

        beforeSend: function () {
            $(".vacunacion_cerdo_total").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function validar_registro_vacunacion_cerddo_todo(
    id_vacuna,
    cantidad
) {
    if (id_vacuna.length == 0 || id_vacuna == "0") {
        $("#vacuna_t_obligg").html("Ingrese la vacuna");
    } else {
        $("#vacuna_t_obligg").html("");
    }

    if (cantidad.length == 0 || cantidad.trim() == "" || cantidad == "0") {
        $("#cantidad_dosis_t_obligg").html("Ingrese cantidad de dosis");
    } else {
        $("#cantidad_dosis_t_obligg").html("");
    }
}

///////////////// guardar muerte del cerdo
function registrar_muerte_cerdo() {
    Swal.fire({
        title: 'Guardar la muerte del cerdo?',
        text: "El registro se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_muerte_cerdo();
        }
    })
}

function guardar_muerte_cerdo() {
    var id_cerdo = $("#id_cerdo_m").val();
    var semana = $("#semana_vacuna_m").val();
    var ig_galpon = $("#id_galpon_cerdo").val();
    var fecha = $("#fecha_vacuna_m").val();
    var hora = $("#hora_muerte").val();
    var motivo_muerte = $("#motivo_muerte").val();

    if (
        fecha.length == 0 ||
        fecha.trim() == "0" ||
        hora.length == 0 ||
        hora.trim() == "" ||
        motivo_muerte.length == 0 ||
        motivo_muerte.trim() == ""
    ) {
        validar_registro_muerte_cerdo(
            fecha,
            hora,
            motivo_muerte
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#fecha_m_obligg").html("");
        $("#hora_obligg").html("");
        $("#causa_obligg").html("");
    }

    var formdata = new FormData();
    formdata.append("id_cerdo", id_cerdo);
    formdata.append("ig_galpon", ig_galpon);
    formdata.append("fecha", fecha);
    formdata.append("hora", hora);
    formdata.append("motivo_muerte", motivo_muerte);
    formdata.append("semana", semana);

    $.ajax({
        url: "/alimento/guardar_muerte_cerdo",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {
            // console.log(resp);
            if (resp == 1) {

                $("#fecha_vacuna_m").val("");
                $("#motivo_muerte").val("");

                traer_detalle_galpon_cerdo();

                $(".muerte_cerdo").LoadingOverlay("hide");
                $("#modal_cerdo_muerto").modal("hide");

                return Swal.fire(
                    "Registro guardado",
                    "La muerte del cerdo se guardó con exito",
                    "success"
                );

            } else {

                $(".muerte_cerdo").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo guardar la muerte, falla en la matrix",
                    "error"
                );

            }
        },

        beforeSend: function () {
            $(".muerte_cerdo").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function validar_registro_muerte_cerdo(
    fecha,
    hora,
    motivo_muerte
) {
    if (fecha.length == 0 || fecha.trim() == "") {
        $("#fecha_m_obligg").html("Ingrese la fecha");
    } else {
        $("#fecha_m_obligg").html("");
    }

    if (hora.length == 0 || hora.trim() == "") {
        $("#hora_obligg").html("Ingrese la hora");
    } else {
        $("#hora_obligg").html("");
    }

    if (motivo_muerte.length == 0 || motivo_muerte.trim() == "") {
        $("#causa_obligg").html("Ingrese la causa de muerte");
    } else {
        $("#causa_obligg").html("");
    }
}

///////////////// vacunas del cerdo
function registrar_medicamento_cerdo() {
    Swal.fire({
        title: 'Guardar desparasitante del cerdo?',
        text: "El desparasitante se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_desparasitantee_cerdoo();
        }
    })
}

function guardar_desparasitantee_cerdoo() {
    var id_c = $("#id_cerdo_despa").val();
    var id_desparasitante = $("#desparasitante").val();
    var semana = $("#semana_desparasitacion").val();
    var cantidad = $("#cantidad_desparasitante").val();
    var dosis_disponible = $("#desparasitante_disponible").val();
    var desc = id_desparasitante.split(" - ");

    if (
        id_desparasitante.length == 0 ||
        id_desparasitante == "0" ||
        cantidad.length == 0 ||
        cantidad.trim() == ""
    ) {
        validar_registro_desparasitantes_cerddo(
            id_desparasitante,
            cantidad
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#cantidad_desparasitante_obligg").html("");
        $("#desparasitante_obligg").html("");
    }

    if (parseInt(cantidad) > parseInt(dosis_disponible)) {
        $("#desparasitante_disponible_obligg").html("XXX");
        $("#cantidad_desparasitante_obligg").html("XXX");
        return swal.fire(
            "Cantidad supera lo disponible",
            "La cantidad: " + cantidad + " , supera lo disponible: " + dosis_disponible + "",
            "warning"
        );
    } else {
        $("#desparasitante_disponible_obligg").html("");
        $("#cantidad_desparasitante_obligg").html("");
    }

    var formdata = new FormData();
    formdata.append("id_desparasitante", desc[0]);
    formdata.append("id_lote", desc[1]);
    formdata.append("cantidad", cantidad);
    formdata.append("semana", semana);
    formdata.append("id_c", id_c);

    $.ajax({
        url: "/alimento/guardar_desparasitantee_cerdoo",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {
            if (resp == 1) {
                $("#cantidad_desparasitante").val("");
                $("#desparasitante_disponible").val("");
                listar_desparasitante_lote($("#tipo_desparasitacion").val());
                $(".desparasitante_cerdo").LoadingOverlay("hide");
                $("#modal_medicamento_cerdo").modal("hide");
                return Swal.fire(
                    "Registro guardado",
                    "La desparasitación del cerdo se guardó con exito",
                    "success"
                );
            } else {

                $(".desparasitante_cerdo").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo guardar el registro, falla en la matrix",
                    "error"
                );

            }
        },

        beforeSend: function () {
            $(".desparasitante_cerdo").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function validar_registro_desparasitantes_cerddo(
    id_vacuna,
    cantidad
) {
    if (id_vacuna.length == 0 || id_vacuna == "0") {
        $("#desparasitante_obligg").html("Ingrese el desparasitante");
    } else {
        $("#desparasitante_obligg").html("");
    }

    if (cantidad.length == 0 || cantidad.trim() == "") {
        $("#cantidad_desparasitante_obligg").html("Ingrese cantidad");
    } else {
        $("#cantidad_desparasitante_obligg").html("");
    }
}

///////////////// desparasitación todo el galpon
function registrar_medicamento_cerdo_todo() {
    Swal.fire({
        title: 'Guardar desparasitación de todo el galpón?',
        text: "Las desparasitación se guardará en el sistema!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, guardar!'
    }).then((result) => {
        if (result.isConfirmed) {
            guardar_desparasitacion_cerdoo_todoo();
        }
    })
}

function guardar_desparasitacion_cerdoo_todoo() {
    var id_desparasitante = $("#desparasitante_t").val();
    var semana = $("#semana_desparasitacion_t").val();
    var cantidad = $("#cantidad_desparasitante_t").val();
    var disponible = $("#desparasitante_disponible_t").val();
    var total = $("#total_desparasitacion").val();
    var desc = id_desparasitante.split(" - ");

    if (
        id_desparasitante.length == 0 ||
        id_desparasitante == "0" ||
        cantidad.length == 0 ||
        cantidad.trim() == "" ||
        cantidad == "0"
    ) {
        validar_registro_desparasitacion_cerddo_todo(
            id_desparasitante,
            cantidad
        );

        return swal.fire(
            "Campo vacios",
            "Los campos no deben quedar vacios, complete los datos",
            "warning"
        );
    } else {
        $("#cantidad_desparasitante_t_obligg").html("");
        $("#desparasitante_t_obligg").html("");
    }

    if (parseInt(total) > parseInt(disponible)) {
        $("#desparasitante_disponible_t_obligg").html("XXX");
        $("#total_desparasitacion_obligg").html("XXX");
        return swal.fire(
            "Total supera lo disponible",
            "El total: " + cantidad + " , supera lo disponible: " + dosis_disponible + "",
            "warning"
        );
    } else {
        $("#desparasitante_disponible_t_obligg").html("");
        $("#total_desparasitacion_obligg").html("");
    }

    var count = 0;
    var arrego_cerdo_id = new Array();

    $("#tabla_galpo_cerdo tbody#tbody_tabla_galpo_cerdo tr").each(
        function () {
            arrego_cerdo_id.push($(this).find("td").eq(0).text());
            count++;
        }
    );

    if (count == 0) {
        return swal.fire(
            "No hay cerdos",
            "No hay cerdos dentro del galpón",
            "warning"
        );
    }

    //aqui combierto el arreglo a un string
    var id_c = arrego_cerdo_id.toString();

    var formdata = new FormData();
    formdata.append("id_desparasitante", desc[0]);
    formdata.append("id_lote", desc[1]);
    formdata.append("cantidad", cantidad);
    formdata.append("semana", semana);
    formdata.append("id_c", id_c);

    $.ajax({
        url: "/alimento/guardar_desparasitantee_cerdoo_todo",
        type: "POST",
        //aqui envio toda la formdata
        data: formdata,
        contentType: false,
        processData: false,
        success: function (resp) {
            if (resp == 1) {
                $("#cantidad_desparasitante_t_obligg").val("");
                $("#desparasitante_disponible_t_obligg").val("");
                $("#total_desparasitacion_obligg").val("");
                listar_desparasitante_lote_t($("#tipo_desparasitacion_t").val());
                $(".desprasitacion_cerdo_total").LoadingOverlay("hide");
                $("#modal_medicamento_cerdo_t").modal("hide");
                return Swal.fire(
                    "Registro guardado",
                    "La desparasitación de los cerdos se guardó con exito",
                    "success"
                );
            } else {
                $(".desprasitacion_cerdo_total").LoadingOverlay("hide");
                return Swal.fire(
                    "Error",
                    "No se pudo guardar el registro, falla en la matrix",
                    "error"
                );
            }
        },
        beforeSend: function () {
            $(".desprasitacion_cerdo_total").LoadingOverlay("show", {
                text: "Cargando...",
            });
        },
    });
    return false;
}

function validar_registro_desparasitacion_cerddo_todo(
    id_desparasitante,
    cantidad
) {
    if (id_desparasitante.length == 0 || id_desparasitante == "0") {
        $("#desparasitante_t_obligg").html("Ingrese el desparasitante");
    } else {
        $("#desparasitante_t_obligg").html("");
    }

    if (cantidad.length == 0 || cantidad.trim() == "" || cantidad == "0") {
        $("#cantidad_desparasitante_t_obligg").html("Ingrese cantidad");
    } else {
        $("#cantidad_desparasitante_t_obligg").html("");
    }
}





////////// listados de alimentos
function modal_listar_alimentos(id) {

    $.ajax({
        url: "/alimento/listar_aliento_cerdo",
        type: "POST",
        data: { id: id },
        success: function (resp) {

            console.log(resp);

            $("#tbody_tabla_l_alimento").empty();
            if (resp != 0) {
                var llenat = "";
                resp["data"].forEach((row) => {

                    llenat += `<tr> 

                            <td> ${row['fecha']} - ${row['hora']}  </td>
                            <td> ${row['tipo']}  </td>
                            <td> ${row['alimento']}  </td>
                            <td> ${row['cantidad']} Kg </td>
                            <td> ${row['tipo']} </td>
                            <td> ${row['semana']}  </td> 
                            <td> ${row['observacion']} </td>             
                                                
                            </tr>`;
                    $("#tbody_tabla_l_alimento").html(llenat);

                    $("#modal_listado_alimento_cerdo").modal({ backdrop: "static", keyboard: false });
                    $("#modal_listado_alimento_cerdo").modal("show");
                });
            } else {
                return Swal.fire(
                    "NO hay alimento",
                    "El cerdo no tiene alimento",
                    "warning"
                );
            }
        },

    });

}

////////// listados de pesajes
function modal_listar_pesaje(id) {

    $.ajax({
        url: "/alimento/listar_pesaje_cerdo",
        type: "POST",
        data: { id: id },
        success: function (resp) {
            $("#tbody_tabla_l_pesaje").empty();
            if (resp != 0) {
                var llenat = "";
                resp["data"].forEach((row) => {

                    llenat += `<tr> 

                            <td> ${row['fecha']} - ${row['hora']}  </td>
                            <td> ${row['semana']}  </td>
                            <td> ${row['metodo']} </td>
                            <td> ${row['nuevo_pesaje']} Kg </td> 
                            <td> ${row['etapa_fase']}  </td>  
                            <td> ${row['observacion']}  </td> 
                            <td> ${row['perimetro_t']} </td>     
                            <td> ${row['largo_c']} </td>             
                                                
                            </tr>`;
                    $("#tbody_tabla_l_pesaje").html(llenat);

                    $("#modal_listado_pesaje_cerdo").modal({ backdrop: "static", keyboard: false });
                    $("#modal_listado_pesaje_cerdo").modal("show");
                });
            } else {
                return Swal.fire(
                    "NO hay pesaje",
                    "El cerdo no tiene pesaje",
                    "warning"
                );
            }
        },

    });

}

////////// listados de vacunas
function modal_listar_vacunass(id) {

    $.ajax({
        url: "/alimento/listar_vacunasa_cerdo",
        type: "POST",
        data: { id: id },
        success: function (resp) {
            $("#tbody_tabla_l_vacunas").empty();
            if (resp != 0) {

                var llenat = "";
                resp["data"].forEach((row) => {

                    llenat += `<tr> 
                            <td> ${row['fecha']} - ${row['hora']}  </td>
                            <td> ${row['semana']}  </td>
                            <td> ${row['nombre']} - ${row['tipo_vacuna']} </td>
                            <td> ${row['dosis']} </td>                               
                            </tr>`;
                    $("#tbody_tabla_l_vacunas").html(llenat);

                    $("#modal_listado_vacunas_cerdo").modal({ backdrop: "static", keyboard: false });
                    $("#modal_listado_vacunas_cerdo").modal("show");
                });
            } else {
                return Swal.fire(
                    "No hay vacunas",
                    "El cerdo no tiene vacunas",
                    "warning"
                );
            }
        },

    });

}

//// modal registrar cerdomuerto
function modal_cerdo_muerto_galpo(id) {
    $("#id_cerdo_m").val(id);
    $("#semana_vacuna_m").val(semana);
    $("#modal_cerdo_muerto").modal({ backdrop: "static", keyboard: false });
    $("#modal_cerdo_muerto").modal("show");
}

//// ver modal cerdos muertos
function modal_ver_cerdos_muertos() {
    var id = $("#id_galpon_cerdo").val();

    $.ajax({
        url: "/alimento/ver_cerdos_muertos_galpon",
        type: "POST",
        data: { id: id },
        success: function (resp) {
            $("#tbody_tabla_l_muertos").empty();
            if (resp != 0) {
                var llenat = "";
                resp["data"].forEach((row) => {

                    llenat += `<tr> 
                            <td> ${row['cerdo']} </td>
                            <td> ${row['fecha_m']} - ${row['hora_m']}  </td>
                            <td> ${row['semana']}  </td>
                            <td> ${row['motivo']}  </td>
                            <td> ${row['fecha_r']} - ${row['hora_r']} </td>      
                            </tr>`;

                    $("#tbody_tabla_l_muertos").html(llenat);
                    $("#modal_cerdo_muerto_ver").modal({ backdrop: "static", keyboard: false });
                    $("#modal_cerdo_muerto_ver").modal("show");
                });
            } else {
                return Swal.fire(
                    "No hay cerdos muertos",
                    "No hay cerdos muertos",
                    "warning"
                );
            }
        },

    });

}

//// ver modal para listar desparasitantes
function modal_listar_desparasitantess(id) {

    $.ajax({
        url: "/alimento/listar_desparasitantess_cerdo",
        type: "POST",
        data: { id: id },
        success: function (resp) {
            $("#tbody_tabla_l_desparasitante").empty();
            if (resp != 0) {
                var llenat = "";
                resp["data"].forEach((row) => {

                    llenat += `<tr> 
                                <td> ${row['fecha']} - ${row['hora']}  </td>
                                <td> ${row['semana']}  </td>
                                <td> ${row['nombre']} - ${row['tipo']} </td>
                                <td> ${row['cantidad']} </td>                               
                                </tr>`;
                    $("#tbody_tabla_l_desparasitante").html(llenat);

                    $("#modal_cerdo_desparasitacion_ver").modal({ backdrop: "static", keyboard: false });
                    $("#modal_cerdo_desparasitacion_ver").modal("show");
                });
            } else {
                return Swal.fire(
                    "No hay desparasitación",
                    "No hay desparasitación",
                    "warning"
                );
            }
        },

    });

}




///// desparasitanción de todos los cerdos
function modal_desparasitar_todo_galpon() {
    $("#semana_desparasitacion_t").val(semana);
    $("#modal_medicamento_cerdo_t").modal({ backdrop: "static", keyboard: false });
    $("#modal_medicamento_cerdo_t").modal("show");
}

$("#tipo_desparasitacion_t").on("change", function () {
    var id = $(this).val();
    listar_desparasitante_lote_t(id)
});

function listar_desparasitante_lote_t(id) {
    $("#desparasitante_disponible_t").val("");
    if (id == 0) {
        return $("#desparasitante_t").html("<option value='0'>--- Seleccione tipo ---</option>");
    }
    $(".espiner_desparasitante").LoadingOverlay("show");
    $.ajax({
        url: "/alimento/select_desparasitante_lote_all",
        type: "POST",
        data: {
            id: id
        },
    }).done(function (data) {
        $("#desparasitante_t").empty();
        var cadena = "<option value='0'>--- Seleccione desparasitante ---</option>";
        if (data != 0) {
            $(".espiner_desparasitante").LoadingOverlay("hide");
            //bucle para extraer los datos del rol
            for (var i = 0; i < data.length; i++) {
                cadena += "<option value='" + data[i]['id_m'] + " - " + data[i]['id_l'] + "'> " + data[i]['codigo'] + " - " + data[i]['nombre'] + " - " + data[i]['fecha'] + " - " + data[i]['cantidad'] + " disponible </option>";
            }
            //aqui concadenamos al id del select
            $("#desparasitante_t").html(cadena);
        } else {
            $(".espiner_desparasitante").LoadingOverlay("hide");
            cadena += "<option value='0'>No hay desparasitantes en lote</option>";
            $("#desparasitante_t").html(cadena);
            $("#desparasitante_disponible_t").val("")
        }

    });
}

$("#desparasitante_t").on("change", function () {
    var id = $(this).val();

    if (id == 0) {
        return $("#desparasitante_disponible_t").val("");
    }
    var desc = id.split(" - ");
    $(".espiner_disponible_d").LoadingOverlay("show");
    $.ajax({
        url: "/alimento/traer_cantidad_desparasitante_lote",
        type: "POST",
        data: {
            id: desc[1]
        },
    }).done(function (data) {
        $(".espiner_disponible_d").LoadingOverlay("hide");
        if (data != 0) {
            $("#desparasitante_disponible_t").val(data[0])
        } else {
            $("#desparasitante_disponible_t").val("")
        }
    });
});

$("#cantidad_desparasitante_t").on("keyup", function () {
    var cantidad = $(this).val();
    var disponibles = $("#desparasitante_disponible_t").val();
    if (disponibles.length == 0 || disponibles.trim() == "" || disponibles == 0) {
        $(this).val("0")
        $("#desparasitante_disponible_t_obligg").html("");
        return swal.fire(
            "No hay cantidad disponible",
            "Sin cantidad",
            "warning"
        );
    } else {
        if (cantidad != "") {
            var count = 0;
            $("#tabla_galpo_cerdo tbody#tbody_tabla_galpo_cerdo tr").each(
                function () {
                    count++;
                }
            );
            var racion = parseInt(cantidad * count);
            $("#total_desparasitacion").val(racion);
        } else {
            $("#total_desparasitacion").val("");
        }
    }
});