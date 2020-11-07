from django.shortcuts import render
from .models import Quiz, Contact, Exam_hs, Item




# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    exams = Exam_hs.objects.all()
    print(Exam_hs)
    params ={'exams':exams}
    return render(request, 'about.html',params)



def services(request):
    quizs = Quiz.objects.all()
    print(Quiz)
    params ={'quizs':quizs}
    return render(request, 'services.html',params)



def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')


def pmc(request):
    items = Item.objects.all()
    params ={'items':items}
    return render(request, 'pmc.html',params)








def diffa(request):
    return render(request, 'diffa.html')



