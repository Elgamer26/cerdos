from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_mail import Mail 

from routers.index import index
from routers.usuario import usuario
from routers.cerdo import cerdo
from routers.galpon import galpon
from routers.alimento import alimento
from routers.compras import compras
from routers.enfermedades import enfermedad
from routers.vacunas import vacunas
from routers.web import web
from routers.venta import venta

from routers.reporte import reporte

# complemento para el envio de correo
from utils.Complemento import Complement
data = Complement.data_email()

app = Flask(__name__)
app.secret_key = 'my_secret_key'

# creo la conexion a la base de datos
# para instalar el modulo de MYSQL el comando es : pip instsall flask-mysqldb
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'elgamer1'
app.config['MYSQL_DB'] = 'tesis_cerdo'
# le paso la conexion al modulo
MySQL(app)

# Configuración del email
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = data['correo']
app.config['MAIL_PASSWORD'] = data['password']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
mail.init_app(app)

# esto llama la vista carpeta routes archivo
app.register_blueprint(index, url_prefix="/")
app.register_blueprint(usuario, url_prefix="/usuario")
app.register_blueprint(cerdo, url_prefix="/cerdo")
app.register_blueprint(galpon, url_prefix="/galpon")
app.register_blueprint(alimento, url_prefix="/alimento")
app.register_blueprint(compras, url_prefix="/compras")
app.register_blueprint(venta, url_prefix="/venta")
app.register_blueprint(enfermedad, url_prefix="/enfermedad")
app.register_blueprint(vacunas, url_prefix="/vacunas")
app.register_blueprint(web, url_prefix="/web")
app.register_blueprint(reporte, url_prefix="/reporte")

#esta funcion ayuda controlar los errores cuanod no hay paginas
def pagna_error(error):
    return render_template('view/home/404.html'), 404
    #return "paguina no enocntrada error 404", 404

