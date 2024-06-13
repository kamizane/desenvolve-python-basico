from datetime import date
from datetime import datetime

data = date.today()
data_formatada= data.strftime("%d/%m/%Y")
hora = datetime.now()
hora_formatada = hora.strftime("%H:%M")
print("Data: %s \nHora: %s" % (data_formatada,hora_formatada))