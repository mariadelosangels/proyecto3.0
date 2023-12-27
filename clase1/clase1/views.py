from django.http import HttpResponse
from datetime import datetime
from django.template import Template , Context 
from django.shortcuts import render
def saludo(request):
    return HttpResponse("Hola Mora!!!!!!")
def despedida(request):
    return HttpResponse ("Chau Mora!!!!") 
def dia_hoy(request):
    dia = datetime.now()
    textoHtml =f"Hoy es: {dia}"
    return HttpResponse(textoHtml)
def vista_parametro(request,nombre):
    textoHtml = f"Hola, {nombre} "
    return HttpResponse(textoHtml)
def vista_template(request):
    # Ruta del archivo HTML
    ruta_html = r"C:\Users\Admin\Desktop\django-proyecto1\clase1\clase1\template.html"

    #Abre el archivo y lee su contenido
    #with open(ruta_html, 'r') as archivo_html:
    
     #   contenido_html = archivo_html.read()

    # Crea la plantilla con el contenido leído
   # plantilla = Template(contenido_html)

    # Define el contexto con datos (puedes modificar esto según tus necesidades)
  #  mi_contexto = {'nombre': 'Usuario Ejemplo'}

    # Renderiza la plantilla con el contexto
   # documento = plantilla.render(mi_contexto)

    return render(request,'template.html')