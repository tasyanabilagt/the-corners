from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406351005',
        'name': 'Tasya Naila Anggita Saragih',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)