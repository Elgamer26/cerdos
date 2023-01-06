function datos_usuarios_logeo() {
  $.ajax({
    type: "GET",
    url: "/usuario/datos_usuarios_logeo",
    success: function (response) {
      if (response != "" || response != null) {
        $("#nombres_l_l").html(response[1]);
        $("#rol_l").html(response[10]);
        $("#imagen_l_1").attr("src", "/static/uploads/usuario/" + response[8]);
        $("#img_l_2").attr("src", "/static/uploads/usuario/" + response[8]);

        $("#img_usuario_l").attr(
          "src",
          "/static/uploads/usuario/" + response[8]
        );
        $("#foto_actu_l").val(response[8]);

        $("#nombres_l").val(response[1]);
        $("#apellidos_l").val(response[2]);
        $("#domicilio_l").val(response[6]);
        $("#telefono_l").val(response[7]);
        $("#usuario_l").val(response[3]);

        $("#correo_l").val(response[11]);
        $("#cedula_l").val(response[12]);

        $("#pass_oculto").val(response[4]);
      }
    },
  });
}

function mostar_perfil() {
  $("#modaleditar_usuario_logeado").modal({
    backdrop: "static",
    keyboard: false,
  });
  $("#modaleditar_usuario_logeado").modal("show");
}

function mostar_foto_l() {
  $("#modal_editar_foto_logeado").modal({
    backdrop: "static",
    keyboard: false,
  });
  $("#modal_editar_foto_logeado").modal("show");
}

function modtar_password_l() {
  $("#modaleditar_password_logeado").modal({
    backdrop: "static",
    keyboard: false,
  });
  $("#modaleditar_password_logeado").modal("show");
}

