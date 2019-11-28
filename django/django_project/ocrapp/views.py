from django.shortcuts import render,HttpResponse
from django.template.loader import get_template

# Create your views here.
def ocrapp(request):
    return render(request, 'index.html', {
        'data': "Hello Django ",
    })

def ocr_button(request):
    return render(request,'index.html')