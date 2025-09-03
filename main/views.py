from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406411906',
        'name': 'Oscar Glad Winfi Simanullang',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
