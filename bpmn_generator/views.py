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

def download_result(request):
    text = request.GET.get('text', '')
    print(f"Text received in GET: {text}")
    result = run_notebook(text)
    print(f"Result from notebook in GET: {result}")
    
    result_text = "\n".join(result)
    response = HttpResponse(result_text, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="result.txt"'
    return response