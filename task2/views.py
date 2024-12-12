from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return render(request,'func_t.html')

class class_t(TemplateView):
    template_name = 'func_t.html'
