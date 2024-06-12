from django.shortcuts import render,HttpResponse

# Create your views here.
def about(request):
    return render(request, "bpmn_generator/about.html")

def dashboard(request):
    return render(request, "bpmn_generator/dashboard.html")

def documentation(request):
    return render(request, "bpmn_generator/documentation.html")

def generate(request):
    return render(request, "bpmn_generator/generate.html")