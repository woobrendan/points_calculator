from django.shortcuts import render


def index(request):
    standing_list = ('Drivers', 'Manufacturer', 'Team')
    return render(request, 'core/index.html', {
        'standing_list': standing_list
    })
