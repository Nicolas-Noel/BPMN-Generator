from django.shortcuts import render,HttpResponse
from .utils import run_notebook
from django.http import JsonResponse

# Create your views here.
def about(request):
    return render(request, "bpmn_generator/about.html")

def dashboard(request):
    return render(request, "bpmn_generator/dashboard.html")

def documentation(request):
    return render(request, "bpmn_generator/documentation.html")

def generate(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('text')
        result = run_notebook(text)
    return render(request, 'bpmn_generator/generate.html', {'result': result})