//// editar usuario
function editar_usuario_loegado() {
  var nombres = $("#nombres_l").val();
  var apellidos = $("#apellidos_l").val();
  var domicilio = $("#domicilio_l").val();
  var telefono = $("#telefono_l").val();
  var usuario = $("#usuario_l").val();
  var correo_l = $("#correo_l").val();
  var cedula_l = $("#cedula_l").val();

  if (
    nombres.length == 0 ||
    nombres.trim() == "" ||
    apellidos.length == 0 ||
    apellidos.trim() == "" ||
    domicilio.length == 0 ||
    domicilio.trim() == "" ||
    telefono.length == 0 ||
    telefono.trim() == "" ||
    usuario.length == 0 ||
    usuario.trim() == "" ||
    correo_l.length == 0 ||
    correo_l.trim() == "" ||
    cedula_l.length == 0 ||
    cedula_l.trim() == ""
  ) {
    validar_registros_usuario_editar_l(
      nombres,
      apellidos,
      domicilio,
      telefono,
      usuario,
      correo_l,
      cedula_l
    );
    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#nombre_oblig_l").html("");
    $("#apellidos_obligg_l").html("");
    $("#domicilio_obligg_l").html("");
    $("#telefono_obligg_l").html("");
    $("#usuario_obligg_l").html("");
    $("#correo_obligg_l").html("");
    $("#cedula_obligg_l").html("");
  }

  if (!G_correo) {
    $("#correo_obligg_l").html("Ingrese un correo correcto");
    return swal.fire(
      "Correo incorrecto",
      "Ingrese un correo correcto",
      "warning"
    );
  } else {
    $("#correo_obligg_l").html("");
  }

  if (!G_cedula) {
    $("#cedula_obligg_l").html("Ingrese una cédula correcta");
    return swal.fire(
      "Cédula incorrecta",
      "Ingrese una cédula correcta",
      "warning"
    );
  } else {
    $("#cedula_obligg_l").html("");
  }

  var formdata = new FormData();
  formdata.append("nombres", nombres);
  formdata.append("apellidos", apellidos);
  formdata.append("domicilio", domicilio);
  formdata.append("telefono", telefono);
  formdata.append("usuario", usuario.trim());
  formdata.append("correo_l", correo_l);
  formdata.append("cedula_l", cedula_l);

  $.ajax({
    url: "/usuario/editar_usuario_logeado",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          $(".modal-body").LoadingOverlay("hide");
          $("#modaleditar_usuario_logeado").modal("hide");
          datos_usuarios_logeo();
          return Swal.fire(
            "Datos editados con éxito",
            "Los datos del usuario se edito con éxito",
            "success"
          );
        } else if (resp == 2) {
          $(".modal-body").LoadingOverlay("hide");
          return Swal.fire(
            "Usuario ya existe",
            "El usuario " + usuario + ", ya existe en el sistema",
            "warning"
          );
        } else if (resp == 3) {
          $(".modal-body").LoadingOverlay("hide");
          return Swal.fire(
            "Correo ya existe",
            "El correo " + correo_l + ", ya existe en el sistema",
            "warning"
          );
        } else if (resp == 4) {
          $(".modal-body").LoadingOverlay("hide");
          return Swal.fire(
            "Cédula ya existe",
            "La cédula " + cedula_l + ", ya existe en el sistema",
            "warning"
          );
        }
      } else {
        $(".modal-body").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo editar el usuario, falla en la matrix",
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

function validar_registros_usuario_editar_l(
  nombres,
  apellidos,
  domicilio,
  telefono,
  usuario,
  correo_l,
  cedula_l
) {
  if (nombres.length == 0 || nombres.trim() == "") {
    $("#nombre_oblig_l").html("Ingrese los nombres");
  } else {
    $("#nombre_oblig_l").html("");
  }

  if (apellidos.length == 0 || apellidos.trim() == "") {
    $("#apellidos_obligg_l").html("Ingrese los apellidos");
  } else {
    $("#apellidos_obligg_l").html("");
  }

  if (domicilio.length == 0 || domicilio.trim() == "") {
    $("#domicilio_obligg_l").html("Ingrese el domicilio");
  } else {
    $("#domicilio_obligg_l").html("");
  }

  if (telefono.length == 0 || telefono.trim() == "") {
    $("#telefono_obligg_l").html("Ingrese el telefono");
  } else {
    $("#telefono_obligg_l").html("");
  }

  if (usuario.length == 0 || usuario.trim() == "") {
    $("#usuario_obligg_l").html("Ingrese el usuario");
  } else {
    $("#usuario_obligg_l").html("");
  }

  if (correo_l.length == 0 || correo_l.trim() == "") {
    $("#correo_obligg_l").html("Ingrese correo");
  } else {
    $("#correo_obligg_l").html("");
  }

  if (cedula_l.length == 0 || cedula_l.trim() == "") {
    $("#cedula_obligg_l").html("Ingrese cédula");
  } else {
    $("#cedula_obligg_l").html("");
  }
}

function editar_foto_usuario_logeado() {
  var foto = document.getElementById("foto_new_l").value;
  var ruta_actual = document.getElementById("foto_actu_l").value;

  if (foto == "" || ruta_actual.length == 0 || ruta_actual == "") {
    return swal.fire(
      "Mensaje de advertencia",
      "Ingrese una imagen para actualizar",
      "warning"
    );
  }

  var formdata = new FormData();
  var foto = $("#foto_new_l")[0].files[0];

  formdata.append("foto", foto);
  formdata.append("ruta_actual", ruta_actual);

  $.ajax({
    url: "/usuario/cambiar_foto_usuario_logeo",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          $(".modal-body").LoadingOverlay("hide");
          document.getElementById("foto_new_l").value = "";
          datos_usuarios_logeo();

          return Swal.fire(
            "Foto cambiada",
            "La foto del usuario se cambio con éxito",
            "success"
          );
        }
      } else {
        $(".modal-body").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "Error al cambiar la foto del usuario",
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

//// editar password
function editar_password_l() {
  var pass_oculto = $("#pass_oculto").val();
  var password_ac = $("#password_ac").val();
  var password_n = $("#password_n").val();
  var confirmar_p = $("#confirmar_p").val();

  if (
    password_ac.length == 0 ||
    password_ac.trim() == "" ||
    password_n.length == 0 ||
    password_n.trim() == "" ||
    confirmar_p.length == 0 ||
    confirmar_p.trim() == ""
  ) {
    validar_password(password_ac, password_n, confirmar_p);
    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#password_ac_oblig").html("");
    $("#password_n_oblig").html("");
    $("#confirmar_p_obligg").html("");
  }

  if (pass_oculto != password_ac) {
    $("#password_ac_oblig").html("Password incorrecto");
    return swal.fire(
      "Password incorrecto",
      "El password ingresado es incorrecto",
      "error"
    );
  } else {
    $("#password_ac_oblig").html("");
  }

  if (password_n != confirmar_p) {
    $("#password_n_oblig").html("Los password no coinciden");
    $("#confirmar_p_obligg").html("Los password no coinciden");
    return swal.fire("Password", "Los password no coinciden", "warning");
  } else {
    $("#password_n_oblig").html("");
    $("#confirmar_p_obligg").html("");
  }

  if (!pass_usus_l) {
    return swal.fire(
      "Password débil",
      "Ingrese un password mas fuerte",
      "warning"
    );
  }

  var formdata = new FormData();
  formdata.append("password_n", password_n.trim());

  $.ajax({
    url: "/usuario/cambiar_password",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          $("#passstrength").html("");
          $("#password_ac").val("");
          $("#password_n").val("");
          $("#confirmar_p").val("");

          $(".modal-body").LoadingOverlay("hide");
          datos_usuarios_logeo();

          return Swal.fire(
            "Password editados con éxito",
            "El password se edito con éxito",
            "success"
          );
        }
      } else {
        $(".modal-body").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo editar el password, falla en la matrix",
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

function validar_password(password_ac, password_n, confirmar_p) {
  if (password_ac.length == 0 || password_ac.trim() == "") {
    $("#password_ac_oblig").html("Ingrese password actual");
  } else {
    $("#password_ac_oblig").html("");
  }

  if (password_n.length == 0 || password_n.trim() == "") {
    $("#password_n_oblig").html("Ingrese password nuevo");
  } else {
    $("#password_n_oblig").html("");
  }

  if (confirmar_p.length == 0 || confirmar_p.trim() == "") {
    $("#confirmar_p_obligg").html("Confirme password nuevo");
  } else {
    $("#confirmar_p_obligg").html("");
  }
}


//////////// fotos de la pagina web
/////////////// subiir fotos de la página web
function subir_foto_1() {
  var foto1 = document.getElementById("foto1").value;
  var foto1_ruta = document.getElementById("foto1_ruta").value;

  if (foto1.length == 0) {
    return swal.fire("No hay foto", "Debe ingresar la foto", "warning");
  }

  var formdata = new FormData();
  var foto = $("#foto1")[0].files[0];
  //est valores son como los que van en la data del ajax

  formdata.append("foto", foto);
  formdata.append("ruta_actual", foto1_ruta);

  $.ajax({
    url: "/web/subir_foto_1",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          cargar_contenido('contenido_principal', '/pag_web');
          return Swal.fire(
            "Imgen subida",
            "La imagen de la web se actualizó con éxito",
            "success"
          );
        }
      } else {
        return Swal.fire(
          "Error",
          "La imagen no se puedo actualizar",
          "error"
        );
      }
    },
  });
  return false;
}

function subir_foto_2() {
  var foto2 = document.getElementById("foto2").value;
  var foto2_ruta = document.getElementById("foto2_ruta").value;

  if (foto2.length == 0) {
    return swal.fire("No hay foto", "Debe ingresar la foto", "warning");
  }

  var formdata = new FormData();
  var foto = $("#foto2")[0].files[0];
  //est valores son como los que van en la data del ajax

  formdata.append("foto", foto);
  formdata.append("ruta_actual", foto2_ruta);

  $.ajax({
    url: "/web/subir_foto_2",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          cargar_contenido('contenido_principal', '/pag_web');
          return Swal.fire(
            "Imgen subida",
            "La imagen de la web se actualizó con éxito",
            "success"
          );
        }
      } else {
        return Swal.fire(
          "Error",
          "La imagen no se puedo actualizar",
          "error"
        );
      }
    },
  });
  return false;
}

