from django.http import HttpResponse
from datetime import datetime , timedelta
from django.template import Context, Template

def hola(request):
    return HttpResponse('Buenas clase 41765!')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'la fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    
    return HttpResponse(f'tu fecha de nacimiento aproximada para tus {edad} años seria {fecha}')

def mi_template(request):
    cargar_archivo = open(r"C:\Users\maval\Desktop\python\clase_django\django\templates\templates.html",'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)