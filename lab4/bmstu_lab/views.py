from django.shortcuts import render

carsList = [
    {'name': 'Audi R8', 'speed': 300, 'cost': 5, 'picture': 'audi.jpg', 'colour': 'белый' },
    {'name': 'Bugatti Veyron', 'speed': 310, 'cost': 7, 'picture': 'bugatti.jpg', 'colour': 'черный'},
    {'name': 'Dodge Viper', 'speed': 290, 'cost': 9, 'picture': 'dodge.jpg', 'colour': 'красный'}
]


def cars(request):
    return render(request, 'cars.html', {'data': {
        'cars': [
            {'name': 'Audi R8', 'id': 1},
            {'name': 'Bugatti Veyron', 'id': 2},
            {'name': 'Dodge Viper', 'id': 3},
        ]
    }})


def car(request, id):
    return render(request, 'car.html', {'data': carsList[id - 1]})