function subir_foto_3() {
  var foto3 = document.getElementById("foto3").value;
  var foto3_ruta = document.getElementById("foto3_ruta").value;

  if (foto3.length == 0) {
    return swal.fire("No hay foto", "Debe ingresar la foto", "warning");
  }

  var formdata = new FormData();
  var foto = $("#foto3")[0].files[0];
  //est valores son como los que van en la data del ajax

  formdata.append("foto", foto);
  formdata.append("ruta_actual", foto3_ruta);

  $.ajax({
    url: "/web/subir_foto_3",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          cargar_contenido('contenido_principal', '/pag_web');
          return Swal.fire(
            "Imgen subida",
            "La imagen de la web se actualizó con éxito",
            "success"
          );
        }
      } else {
        return Swal.fire(
          "Error",
          "La imagen no se puedo actualizar",
          "error"
        );
      }
    },
  });
  return false;
}

function editar_detalle_foto() {
  var detalle1 = $("#detalle_1").val();
  var detalle2 = $("#detalle_2").val();
  var detalle3 = $("#detalle_3").val();

  if (detalle1.length == 0 || detalle2.length == 0 || detalle3.length == 0 ||
    detalle1.trim() == "" || detalle2.trim() == "" || detalle3.trim() == "") {
    if (detalle1.length == 0 || detalle1.trim() == "") {
      $("#lbldetalle_1").html("Ingrese detalle");
    } else {
      $("#lbldetalle_1").html("");
    }

    if (detalle2.length == 0 || detalle2.trim() == "") {
      $("#lbldetalle_2").html("Ingrese detalle");
    } else {
      $("#lbldetalle_2").html("");
    }

    if (detalle3.length == 0 || detalle3.trim() == "") {
      $("#lbldetalle_3").html("Ingrese detalle");
    } else {
      $("#lbldetalle_3").html("");
    }

    return swal.fire("Campos vacios", "NO debe dejar campos de texto vacios", "warning");
  } else {
    $("#lbldetalle_1").html("");
    $("#lbldetalle_2").html("");
    $("#lbldetalle_3").html("");
  }

  $.ajax({
    url: "/web/detalle_de_web",
    type: "POST",
    data: {
      detalle1: detalle1,
      detalle2: detalle2,
      detalle3: detalle3
    },
  }).done(function (resp) {
    if (resp > 0) {
      if (resp == 1) {
        cargar_contenido('contenido_principal', '/pag_web');
        return Swal.fire(
          "Datos actualizados",
          "Los datos se actualizarón con éxito",
          "success"
        );
      }
    } else {
      return Swal.fire(
        "Error",
        "No se puedo actualizar los datos",
        "error"
      );
    }
  });
}

