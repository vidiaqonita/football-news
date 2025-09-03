from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406345381',
        'name': 'Vidia Qonita Ahmad',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
