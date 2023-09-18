from django.shortcuts import render


def index(request):
    styling = 'py-2 px-2 rounded-xl bg-red-200 text-lg hover:bg-red-500 flex justify-center'

    return render(request, 'core/index.html', {
        'styling': styling
    })