var tabla_lote_alimento_exper, tabla_lote_vacunas_exper, listar_lote_desparasitante_expirar, tabla_lote_insumo_exper;
var fecha_lote_1, fecha_lote_2;

fecha = new Date();
fecha_2 = new Date();

fecha.setDate(fecha.getDate() + 20);
fecha_lote_1 = fecha.getFullYear() + "-" + (fecha.getMonth() + 1) + "-" + fecha.getDate();

fecha_2.setDate(fecha_2.getDate() + 30);
fecha_lote_2 = fecha_2.getFullYear() + "-" + (fecha_2.getMonth() + 1) + "-" + fecha_2.getDate();

////////////////// listar el lote de alimentos por expirar
function listar_lote_alimento_expirar() {
  tabla_lote_alimento_exper = $("#tabla_lote_alimento_exper").DataTable({
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
      url: "/alimento/listar_lote_alimento",
      type: "GET",
    },
    //hay que poner la misma cantidad de columnas y tambien en el html
    columns: [
      { data: "codigo" },
      {
        data: "fecha_f",
        render: function (data, type, row) {
          if (data <= fecha_lote_1) {
            return "<span class='badge badge-danger'>" + data + "</span>";
          }
          if (data > fecha_lote_1 && fecha_lote_2 > data) {
            return "<span class='badge badge-warning'>" + data + " </span>";
          }
          return "<span class='badge badge-success'>" + data + " </span>";
        },
      },
      { data: "nombre" },
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
    order: [[1, 'asc']]
  });

}

