from django.shortcuts import render,HttpResponse

# Create your views here.
def ocrapp(request):
    return render(request, 'index.html', {
        'data': "Hello Django ",
    })