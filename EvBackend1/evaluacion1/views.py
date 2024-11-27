from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'evaluacion1/index.html')

def pagina2(request):
    return render(request, 'evaluacion1/pagina2.html')

def pagina3(request):
    return render(request, 'evaluacion1/pagina3.html')

def pagina4(request):
    return render(request, 'evaluacion1/pagina4.html')

def pagina5(request):
    return render(request, 'evaluacion1/pagina5.html')