function listar_lote_vacunas_expirar() {
  tabla_lote_vacunas_exper = $("#tabla_lote_vacunas_expe").DataTable({
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
      { data: "codigo" },
      {
        data: "fecha_f",
        render: function (data, type, row) {
          if (data <= fecha_lote_1) {
            return "<span class='badge badge-danger'>" + data + "</span>";
          }
          if (data > fecha_lote_1 && fecha_lote_2 > data) {
            return "<span class='badge badge-warning'>" + data + " </span>";
          }
          return "<span class='badge badge-success'>" + data + " </span>";
        },
      },
      { data: "nombre" },
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
    order: [[1, 'asc']]
  });

}

function listar_lote_desparasitante_expirar() {
  tabla_lote_desparasitante_exper = $("#tabla_lote_desaparasitantes_expe").DataTable({
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
      url: "/compras/listar_lote_medicmaneto",
      type: "GET",
    },
    //hay que poner la misma cantidad de columnas y tambien en el html
    columns: [
      { data: "codigo" },
      {
        data: "fecha_f",
        render: function (data, type, row) {
          if (data <= fecha_lote_1) {
            return "<span class='badge badge-danger'>" + data + "</span>";
          }
          if (data > fecha_lote_1 && fecha_lote_2 > data) {
            return "<span class='badge badge-warning'>" + data + " </span>";
          }
          return "<span class='badge badge-success'>" + data + " </span>";
        },
      },
      { data: "medicamento" },
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
    order: [[1, 'asc']]
  });

}

function listar_lote_insumo_expirar() {
  tabla_lote_insumo_exper = $("#tabla_lote_insumo_exper").DataTable({
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
      url: "/compras/listar_lote_insumos",
      type: "GET",
    },
    //hay que poner la misma cantidad de columnas y tambien en el html
    columns: [
      { data: "codigo" },
      {
        data: "fecha_f",
        render: function (data, type, row) {
          if (data <= fecha_lote_1) {
            return "<span class='badge badge-danger'>" + data + "</span>";
          }
          if (data > fecha_lote_1 && fecha_lote_2 > data) {
            return "<span class='badge badge-warning'>" + data + " </span>";
          }
          return "<span class='badge badge-success'>" + data + " </span>";
        },
      },
      { data: "insumo" },
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
    order: [[1, 'asc']]
  });

}

//// listar calendaris
function listar_calendario_dasboard() {
  var n = new Date();
  var y = n.getFullYear();
  var m = n.getMonth() + 1;
  var d = n.getDate();
  if (d < 10) {
    d = '0' + d;
  }
  if (m < 10) {
    m = '0' + m;
  }
  var dia = y + "-" + m + "-" + d;

  $("#calendar_dasboard").fullCalendar({
    height: 650,
    header: {
      language: 'es',
      left: 'prev,next today',
      center: 'title',
      right: 'month,listWeek'
    },
    defaultDate: dia,
    editable: true,
    eventLimit: true, // allow "more" link when too many events
    selectHelper: true,
    selectable: true,
    //-----------------
    customButtons: {
      // este boton yo lo cree
      Miboton: {
        text: "Boton 1",
        click: function () {
          alert("Acciom del boton");
        }
      }
    },

    //esto es para obtener los valores de dia fecha y cambir de color
    dayClick: function (date, jsEvent, view) {
      return Swal.fire(
        "Fecha seleccionada",
        "La fecha seleccionada es: " + date.format() + "",
        "info"
      );
    },

    events: "/vacunas/listar_calendario",

    //este funcion mostrara los datos del evento seleccionado del cintillo
    eventClick: function (calEvent, jsEvent, view) {

      $("#titulo_evento_editar").html("Fecha de evento: " + moment(calEvent.start).format("YYYY-MM-DD"));
      $("#evento_titulo_dasboard").val(calEvent.title);
      $("#galpon_cerdo_dasboardt").val(calEvent.galpon_cerdo);
      $("#fecha_evento_dasboard").val(moment(calEvent.start).format("YYYY-MM-DD"));
      $("#descripcion_dasboard").val(calEvent.descripcion);
      $("#tipo_dasboard").val(calEvent.tipo);

      $("#color_dasboard").val(calEvent.textColor);
      $("#color_etiqueta_dasboard").val(calEvent.color);

      $("#modal_canlendario_dasboard").modal({
        backdrop: "static",
        keyboard: false,
      });
      $("#modal_canlendario_dasboard").modal("show");
    },

  });
}


