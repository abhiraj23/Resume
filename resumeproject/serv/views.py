from django.shortcuts import render


def services(request):
    context = {'serv': 'active'}
    return render(request, 'serv/services.html', context)
