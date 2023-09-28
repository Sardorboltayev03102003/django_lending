from django.shortcuts import render

from  . import models


def home(request):
    context = None
    if request.method == "POST":
        models.Customer.objects.create(
            name=request.POST.get('name', None),
            email= request.POST.get('email', None),
            message= request.POST.get('message', None)
        )

    if request.method == 'GET':
        obj = models.Sardor.objects.first()
        context = {
            'name': obj.ism,
            'des': obj.description
        }
    return render(request,"index.html", context=context)

# Create your views here.
