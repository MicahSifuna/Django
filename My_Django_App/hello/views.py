from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'hello/index.html',{'name': 'Micah'})



def index(request):
    today = datetime.datetime.now().date()
    return render(request,"index.html",{"today": today})

