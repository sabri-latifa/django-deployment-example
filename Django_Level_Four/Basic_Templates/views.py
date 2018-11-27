from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'Basic_Templates/index.html',context_dict) 

def other(request):
    return render(request,'Basic_Templates/other.html')

def relative(request):
    return render(request,'Basic_Templates/relative_url_templates.html')