///////////// permisos del usuario logeado
function obtener_permisos_del_usuaro_logeado() {

  $.ajax({
    url: "/usuario/obterner_permiso_usuario_logeado",
    type: "GET",
    success: function (data) {

      data[2].toString() == "true"
        ? ($(".usuario_p_lo").show())
        : ($(".usuario_p_lo").hide());

      data[3].toString() == "true"
        ? ($(".configuracion_p_lo").show())
        : ($(".configuracion_p_lo").hide());

      data[4].toString() == "true"
        ? ($(".cerdos_p_lo").show())
        : ($(".cerdos_p_lo").hide());

      data[5].toString() == "true"
        ? ($(".galpones_p_lo").show())
        : ($(".galpones_p_lo").hide());

      data[6].toString() == "true"
        ? ($(".comppras_ventas_p_lo").show())
        : ($(".comppras_ventas_p_lo").hide());

      data[7].toString() == "true"
        ? ($(".alimentacion_p_lo").show())
        : ($(".alimentacion_p_lo").hide());

      data[8].toString() == "true"
        ? ($(".vacuna_desparasita_p_lo").show())
        : ($(".vacuna_desparasita_p_lo").hide());

      data[9].toString() == "true"
        ? ($(".enfermedad_trata_p_lo").show())
        : ($(".enfermedad_trata_p_lo").hide());

      data[10].toString() == "true"
        ? ($(".informes_p_lo").show())
        : ($(".informes_p_lo").hide());

    }
  });
  return false;
}

//// traer detalle del cerdo
function ver_detalle_cerdo(id) {

  $.ajax({
    url: "/cerdo/ver_detalle_cerdo",
    type: "POST",
    data: { id: id },
    success: function (data) {

      $("#raza_cerdo").html(data[3]);
      $("#peso_cerdo").html("Peso: " + data[4] + " Kg");
      $("#sexo_cerdo").html("Sexo: " + data[2]);
      $("#etap_cerdo").html("Etapa: " + data[7]);
      $("#detalle_cerdo").html("<b>Detalle del cerdo:</b> " + data[5]);
      $("#unir_imagen").html(`<img id="imagen_cerdo_detalle" src="static/uploads/cerdo/${data[6]}" style="border-radius: 20px;"
      width="550" height="400" alt="IMAGEN DEL CERDO" />`);
      $("#agregar_carrito").html(`<div class="flex-w flex-r-m p-b-10">
          <div class="size-204 flex-w flex-m respon6-next">
            <button onclick="Enviar_cerdo_local(${id},'${data[3]}',${data[4]},'${data[6]}');" class="flex-c-m stext-101 cl0 size-101 bg1 bor1 hov-btn1 p-lr-15 trans-04">
              Agregar al carrito <i class="fa fa-shopping-cart" style="width: 40px; font-size: 20px;"></i>
            </button>
          </div>
        </div>`);

    }
  });
  return false;
}

function Enviar_cerdo_local(id, raza, peso, foto) {
  var id_cerdo;
  var valor_cerdo;
  valor_cerdo = RecuperarLocal();
  valor_cerdo.forEach(animal => {
    if (animal.id === id) {
      id_cerdo = animal.id;
    }
  });

  if (id_cerdo === id) {
    swal(
      'Cerdo dentro de carrito',
      'El cerdo seleccionado ya esta dentro de carrito!!',
      'warning'
    )
    return false;
  }

  let valor = { "id": id, "raza": raza, "peso": peso, "foto": foto }
  agregarCarrtio(valor);
}

function RecuperarLocal() {
  let cerdo;
  if (localStorage.getItem('cerdo_dentro') === null) {
    cerdo = [];
  } else {
    cerdo = JSON.parse(localStorage.getItem('cerdo_dentro'));
  }
  return cerdo;
}

