from django.shortcuts import render


def index(request):
    standing_list = ('Drivers', 'Manufacturer', 'Team')
    styling = 'py-2 px-2 rounded-xl bg-red-200 text-lg hover:bg-red-500'

    return render(request, 'core/index.html', {
        'standing_list': standing_list,
        'styling': styling
    })
