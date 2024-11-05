from django.shortcuts import render

def index(request):
    context_dict={'text':'hello world','number':1000}
    return render(request,'basicapp/index.html',context_dict)

def other(request):
    return render(request,'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/relative_url_templates.html')