function agregarCarrtio(id) {
  let cerdo;
  cerdo = RecuperarLocal();
  cerdo.push(id);
  localStorage.setItem('cerdo_dentro', JSON.stringify(cerdo));
  swal(
    'Cerdo agregado al carrito',
    'El cerdo seleccionado se agregó al carrito!!',
    'success'
  )
}

$(document).on('click', '#vaciar_carrito', function (e) {
  e.preventDefault();

  var cerdo;
  cerdo = RecuperarLocal();

  if (cerdo.length == 0) {
    return swal(
      'El carrito esta vacio!',
      'No hay cerdo en carrito.',
      'warning'
    )
  }

  alertify.confirm("Vaciar carrito de pedidos.", "Los cerdos se borraran del detalle de forma permanente",
    function () {
      localStorage.clear();
      swal(
        'Carrito vaciado!',
        'El carrito se vacio de forma correcta.',
        'success'
      )
      Mostra_carrito();
    },
    function () {
      alertify.error('Cancel');
    });

})

function Mostra_carrito() {
  let valor;
  valor = RecuperarLocal();
  let html = "";
  var total = 0;
  var subtotal = 0;
  $("#unir_detale_tabla").html("");
  valor.forEach(row => {
    total = parseFloat(row['peso'] * 5).toFixed(2);
    html += `<tr class="table_row">
    <td hidden>${row['id']}</td>
    <td class="column-1"><a class="btn btn-danger" onclick="Eliminar_cerdo_Ls(${row['id']});" style="cursor: pointer;"> <i class="fa fa-trash" style="color: white;"></i> </a></td>
    <td class="column-1">${row['raza']}</td>
    <td class="column-2"> <img Src="/static/uploads/cerdo/${row['foto']}" style="border-radius: 20px;"
    height="100" width="100" alt="${row['foto']}"/></td>
    <td class="column-3">${row['peso']}</td>
    <td class="column-3"> 5 </td>
    <td class="column-5">${total}</td>
    </tr>`;
    subtotal = parseFloat(subtotal) + parseFloat(total);
    $("#unir_detale_tabla").html(html);
  });
  $("#subtotal_unir").html(parseFloat(subtotal).toFixed(2));

  var iva = 0;
  var fulltotal = 0;
  iva = parseFloat(subtotal) * 0.12;
  fulltotal = parseFloat(iva) + parseFloat(subtotal);

  $("#iva_unir").html(parseFloat(iva).toFixed(2));
  $("#full_total").html(parseFloat(fulltotal).toFixed(2));
}

function Eliminar_cerdo_Ls(id) {
  alertify.confirm("Borrar cerdo del detalle.", "El cerdo se borrará del detalle de forma permanente",
    function () {
      let cerdo;
      cerdo = RecuperarLocal();
      cerdo.forEach(function (valor, indice) {
        if (valor.id === id) {
          cerdo.splice(indice, 1);
        }
      });
      localStorage.setItem('cerdo_dentro', JSON.stringify(cerdo));
      Mostra_carrito();
    },
    function () {
      alertify.error('Cancel');
    });
}

