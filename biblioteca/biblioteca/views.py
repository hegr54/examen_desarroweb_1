from django.shortcuts import render

def home(request):
    print request
    v = "Mi Biblioteca: consulta de libros"
    v1="Rigoberto"
    v2 = "Usuario: " + v1
    return render(request, "home.html", {'v':v, 'v2':v2})
