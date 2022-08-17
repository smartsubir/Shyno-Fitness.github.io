from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Feedback
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"This is sent"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mid = request.POST.get('mid')
        qoe = request.POST.get('qoe')
        moe = request.POST.get('moe')
        tb = request.POST.get('tb')
        qopt = request.POST.get('qopt')
        naqoe = request.POST.get('naqoe')
        gms = request.POST.get('gms')
        ge = request.POST.get('ge')
        hc = request.POST.get('hc')
        remark = request.POST.get('remark')
        
        feedback = Feedback(name=name, phone=phone, mid=mid,remark=remark,date=datetime.today(),QualityofEquipements=qoe,MaintenanceofEquipements=moe,TrainersBehavior=tb,QualityofPersonalTraining=qopt,NutritionistAdvisor=naqoe,GymMusicSystem=gms,GymEnvironment=ge,HealthCalculator=hc)
        feedback.save()
        # messages.success(request, 'Your message has been sent.')
    return render(request, 'index.html')

def feedback(request):
    return render(request, 'feedback.html')


def healthcal(request):
    return render(request, 'healthcal.html')