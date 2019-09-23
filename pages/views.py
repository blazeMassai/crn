from django.shortcuts import render
from django.http import HttpResponse
from monitor.models import Crn
from station.models import Station

# Create your views here.
def index(request):

    return render(request, 'pages/index.html')

def latest(request):
    #hapa chini tunataka listings 3 ambazo ni latest na published
    crns = Crn.objects.order_by('-created_at')

    context = {
        'crns': crns ,
    }
    return render(request, 'pages/latest.html' ,context)
