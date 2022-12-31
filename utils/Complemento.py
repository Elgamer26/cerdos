
class Complement:
    def current_date_format(date):
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = date.day
        month = months[date.month - 1]
        year = date.year
        messsage = "{} de {} del {}".format(day, month, year)
        return messsage
    
    # para el correo
    def data_email():
        data = {
            'correo': 'haciendamada@amada.i-sistener.xyz',
            'password': 'HaciendAmada1.'
        }
        return data
    