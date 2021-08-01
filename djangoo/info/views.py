from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.
def infolist(request):
    infoo = models.infoclass.objects.all().order_by('firstname')
    arg ={'infoo' :infoo}
    return render(request , 'info.html' ,arg)

def infodetail(request, firstname):
    return HttpRespnse(firstname)
    