$(document).on('click', "#btn_procesar_pedido", function (e) {
  e.preventDefault();

  var nombre = $("#nombre_cli").val();
  var apellido = $("#apellido_cli").val();
  var telefono = $("#telefono_cli").val();
  var cedula = $("#cedula_cli").val();
  var correo = $("#correo_cli").val();
  var direccion = $("#direccion_cli").val();

  var count = 0;

  $("#tabla_pediddo tbody#unir_detale_tabla tr").each(function () {
    count++;
  });

  if (count == 0) {
    return swal(
      "Detalle pedido esta vacio",
      "No hay cerdos en el detalle de pedidos",
      "warning"
    );
  }

  if (!correo_pedido) {
    return swal(
      "Correo inválido",
      "El correo ingresado es incorrecto",
      "warning"
    );
  }

  if (nombre.trim() == "" || nombre.length == 0 ||
    apellido.trim() == "" || apellido.length == 0 ||
    telefono.trim() == "" || telefono.length == 0 ||
    cedula.trim() == "" || cedula.length == 0 ||
    correo.trim() == "" || correo.length == 0 ||
    direccion.trim() == "" || direccion.length == 0) {
    validar_datos_pedidos(nombre, apellido, telefono, cedula, correo, direccion);

    return swal(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#nombres_obligg").html("");
    $("#apellidos_obligg").html("");
    $("#telefono_obligg").html("");
    $("#cedulla_obligg").html("");
    $("#correo_obligg").html("");
    $("#direccion_obligg").html("");
  }

  var subtotal = $("#subtotal_unir").text();
  var impuesto = $("#iva_unir").text();
  var total = $("#full_total").text();

  $.ajax({
    type: "POST",
    async: true,
    url: "/venta/procesar_pedidos",
    data: {
      nombre: nombre,
      apellido: apellido,
      telefono: telefono,
      cedula: cedula,
      correo: correo,
      direccion: direccion,
      subtotal: subtotal,
      impuesto: impuesto,
      total: total
    }
  }).done(function (data) {
    if (data > 0) {
      registrar_detalle_pedido(parseInt(data));
      return swal(
        "Enviando información",
        "Enviando información de pedido, espere un momento por favor...",
        ""
      );
    } else {
      return swal(
        "Error de registro",
        "Error de pedido: " + data,
        "error"
      );
    }
  });
});

function validar_datos_pedidos(nombre, apellido, telefono, cedula, correo, direccion) {
  if (nombre.trim() == "" || nombre.length == 0) {
    $("#nombres_obligg").html(" - Ingrese nombres");
  } else {
    $("#nombres_obligg").html("");
  }

  if (apellido.trim() == "" || apellido.length == 0) {
    $("#apellidos_obligg").html(" - Ingrese apellidos");
  } else {
    $("#apellidos_obligg").html("");
  }

  if (telefono.trim() == "" || telefono.length == 0) {
    $("#telefono_obligg").html(" - Ingrese teléfono");
  } else {
    $("#telefono_obligg").html("");
  }

  if (cedula.trim() == "" || cedula.length == 0) {
    $("#cedulla_obligg").html(" - Ingrese cédula");
  } else {
    $("#cedulla_obligg").html("");
  }

  if (correo.trim() == "" || correo.length == 0) {
    $("#correo_obligg").html(" - Ingrese correo");
  } else {
    $("#correo_obligg").html("");
  }

  if (direccion.trim() == "" || direccion.length == 0) {
    $("#direccion_obligg").html(" - Ingrese dirección");
  } else {
    $("#direccion_obligg").html("");
  }

}

function registrar_detalle_pedido(id) {
  var count = 0;
  var arreglo_id = new Array();
  var arreglo_peso = new Array();
  var arreglo_precio = new Array();
  var arreglo_total = new Array();

  $("#tabla_pediddo tbody#unir_detale_tabla tr").each(function () {
    arreglo_id.push($(this).find("td").eq(0).text());
    arreglo_peso.push($(this).find("td").eq(4).text());
    arreglo_precio.push($(this).find("td").eq(5).text());
    arreglo_total.push($(this).find("td").eq(6).text());
    count++;
  });

  var id_cerdo = arreglo_id.toString();
  var peso = arreglo_peso.toString();
  var precio = arreglo_precio.toString();
  var total = arreglo_total.toString();

  if (count == 0) {
    return false;
  }

  $.ajax({
    url: "/venta/registrar_detalle_pedido",
    type: "POST",
    async: true,
    data: {
      id: id,
      id_cerdo: id_cerdo,
      peso: peso,
      precio: precio,
      total: total,
    },
  }).done(function (resp) {
    if (resp > 0) {
      if (resp == 1) {
        localStorage.clear();
        Mostra_carrito();
        return swal(
          "Pedido de cerdos",
          "El pedido se realizó con exito - pedido enviado al correo!",
          "success"
        );
      }
    } else {
      return swal(
        "Error",
        "No se pudo crear el detalle de venta, falla en la matrix" + resp,
        "error"
      );
    }
  });
}