from django.shortcuts import render

from Models_test.models import Cars


def cars(request):
    return render(request, 'cars.html', {'data': {
        'cars': Cars.objects.all()
    }})


def car(request, id):
    print(Cars.objects.filter(id=id).get())
    return render(request, 'car.html', {'data': Cars.objects.filter(id=id).get()})
