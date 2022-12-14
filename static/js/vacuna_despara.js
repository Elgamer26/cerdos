var tabla_tipo_vacuna, tabla_vacunas, tabla_lote_vacuna;

function registrar_calendario_cerdo() {
  var titulo = $("#evento_titulo").val(); 
  var galpon = $("#galpon_cerdo").val(); 
  var descripcion = $("#descripcion").val();
  var tipo = $("#tipo").val();
  var fecha_evento = $("#fecha_evento").val();
  var color = $("#color").val();
  var color_etiqueta = $("#color_etiqueta").val();

  if (
    titulo.trim() == "" || 
    descripcion.trim() == "" ||
    tipo == 0
  ) {
    validar_registro_calendario_save(titulo, descripcion, tipo);

    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#titulo_obligg").html(""); 
    $("#descripcion_obligg").html("");
    $("#tipoo_obligg").html("");
  }

  if (color == color_etiqueta) {
    $("#color_obligg").html("Colores iguales");
    $("#etiqueta_obligg").html("Colores iguales");
    return swal.fire(
      "Colores",
      "El 'Color letra', no debe ser igual al 'Color etiqueta'",
      "warning"
    );
  } else {
    $("#color_obligg").html("");
    $("#etiqueta_obligg").html("");
  }

  var formdata = new FormData();
  formdata.append("titulo", titulo);
  formdata.append("galpon", galpon);
  formdata.append("descripcion", descripcion);
  formdata.append("tipo", tipo);
  formdata.append("fecha_evento", fecha_evento);
  formdata.append("color", color);
  formdata.append("color_etiqueta", color_etiqueta);

  $.ajax({
    url: "/vacunas/calendario_registrar",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {

      if (resp > 0) {
        if (resp == 1) {

          $(".bg-success").LoadingOverlay("hide");
          $("#modal_canlendario_register").modal("hide");
          $("#calendar").fullCalendar("refetchEvents");
          Listar_tabla_calendar();

          return Swal.fire(
            "Calendario creado con éxito",
            "El calendario creo con éxito",
            "success"
          );
        } else if (resp == 2) {
          $(".bg-success").LoadingOverlay("hide");
          return Swal.fire(
            "Calendario ya existe",
            "El gapoón seleccionado ya tiene creado un evento: '" + tipo + "' en el calendario en la fecha: '" +
            fecha_evento +
            "', ya existe en el sistema",
            "warning"
          );
        }
      } else {
        $(".bg-success").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo crear el calendario, falla en la matrix",
          "error"
        );
      }

    },

    beforeSend: function () {
      $(".bg-success").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

function validar_registro_calendario_save(titulo, descripcion, tipo) {
  if (titulo.trim() == "") {
    $("#titulo_obligg").html("Ingrese el titulo");
  } else {
    $("#titulo_obligg").html("");
  }

  if (descripcion.trim() == "") {
    $("#descripcion_obligg").html("Ingrese la descripción");
  } else {
    $("#descripcion_obligg").html("");
  }

  if (tipo == 0) {
    $("#tipoo_obligg").html("Seleccione el tipo");
  } else {
    $("#tipoo_obligg").html("");
  }
}

function editar_calendario_cerdo() {
  var id = $("#id_calendario").val();
  var titulo = $("#evento_titulo_edit").val(); 
  var descripcion = $("#descripcion_edit").val();
  var tipo = $("#tipo_edit").val();
  var fecha_evento = $("#fecha_evento_edit").val();
  var color = $("#color_edit").val();
  var color_etiqueta = $("#color_etiqueta_edit").val();

  if (
    titulo.trim() == "" ||
    descripcion.trim() == "" ||
    tipo == 0
  ) {
    validar_editar_calendario(titulo, descripcion, tipo);

    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#titulo_obligg_edit").html(""); 
    $("#descripcion_obligg_edit").html("");
    $("#tipoo_obligg_edit").html("");
  }

  if (color == color_etiqueta) {
    $("#color_obligg_edit").html("Colores iguales");
    $("#etiqueta_obligg_edit").html("Colores iguales");
    return swal.fire(
      "Colores",
      "El 'Color letra', no debe ser igual al 'Color etiqueta'",
      "warning"
    );
  } else {
    $("#color_obligg_edit").html("");
    $("#etiqueta_obligg_edit").html("");
  }

  var formdata = new FormData();
  formdata.append("id", id);
  formdata.append("titulo", titulo);
  formdata.append("descripcion", descripcion);
  formdata.append("tipo", tipo);
  formdata.append("fecha_evento", fecha_evento);
  formdata.append("color", color);
  formdata.append("color_etiqueta", color_etiqueta);

  $.ajax({
    url: "/vacunas/calendario_editar",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {

      if (resp > 0) {
        if (resp == 1) {

          $(".bg-primary").LoadingOverlay("hide");
          $("#modal_canlendario_editar").modal("hide");
          $("#calendar").fullCalendar("refetchEvents");
          Listar_tabla_calendar();

          return Swal.fire(
            "Calendario editado con éxito",
            "El calendario se edito con éxito",
            "success"
          );
        } else if (resp == 2) {
          $(".bg-primary").LoadingOverlay("hide");
          return Swal.fire(
            "Calendario ya existe",
            "Ya tiene creado un evento: '" + tipo + "' en el calendario en la fecha: '" +
            fecha_evento +
            "', ya existe en el sistema",
            "warning"
          );
        }
      } else {
        $(".bg-primary").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo editar el calendario, falla en la matrix",
          "error"
        );
      }

    },

    beforeSend: function () {
      $(".bg-primary").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

function validar_editar_calendario(titulo, descripcion, tipo) {
  if (titulo.trim() == "") {
    $("#titulo_obligg_edit").html("Ingrese el titulo");
  } else {
    $("#titulo_obligg_edit").html("");
  }

  if (descripcion.trim() == "") {
    $("#descripcion_obligg_edit").html("Ingrese la descripción");
  } else {
    $("#descripcion_obligg_edit").html("");
  }

  if (tipo == 0) {
    $("#tipoo_obligg_edit").html("Seleccione el tipo");
  } else {
    $("#tipoo_obligg_edit").html("");
  }
}

/// eliminra  evento del calendario
function eliminar_evento_calendario() {
  var id = $("#id_calendario").val();

  Swal.fire({
    title: "Eliminar evento?",
    text: "El evento se eliminará del calendario!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      eliminar_evento_calendario_ok(id);
    }
  });
}

function eliminar_evento_calendario_ok(id) {
  $.ajax({
    url: "/vacunas/eliminar_evento_calendario",
    type: "POST",
    data: { id: id },
  }).done(function (response) {
    if (response == 1) {
      
      $("#modal_canlendario_editar").modal("hide");
      $("#calendar").fullCalendar("refetchEvents");  
      Listar_tabla_calendar();
          
      return Swal.fire(
        "Evento eliminado",
        "El evento se eliminó con éxito",
        "success"
      );
    } else {
      return Swal.fire(
        "Error",
        "No se pudo eliminar el evento, error en la matrix",
        "error"
      );
    }
  });
}

///// tipo vacuna
function Listar_tipo_vacuna() {
  tabla_tipo_vacuna = $("#tabla_tipo_tv_").DataTable({
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
      url: "/vacunas/Listar_tipo_vacuna",
      type: "GET",
    },
    //hay que poner la misma cantidad de columnas y tambien en el html
    columns: [
      { defaultContent: "" },
      {
        data: "estado",
        render: function (data, type, row) {
          if (data == 1) {
            return `<button style='font-size:10px;' type='button' class='inactivar btn btn-outline-danger' title='Inactivar el cerdo'><i class='fa fa-times' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='editar btn btn-outline-primary' title='Editar el cerdo'><i class='fa fa-edit' style='font-size: 15px;'></i></button>`;
          } else {
            return `<button style='font-size:10px;' type='button' class='activar btn btn-outline-success' title='Activar el cerdo'><i class='fa fa-check' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='editar btn btn-outline-primary' title='Editar el cerdo'><i class='fa fa-edit' style='font-size: 15px;'></i></button>`;
          }
        },
      },
      { data: "tipo" },
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
    order: [[0, "ASC"]],
  });

  //esto es para crearn un contador para la tabla este contador es automatico
  tabla_tipo_vacuna.on("draw.dt", function () {
    var pageinfo = $("#tabla_tipo_tv_").DataTable().page.info();
    tabla_tipo_vacuna
      .column(0, { page: "current" })
      .nodes()
      .each(function (cell, i) {
        cell.innerHTML = i + 1 + pageinfo.start;
      });
  });
}

function registra_tipo_vacuna() {
  var valor = $("#tipo_vacuna").val();

  $("#mensaje_tipo_i_success").text("");
  $(".alerta_smsm_tipo_i_success").hide(1000);

  if (valor.length == 0 || valor.trim() == "") {
    $("#mensaje_tipo_i").text("Ingrese el tipo de vacuna");
    $(".alerta_smsm_tipo_i").show(3000);
    return false;
  } else {
    $("#mensaje_tipo_i").text("");
    $(".alerta_smsm_tipo_i").hide(1000);
  }

  funcion = "registra_tipo_vacuna";

  $.ajax({
    type: "POST",
    url: "/vacunas/accion_tipo_vacuna",
    data: { valor: valor, funcion: funcion },
    success: function (response) {

      if (response == 1) {

        $(".card-dark").LoadingOverlay("hide");
        $("#tipo_vacuna").val("");

        $("#mensaje_tipo_i_success").text("El tipo de vacuna se creo con éxito");
        $(".alerta_smsm_tipo_i_success").show(3000);

        tabla_tipo_vacuna.ajax.reload();

      } else if (response == 2) {

        $(".card-dark").LoadingOverlay("hide");
        $("#mensaje_tipo_i").text("El tipo de vacuna: '" + valor + "', ya existe");
        $(".alerta_smsm_tipo_i").show(1000);

      } else {

        $(".card-dark").LoadingOverlay("hide");
        $("#mensaje_tipo_i").text("Error:" + response);
        $(".alerta_smsm_tipo_i").show(1000);

      }
    },

    beforeSend: function () {
      $(".card-dark").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
}

$("#tabla_tipo_tv_").on("click", ".editar", function () {
  //esto esta extrayendo los datos de la tabla el (data)
  var data = tabla_tipo_vacuna.row($(this).parents("tr")).data(); //a que fila deteta que doy click
  //esta condicion es importante para el responsibe porque salda un error si no lo pongo
  if (tabla_tipo_vacuna.row(this).child.isShown()) {
    //esto es cuando esta en tamaño responsibo
    var data = tabla_tipo_vacuna.row(this).data();
  }

  $("#mensaje_tipo_i_success").text("");
  $(".alerta_smsm_tipo_i_success").hide(1000);

  $("#mensaje_tipo_i").text("");
  $(".alerta_smsm_tipo_i").hide(1000);

  document.getElementById("id_tipo_tv").value = data.id;
  document.getElementById("tipo_vacuna").value = data.tipo;

  $("#unir_texto").text("Editar tipo de vacuna");
  $("#btn_registrar").hide();
  $("#btn_editar").show();
  $("#btn_nuevo").show();
});

function editar_tipo_vacuna() {
  var id = $("#id_tipo_tv").val();
  var valor = $("#tipo_vacuna").val();

  $("#mensaje_tipo_i_success").text("");
  $(".alerta_smsm_tipo_i_success").hide(1000);

  if (valor.length == 0 || valor.trim() == "") {
    $("#mensaje_tipo_i").text("Ingrese el tipo de vacuna");
    $(".alerta_smsm_tipo_i").show(3000);
    return false;
  } else {
    $("#mensaje_tipo_i").text("");
    $(".alerta_smsm_tipo_i").hide(1000);
  }

  funcion = "editar_tipo_vacuna";

  $.ajax({
    type: "POST",
    url: "/vacunas/accion_tipo_vacuna",
    data: { valor: valor, funcion: funcion, id: id },
    success: function (response) {

      if (response == 1) {

        $(".card-dark").LoadingOverlay("hide");
        $("#tipo_vacuna").val("");
        $("#id_tipo_tv").val("");

        $("#mensaje_tipo_i_success").text("El tipo de vacuna se edito con éxito");
        $(".alerta_smsm_tipo_i_success").show(3000);

        tabla_tipo_vacuna.ajax.reload();

        $("#unir_texto").text("Registrar tipo vacuna");
        $("#btn_registrar").show();
        $("#btn_editar").hide();
        $("#btn_nuevo").hide();

      } else if (response == 2) {

        $(".card-dark").LoadingOverlay("hide");
        $("#mensaje_tipo_i").text("El tipo de vacuna: '" + valor + "', ya existe");
        $(".alerta_smsm_tipo_i").show(1000);

      } else {

        $(".card-dark").LoadingOverlay("hide");
        $("#mensaje_tipo_i").text("Error:" + response);
        $(".alerta_smsm_tipo_i").show(1000);

      }
    },

    beforeSend: function () {
      $(".card-dark").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
}

$("#tabla_tipo_tv_").on("click", ".inactivar", function () {
  //esto esta extrayendo los datos de la tabla el (data)
  var data = tabla_tipo_vacuna.row($(this).parents("tr")).data(); //a que fila deteta que doy click
  //esta condicion es importante para el responsibe porque salda un error si no lo pongo
  if (tabla_tipo_vacuna.row(this).child.isShown()) {
    //esto es cuando esta en tamaño responsibo
    var data = tabla_tipo_vacuna.row(this).data();
  }
  var dato = 0;
  var id = data.id;

  Swal.fire({
    title: "Cambiar estado?",
    text: "El estado del tipo vacuna se cambiará!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, cambiar!",
  }).then((result) => {
    if (result.isConfirmed) {
      cambiar_estado_tipo_vacuna(id, dato);
    }
  });
});

$("#tabla_tipo_tv_").on("click", ".activar", function () {
  //esto esta extrayendo los datos de la tabla el (data)
  var data = tabla_tipo_vacuna.row($(this).parents("tr")).data(); //a que fila deteta que doy click
  //esta condicion es importante para el responsibe porque salda un error si no lo pongo
  if (tabla_tipo_vacuna.row(this).child.isShown()) {
    //esto es cuando esta en tamaño responsibo
    var data = tabla_tipo_vacuna.row(this).data();
  }
  var dato = 1;
  var id = data.id;

  Swal.fire({
    title: "Cambiar estado?",
    text: "El estado del tipo vacuna se cambiará!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, cambiar!",
  }).then((result) => {
    if (result.isConfirmed) {
      cambiar_estado_tipo_vacuna(id, dato);
    }
  });
});

function cambiar_estado_tipo_vacuna(id, dato) {
  var res = "";
  if (dato == 1) {
    res = "activo";
  } else {
    res = "inactivo";
  }

  funcion = "estado_tipo_vacuna";

  $.ajax({
    url: "/vacunas/accion_tipo_vacuna",
    type: "POST",
    data: { id: id, dato: dato, funcion: funcion },
  }).done(function (response) {
    if (response > 0) {
      if (response == 1) {

        tabla_tipo_vacuna.ajax.reload();
        return Swal.fire(
          "Estado de marca",
          "EL estado se " + res + " con extio",
          "success"
        );
      }
    } else {
      return Swal.fire(
        "Estado de marca",
        "No se pudo cambiar el estado, error en la matrix",
        "error"
      );
    }
  });
}

//// Vacunas
function registrar_vacuna() {
  Swal.fire({
    title: 'Guardar registro?',
    text: "El registro se guardará en el sistema!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, guardar!'
  }).then((result) => {
    if (result.isConfirmed) {
      guardar_vacunas_de_cerdos();
    }
  })
}

function guardar_vacunas_de_cerdos() {
  var codigo = $("#codigo_vacuna").val();
  var nombre = $("#nombre").val();
  var tipo = $("#tipo_id").val();
  var cantidad = $("#cantidad").val();
  var precio = $("#precio_c").val();
  var detalle = $("#detalle_v").val();
  var presentacion = $("#presentacion").val();

  var registro_sani = $("#registro_sani").val();
  var cantidad_dosis = $("#cantidad_dosis").val();

  if (
    codigo.length == 0 ||
    codigo.trim() == "" ||
    nombre.length == 0 ||
    nombre.trim() == "" ||
    tipo == 0 ||
    tipo.trim() == "0" ||
    cantidad < 0 ||
    cantidad.trim() == "" ||
    precio < 0 ||
    precio.trim() == "" ||
    detalle.length == 0 ||
    detalle.trim() == "" ||
    presentacion.length == 0 ||
    presentacion.trim() == "" ||
    registro_sani.length == 0 ||
    registro_sani.trim() == "" ||
    cantidad_dosis.length == 0 ||
    cantidad_dosis.trim() == ""
  ) {
    validar_registro_vacunas_REGISTER(
      codigo,
      nombre,
      tipo,
      cantidad,
      precio,
      detalle,
      presentacion,
      registro_sani,
      cantidad_dosis
    );

    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#codigo_oblig").html("");
    $("#nombre_obligg").html("");
    $("#tipo_obligg").html("");
    $("#cantidad_obligg").html("");
    $("#precio_obligg").html("");
    $("#detalle_obligg").html("");
    $("#presentacion_obligg").html("");
    $("#cantidad_dosis_obligg").html("");
    $("#registro_sani_obligg").html("");
  }

  var formdata = new FormData();
  var foto = $("#foto")[0].files[0];
  //est valores son como los que van en la data del ajax
  formdata.append("codigo", codigo);
  formdata.append("nombre", nombre);
  formdata.append("tipo", tipo);
  formdata.append("cantidad", cantidad);
  formdata.append("precio", precio);
  formdata.append("detalle", detalle);
  formdata.append("presentacion", presentacion);

  formdata.append("registro_sani", registro_sani);
  formdata.append("cantidad_dosis", cantidad_dosis);

  formdata.append("foto", foto);

  $.ajax({
    url: "/vacunas/crear_vacuna_cerdos",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          $(".card-success").LoadingOverlay("hide");
          cargar_contenido("contenido_principal", "/vacunas");

          return Swal.fire(
            "Vacuna creado con éxito",
            "La vacuna se creo con éxito",
            "success"
          );
        } else if (resp == 2) {
          $(".card-success").LoadingOverlay("hide");
          return Swal.fire(
            "Codigo ya existe",
            "El codigo '" + codigo + "', ya existe en el sistema",
            "warning"
          );
        }
      } else {
        $(".card-success").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo crear la vacuna, falla en la matrix",
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

function validar_registro_vacunas_REGISTER(
  codigo,
  nombre,
  tipo,
  cantidad,
  precio,
  detalle,
  presentacion,
  registro_sani,
  cantidad_dosis
) {
  if (codigo.length == 0 || codigo.trim() == "") {
    $("#codigo_oblig").html("Ingrese código");
  } else {
    $("#codigo_oblig").html("");
  }

  if (nombre.length == 0 || nombre.trim() == "") {
    $("#nombre_obligg").html("Ingrese nombre de la vacuna");
  } else {
    $("#nombre_obligg").html("");
  }

  if (tipo == 0 || tipo.trim() == "") {
    $("#tipo_obligg").html("Ingrese tipo de vacuna");
  } else {
    $("#tipo_obligg").html("");
  }

  if (cantidad < 0 || cantidad.trim() == "") {
    $("#cantidad_obligg").html("Ingrese la cantidad");
  } else {
    $("#cantidad_obligg").html("");
  }

  if (precio < 0 || precio.trim() == "") {
    $("#precio_obligg").html("Ingrese el precio");
  } else {
    $("#precio_obligg").html("");
  }

  if (detalle.length == 0 || detalle.trim() == "") {
    $("#detalle_obligg").html("Ingrese el detalle de la vacuna");
  } else {
    $("#detalle_obligg").html("");
  }

  if (presentacion.length == 0 || presentacion.trim() == "") {
    $("#presentacion_obligg").html("Ingrese la presentación de la vacuna");
  } else {
    $("#presentacion_obligg").html("");
  }

  if (registro_sani.length == 0 || registro_sani.trim() == "") {
    $("#cantidad_dosis_obligg").html("Ingrese cantidad de dosis");
  } else {
    $("#cantidad_dosis_obligg").html("");
  }

  if (cantidad_dosis.length == 0 || cantidad_dosis.trim() == "") {
    $("#registro_sani_obligg").html("Ingrese registro sanitario");
  } else {
    $("#registro_sani_obligg").html("");
  }
}

function listar_vacunas() {
  tabla_vacunas = $("#tabla_vacunas").DataTable({
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
      url: "/vacunas/listar_vacunas",
      type: "GET",
    },
    //hay que poner la misma cantidad de columnas y tambien en el html
    columns: [
      { defaultContent: "" },
      {
        data: "estado",
        render: function (data, type, row) {
          if (data == 1) {
            return `<button style='font-size:10px;' type='button' class='inactivar btn btn-outline-danger' title='Inactivar el cerdo'><i class='fa fa-times' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='editar btn btn-outline-primary' title='Editar el cerdo'><i class='fa fa-edit' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='photo btn btn-outline-warning' title='Foto del cerdo'><i class='fa fa-image' style='font-size: 15px;'></i></button>`;
          } else {
            return `<button style='font-size:10px;' type='button' class='activar btn btn-outline-success' title='Activar el cerdo'><i class='fa fa-check' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='editar btn btn-outline-primary' title='Editar el cerdo'><i class='fa fa-edit' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='photo btn btn-outline-warning' title='foto del cerdo'><i class='fa fa-image' style='font-size: 15px;'></i></button>`;
          }
        },
      },
      { data: "codigo" },
      { data: "nombre" },
      { data: "tipo" },
      {
        data: "foto",
        render: function (data, type, row) {
          // {{url_for('static', filename='assets/img/admin-avatar.png')}}
          return (
            "<img class='img-circle' src='static/uploads/vacuna/" +
            data +
            "' width='50px' />"
          );
        },
      },
      { data: "presentacion" },
      { data: "precio" },
      { data: "detalle" },
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
    dom: "Bfrtilp",
    buttons: [
      {
        extend: "excelHtml5",
        text: "Excel",
        titleAttr: "Exportar a Excel",
        className: "btn btn-success greenlover",
      },
      {
        extend: "pdfHtml5",
        text: "PDF",
        titleAttr: "Exportar a PDF",
        className: "btn btn-danger redfule",
      },
      {
        extend: "print",
        text: "Imprimir",
        titleAttr: "Imprimir",
        className: "btn btn-primary azuldete",
      },
    ],
    order: [[0, "ASC"]],
  });

  //esto es para crearn un contador para la tabla este contador es automatico
  tabla_vacunas.on("draw.dt", function () {
    var pageinfo = $("#tabla_vacunas").DataTable().page.info();
    tabla_vacunas
      .column(0, { page: "current" })
      .nodes()
      .each(function (cell, i) {
        cell.innerHTML = i + 1 + pageinfo.start;
      });
  });
}

function listar_lotes_vacunas() {
  tabla_lote_vacuna = $("#tabla_lote_vacuna").DataTable({
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
      url: "/vacunas/listar_vacunas_lotes",
      type: "GET",
    },
    //hay que poner la misma cantidad de columnas y tambien en el html
    columns: [
      {
        render: function (data, type, row) {
          return `<button style='font-size:10px;' type='button' class='eliminar btn btn-outline-danger' title='Eliminar el lote'><i class='fa fa-times' style='font-size: 15px;'></i></button>`;
        },
      },
      { data: "codigo" },
      { data: "nombre" },
      { data: "cantidad" },
      { data: "fecha_i" },
      { data: "fecha_f" },
      { data: "fecha" },
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
    dom: "Bfrtilp",
    buttons: [
      {
        extend: "excelHtml5",
        text: "Excel",
        titleAttr: "Exportar a Excel",
        className: "btn btn-success greenlover",
      },
      {
        extend: "pdfHtml5",
        text: "PDF",
        titleAttr: "Exportar a PDF",
        className: "btn btn-danger redfule",
      },
      {
        extend: "print",
        text: "Imprimir",
        titleAttr: "Imprimir",
        className: "btn btn-primary azuldete",
      },
    ],
    order: [[0, "ASC"]],
  });
}

$("#tabla_lote_vacuna").on("click", ".eliminar", function () {
  //esto esta extrayendo los datos de la tabla el (data)
  var data = tabla_lote_vacuna.row($(this).parents("tr")).data(); //a que fila deteta que doy click
  //esta condicion es importante para el responsibe porque salda un error si no lo pongo
  if (tabla_lote_vacuna.row(this).child.isShown()) {
    //esto es cuando esta en tamaño responsibo
    var data = tabla_lote_vacuna.row(this).data();
  }

  var id = data.id;

  Swal.fire({
    title: "Eliminar el lote de vacuna?",
    text: "El lote de vacina se eliminará!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      eliminar_lote_vacuna_a(id);
    }
  });

});

function eliminar_lote_vacuna_a(id) {
  $.ajax({
    url: "/vacunas/eliminar_lote_vacuna_a",
    type: "POST",
    data: { id: id },
  }).done(function (response) {
    if (response > 0) {
      if (response == 1) {
        tabla_lote_vacuna.ajax.reload();
        return Swal.fire(
          "Lote eliminado",
          "EL lote de vacuna se eliminó con éxito",
          "success"
        );
      }
    } else {
      return Swal.fire(
        "Error",
        "No se pudo eliminar el lote, error en la matrix",
        "error"
      );
    }
  });
}

$("#tabla_vacunas").on("click", ".inactivar", function () {
  //esto esta extrayendo los datos de la tabla el (data)
  var data = tabla_vacunas.row($(this).parents("tr")).data(); //a que fila deteta que doy click
  //esta condicion es importante para el responsibe porque salda un error si no lo pongo
  if (tabla_vacunas.row(this).child.isShown()) {
    //esto es cuando esta en tamaño responsibo
    var data = tabla_vacunas.row(this).data();
  }
  var dato = 0;
  var id = data.id;

  Swal.fire({
    title: "Cambiar estado?",
    text: "El estado de la vacuna se cambiará!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, cambiar!",
  }).then((result) => {
    if (result.isConfirmed) {
      cambiar_estado_vacuna(id, dato);
    }
  });
});

$("#tabla_vacunas").on("click", ".activar", function () {
  //esto esta extrayendo los datos de la tabla el (data)
  var data = tabla_vacunas.row($(this).parents("tr")).data(); //a que fila deteta que doy click
  //esta condicion es importante para el responsibe porque salda un error si no lo pongo
  if (tabla_vacunas.row(this).child.isShown()) {
    //esto es cuando esta en tamaño responsibo
    var data = tabla_vacunas.row(this).data();
  }
  var dato = 1;
  var id = data.id;

  Swal.fire({
    title: "Cambiar estado?",
    text: "El estado de la vacuna se cambiará!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, cambiar!",
  }).then((result) => {
    if (result.isConfirmed) {
      cambiar_estado_vacuna(id, dato);
    }
  });
});

function cambiar_estado_vacuna(id, dato) {
  var res = "";
  if (dato == 1) {
    res = "activo";
  } else {
    res = "inactivo";
  }

  $.ajax({
    url: "/vacunas/estado_vacuna",
    type: "POST",
    data: { id: id, dato: dato },
  }).done(function (response) {
    if (response > 0) {
      if (response == 1) {
        tabla_vacunas.ajax.reload();
        return Swal.fire(
          "Estado de la vacuna",
          "EL estado se " + res + " con extio",
          "success"
        );
      }
    } else {
      return Swal.fire(
        "Estado de la vacuna",
        "No se pudo cambiar el estado, error en la matrix",
        "error"
      );
    }
  });
}

$("#tabla_vacunas").on("click", ".editar", function () {
  //esto esta extrayendo los datos de la tabla el (data)
  var data = tabla_vacunas.row($(this).parents("tr")).data(); //a que fila deteta que doy click
  //esta condicion es importante para el responsibe porque salda un error si no lo pongo
  if (tabla_vacunas.row(this).child.isShown()) {
    //esto es cuando esta en tamaño responsibo
    var data = tabla_vacunas.row(this).data();
  }

  $("#id_vacuna_editt").val(data.id);
  $("#codigo_vacuna_edi").val(data.codigo);
  $("#nombre_edi").val(data.nombre);
  $("#tipo_id_edi").val(data.tipo_id).trigger("change");
  $("#cantidad_edi").val(data.cantidad);
  $("#precio_c_edi").val(data.precio);
  $("#detalle_a_edi").val(data.detalle);
  $("#presentacion_edit").val(data.presentacion);

  $("#registro_sani_edit").val(data.registro_sani);
  $("#cantidad_dosis_edit").val(data.cantidad_dosis);


  $("#codigo_oblig_edi").html("");
  $("#nombre_obligg_edi").html("");
  $("#tipo_obligg_edi").html("");
  $("#cantidad_obligg_edi").html("");
  $("#precio_obligg_edi").html("");
  $("#detalle_obligg_edi").html("");
  $("#presentacion_edit_obligg").html("");
  $("#registro_sani_edit_obligg").html("");
  $("#cantidad_dosis_edit_obligg").html("");

  $("#modal_editar_vacuna").modal({ backdrop: "static", keyboard: false });
  $("#modal_editar_vacuna").modal("show");
});

function editar_vacuna() {
  var id = $("#id_vacuna_editt").val();
  var codigo = $("#codigo_vacuna_edi").val();
  var nombre = $("#nombre_edi").val();
  var tipo = $("#tipo_id_edi").val();
  var cantidad = $("#cantidad_edi").val();
  var precio = $("#precio_c_edi").val();
  var detalle = $("#detalle_a_edi").val();
  var presentacion = $("#presentacion_edit").val();

  var registro_sani = $("#registro_sani_edit").val();
  var cantidad_dosis = $("#cantidad_dosis_edit").val();

  if (
    codigo.length == 0 ||
    codigo.trim() == "" ||
    nombre.length == 0 ||
    nombre.trim() == "" ||
    tipo == 0 ||
    tipo.trim() == "0" ||
    cantidad < 0 ||
    cantidad.trim() == "" ||
    precio < 0 ||
    precio.trim() == "" ||
    detalle.length == 0 ||
    detalle.trim() == "" ||
    presentacion.length == 0 ||
    presentacion.trim() == "" ||
    registro_sani.length == 0 ||
    registro_sani.trim() == "" ||
    cantidad_dosis.length == 0 ||
    cantidad_dosis.trim() == ""
  ) {
    validar_editar_vacuna(
      codigo,
      nombre,
      tipo,
      cantidad,
      precio,
      detalle,
      presentacion,
      registro_sani,
      cantidad_dosis
    );

    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#codigo_oblig_edi").html("");
    $("#nombre_obligg_edi").html("");
    $("#tipo_obligg_edi").html("");
    $("#cantidad_obligg_edi").html("");
    $("#precio_obligg_edi").html("");
    $("#detalle_obligg_edi").html("");
    $("#presentacion_edit_obligg").html("");
    $("#registro_sani_edit_obligg").html("");
    $("#cantidad_dosis_edit_obligg").html("");
  }

  var formdata = new FormData();
  formdata.append("id", id);
  formdata.append("codigo", codigo);
  formdata.append("nombre", nombre);
  formdata.append("tipo", tipo);
  formdata.append("cantidad", cantidad);
  formdata.append("precio", precio);
  formdata.append("detalle", detalle);
  formdata.append("presentacion", presentacion);

  formdata.append("registro_sani", registro_sani);
  formdata.append("cantidad_dosis", cantidad_dosis);

  $.ajax({
    url: "/vacunas/editar_vacuna",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {

          $(".bg-primary").LoadingOverlay("hide");
          $("#modal_editar_vacuna").modal("hide");
          tabla_vacunas.ajax.reload();
          return Swal.fire(
            "Vacuna editada con éxito",
            "La vacuna se edito con éxito",
            "success"
          );

        } else if (resp == 2) {

          $(".bg-primary").LoadingOverlay("hide");
          return Swal.fire(
            "Codigo ya existe",
            "El codigo '" + codigo + "', ya existe en el sistema",
            "warning"
          );

        }
      } else {

        $(".bg-primary").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo editar la vacuna, falla en la matrix",
          "error"
        );

      }
    },
    beforeSend: function () {
      $(".bg-primary").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

function validar_editar_vacuna(
  codigo,
  nombre,
  tipo,
  cantidad,
  precio,
  detalle,
  presentacion,
  registro_sani,
  cantidad_dosis
) {
  if (codigo.length == 0 || codigo.trim() == "") {
    $("#codigo_oblig_edi").html("Ingrese código");
  } else {
    $("#codigo_oblig_edi").html("");
  }

  if (nombre.length == 0 || nombre.trim() == "") {
    $("#nombre_obligg_edi").html("Ingrese nombre de la vacuna");
  } else {
    $("#nombre_obligg_edi").html("");
  }

  if (tipo == 0 || tipo.trim() == "") {
    $("#tipo_obligg_edi").html("Ingrese el tipo de vacuna");
  } else {
    $("#tipo_obligg_edi").html("");
  }

  if (cantidad < 0 || cantidad.trim() == "") {
    $("#cantidad_obligg_edi").html("Ingrese la cantidad");
  } else {
    $("#cantidad_obligg_edi").html("");
  }

  if (precio < 0 || precio.trim() == "") {
    $("#precio_obligg_edi").html("Ingrese el precio");
  } else {
    $("#precio_obligg_edi").html("");
  }

  if (detalle.length == 0 || detalle.trim() == "") {
    $("#detalle_obligg_edi").html("Ingrese el detalle de la vacuna");
  } else {
    $("#detalle_obligg_edi").html("");
  }

  if (presentacion.length == 0 || presentacion.trim() == "") {
    $("#presentacion_edit_obligg").html("Ingrese la presentación");
  } else {
    $("#presentacion_edit_obligg").html("");
  }

  if (registro_sani.length == 0 || registro_sani.trim() == "") {
    $("#cantidad_dosis_edit_obligg").html("Ingrese cantidad de dosis");
  } else {
    $("#cantidad_dosis_edit_obligg").html("");
  }

  if (cantidad_dosis.length == 0 || cantidad_dosis.trim() == "") {
    $("#registro_sani_edit_obligg").html("Ingrese registro sanitario");
  } else {
    $("#registro_sani_edit_obligg").html("");
  }
}

$("#tabla_vacunas").on("click", ".photo", function () {
  //esto esta extrayendo los datos de la tabla el (data)
  var data = tabla_vacunas.row($(this).parents("tr")).data(); //a que fila deteta que doy click
  //esta condicion es importante para el responsibe porque salda un error si no lo pongo
  if (tabla_vacunas.row(this).child.isShown()) {
    //esto es cuando esta en tamaño responsibo
    var data = tabla_vacunas.row(this).data();
  }

  var id = data.id;
  var foto = data.foto;

  $("#id_cerdo_foto").val(id);
  $("#foto_actu_c").val(foto);
  $("#img_cerdo").attr("src", "static/uploads/vacuna/" + foto);

  $("#foto_new_c").val("");

  $("#modal_editar_foto_vacuna").modal({ backdrop: "static", keyboard: false });
  $("#modal_editar_foto_vacuna").modal("show");
});

function editar_foto_vacuna() {
  var id = document.getElementById("id_cerdo_foto").value;
  var foto = document.getElementById("foto_new_c").value;
  var ruta_actual = document.getElementById("foto_actu_c").value;

  if (foto == "" || ruta_actual.length == 0 || ruta_actual == "") {
    return swal.fire(
      "Mensaje de advertencia",
      "Ingrese una imagen para actualizar",
      "warning"
    );
  }

  var formdata = new FormData();
  var foto = $("#foto_new_c")[0].files[0];

  formdata.append("id", id);
  formdata.append("foto", foto);
  formdata.append("ruta_actual", ruta_actual);

  $.ajax({
    url: "/vacunas/cambiar_foto_vacuna",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {

      if (resp > 0) {
        if (resp == 1) {

          $(".modal-body").LoadingOverlay("hide");
          document.getElementById("foto_new_c").value = "";
          tabla_vacunas.ajax.reload();

          $("#modal_editar_foto_vacuna").modal("hide");
          return Swal.fire(
            "Foto cambiada",
            "La foto de la vacuna se cambio con éxito",
            "success"
          );

        }
      } else {
        $(".modal-body").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "Error al cambiar la foto de la vacuna",
          "error"
        );
      }
    },
    beforeSend: function () {
      $(".modal-body").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

///////////////////
//// Vacunacion
function registra_vacunacion() {
  Swal.fire({
    title: 'Guardar registro?',
    text: "El registro se guardará en el sistema!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, guardar!'
  }).then((result) => {
    if (result.isConfirmed) {
      guardar_registro_vacunacion();
    }
  })
}

function guardar_registro_vacunacion() {
  var cerdo_id = $("#cerdo_id").val();
  var fecha = $("#fecha_r").val();
  var observacion = $("#observacion").val();
  var count = 0;

  if (
    cerdo_id == '0' ||
    cerdo_id.trim() == "0" ||
    fecha.length == 0 ||
    fecha.trim() == "" ||
    observacion.length == 0 ||
    observacion.trim() == ""
  ) {
    validar_registro_vacunas(
      cerdo_id,
      fecha,
      observacion
    );

    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#cerdo_obligg").html("");
    $("#fecha_obligg").html("");
    $("#observacion_obligg").html("");
  }

  $("#tabla_vacunacion tbody#tbody_tabla_vacunacion tr").each(function () {
    count++;
  }
  );

  if (count == 0) {
    $("#unir_no_hay").html('<span class="badge badge-danger"><b>.:No hay vacuna en el detalle:.</b></span>');
    return swal.fire(
      "Detalle vacío",
      "No hay vacuna en el detalle",
      "warning"
    );
  } else {
    $("#unir_no_hay").html("");
  }

  var formdata = new FormData();
  //est valores son como los que van en la data del ajax
  formdata.append("cerdo_id", cerdo_id);
  formdata.append("fecha", fecha);
  formdata.append("observacion", observacion);

  $.ajax({
    url: "/vacunas/registro_vacunacion_cerdo",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {

      if (resp > 0) {
        registrar_detalle_vacunacion(parseInt(resp));
      } else {
        $(".card-success").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo crear la vacunación del cerdo, falla en la matrix",
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

function validar_registro_vacunas(
  cerdo_id,
  fecha,
  observacion
) {
  if (cerdo_id == '0' ||
    cerdo_id.trim() == "0") {
    $("#cerdo_obligg").html("Seleccione el cerdo");
  } else {
    $("#cerdo_obligg").html("");
  }

  if (fecha.length == 0 ||
    fecha.trim() == "") {
    $("#fecha_obligg").html("Ingrese la fecha");
  } else {
    $("#fecha_obligg").html("");
  }

  if (observacion.length == 0 ||
    observacion.trim() == "") {
    $("#observacion_obligg").html("Ingrese observación");
  } else {
    $("#observacion_obligg").html("");
  }
}

function registrar_detalle_vacunacion(id) {
  var count = 0;
  var arrego_id = new Array();
  var arreglo_fecha = new Array();
  var arreglo_cantidad = new Array();
  var arreglo_motivo = new Array();

  $("#tabla_vacunacion tbody#tbody_tabla_vacunacion tr").each(
    function () {
      arrego_id.push($(this).find("td").eq(0).text());
      arreglo_fecha.push($(this).find("td").eq(1).text());
      arreglo_cantidad.push($(this).find("td").eq(3).text());
      arreglo_motivo.push($(this).find("td").eq(4).text());
      count++;
    }
  );

  //aqui combierto el arreglo a un string
  var idv = arrego_id.toString();
  var fecha = arreglo_fecha.toString();
  var cantidad = arreglo_cantidad.toString();
  var motivo = arreglo_motivo.toString();

  if (count == 0) {
    return false;
  }

  $.ajax({
    url: "/vacunas/registro_detalle_vacunacion_cerdo",
    type: "POST",
    data: {
      id: id,
      idv: idv,
      fecha: fecha,
      cantidad: cantidad,
      motivo: motivo
    },
  }).done(function (resp) {
    if (resp > 0) {

      if (resp == 1) {
        $(".card-success").LoadingOverlay("hide");
        cargar_contenido("contenido_principal", "/registro_vacunacion");
        return Swal.fire(
          "Vacunación del cerdo creado con éxito",
          "La vacunación del cerdo se creo con éxito",
          "success"
        );
      }

    } else {

      return Swal.fire(
        "Error",
        "No se pudo crear el detalle de vacunación, falla en la matrix",
        "error"
      );

    }
  });
}

function anular_vacunacion_cerdo(id) {
  Swal.fire({
    title: "Anular la vacunación del cerdo?",
    text: "La vacunación se anulará!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, anular!",
  }).then((result) => {
    if (result.isConfirmed) {
      vacunacion_cerdo_anular(id);
    }
  });
}

function vacunacion_cerdo_anular(id) {
  $.ajax({
    url: "/vacunas/anular_vacunacion_cerdo",
    type: "POST",
    data: { id: id },
  }).done(function (response) {

    if (response > 0) {

      if (response == 1) {
        cargar_contenido('contenido_principal', '/listado_vacunacion');
        return Swal.fire(
          "Vacunación anulada",
          "La vacunación se anulo con extio",
          "success"
        );
      }

    } else {
      return Swal.fire(
        "Error",
        "No se pudo anular la vacunación, error en la matrix",
        "error"
      );
    }
  });
}

function ver_detalle_vacunas_cerdo(id) {
  $.ajax({
    url: "/vacunas/ver_detalle_vacunas_cerdo",
    type: "POST",
    data: { id: id },
    success: function (resp) {

      $('#tbody_tabla_vacunas_detalle').empty();

      if (resp != 0) {
        var llenat = "";
        var count = 0;

        resp["data"].forEach((row) => {
          count++;
          llenat += `<tr>
                      <td> ${count} </td>
                      <td> ${row['fecha']} </td>  
                      <td> ${row['vacuna']} </td>
                      <td> ${row['cantidad']} </td>  
                      <td> ${row['motivo']} </td> 
                    </tr>`;
          $("#tbody_tabla_vacunas_detalle").html(llenat);
        });
      }

      $("#modal_detalle_vacunasa").modal({ backdrop: "static", keyboard: false });
      $("#modal_detalle_vacunasa").modal("show");
    },
  });
}

///////////////////
//// Vacunacion
function registra_desparasitacion() {
  Swal.fire({
    title: 'Guardar registro?',
    text: "El registro se guardará en el sistema!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, guardar!'
  }).then((result) => {
    if (result.isConfirmed) {
      guardar_registro_desprasitacion();
    }
  })
}

function guardar_registro_desprasitacion() {
  var cerdo_id = $("#cerdo_id").val();
  var fecha = $("#fecha_r").val();
  var observacion = $("#observacion").val();
  var count = 0;

  if (
    cerdo_id == '0' ||
    cerdo_id.trim() == "0" ||
    fecha.length == 0 ||
    fecha.trim() == "" ||
    observacion.length == 0 ||
    observacion.trim() == ""
  ) {
    validar_registro_desprasitacion(
      cerdo_id,
      fecha,
      observacion
    );

    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#cerdo_obligg").html("");
    $("#fecha_obligg").html("");
    $("#observacion_obligg").html("");
  }

  $("#tabla_desparasitacion tbody#tbody_tabla_desparasitacion tr").each(function () {
    count++;
  }
  );

  if (count == 0) {
    $("#unir_no_hay").html('<span class="badge badge-danger"><b>.:No hay medicina o desparasitante en el detalle:.</b></span>');
    return swal.fire(
      "Detalle vacío",
      "No hay medicina o desparasitantes en el detalle",
      "warning"
    );
  } else {
    $("#unir_no_hay").html("");
  }

  var formdata = new FormData();
  //est valores son como los que van en la data del ajax
  formdata.append("cerdo_id", cerdo_id);
  formdata.append("fecha", fecha);
  formdata.append("observacion", observacion);

  $.ajax({
    url: "/vacunas/registro_desparasitacion_cerdo",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        registrar_detalle_desparasitacion(parseInt(resp));
      } else {
        $(".card-success").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo crear la desprasitación del cerdo, falla en la matrix",
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

function validar_registro_desprasitacion(
  cerdo_id,
  fecha,
  observacion
) {
  if (cerdo_id == '0' ||
    cerdo_id.trim() == "0") {
    $("#cerdo_obligg").html("Seleccione el cerdo");
  } else {
    $("#cerdo_obligg").html("");
  }

  if (fecha.length == 0 ||
    fecha.trim() == "") {
    $("#fecha_obligg").html("Ingrese la fecha");
  } else {
    $("#fecha_obligg").html("");
  }

  if (observacion.length == 0 ||
    observacion.trim() == "") {
    $("#observacion_obligg").html("Ingrese observación");
  } else {
    $("#observacion_obligg").html("");
  }
}

function registrar_detalle_desparasitacion(id) {
  var count = 0;
  var arrego_id = new Array();
  var arreglo_fecha = new Array();
  var arreglo_cantidad = new Array();
  var arreglo_motivo = new Array();

  $("#tabla_desparasitacion tbody#tbody_tabla_desparasitacion tr").each(
    function () {
      arrego_id.push($(this).find("td").eq(0).text());
      arreglo_fecha.push($(this).find("td").eq(1).text());
      arreglo_cantidad.push($(this).find("td").eq(3).text());
      arreglo_motivo.push($(this).find("td").eq(4).text());
      count++;
    }
  );

  //aqui combierto el arreglo a un string
  var idv = arrego_id.toString();
  var fecha = arreglo_fecha.toString();
  var cantidad = arreglo_cantidad.toString();
  var motivo = arreglo_motivo.toString();

  if (count == 0) {
    return false;
  }

  $.ajax({
    url: "/vacunas/registro_detalle_desparasitacion_cerdo",
    type: "POST",
    data: {
      id: id,
      idv: idv,
      fecha: fecha,
      cantidad: cantidad,
      motivo: motivo
    },
  }).done(function (resp) {
    if (resp > 0) {

      if (resp == 1) {
        $(".card-success").LoadingOverlay("hide");
        cargar_contenido("contenido_principal", "/registro_desparasitacion");
        return Swal.fire(
          "Desparasitación del cerdo creado con éxito",
          "La desparasitación del cerdo se creo con éxito",
          "success"
        );
      }

    } else {

      return Swal.fire(
        "Error",
        "No se pudo crear el detalle de desparasitación, falla en la matrix",
        "error"
      );

    }
  });
}

function anular_desparasitacion_cerdo(id) {
  Swal.fire({
    title: "Anular la desparasitación del cerdo?",
    text: "La desparasitación se anulará!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, anular!",
  }).then((result) => {
    if (result.isConfirmed) {
      desparasitacion_cerdo_anular(id);
    }
  });
}

function desparasitacion_cerdo_anular(id) {
  $.ajax({
    url: "/vacunas/anular_desparasitacion_cerdo",
    type: "POST",
    data: { id: id },
  }).done(function (response) {

    if (response > 0) {

      if (response == 1) {
        cargar_contenido('contenido_principal', '/listado_desparasitacion');
        return Swal.fire(
          "Desparasitación anulada",
          "La desparasitación se anulo con extio",
          "success"
        );
      }

    } else {
      return Swal.fire(
        "Error",
        "No se pudo anular la desparasitación, error en la matrix",
        "error"
      );
    }
  });
}

function ver_detalle_desparsitantes_cerdo(id) {
  $.ajax({
    url: "/vacunas/ver_detalle_desparsitantes_cerdo",
    type: "POST",
    data: { id: id },
    success: function (resp) {

      $('#tbody_tabla_desparasitante_detalle').empty();

      if (resp != 0) {
        var llenat = "";
        var count = 0;

        resp["data"].forEach((row) => {
          count++;
          llenat += `<tr>
                      <td> ${count} </td>
                      <td> ${row['fecha']} </td>  
                      <td> ${row['desparasitante']} </td>
                      <td> ${row['cantidad']} </td>  
                      <td> ${row['motivo']} </td> 
                    </tr>`;
          $("#tbody_tabla_desparasitante_detalle").html(llenat);
        });
      }

      $("#modal_detalle_desparasitante").modal({ backdrop: "static", keyboard: false });
      $("#modal_detalle_desparasitante").modal("show");
    },
  });
}