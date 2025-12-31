from django.shortcuts import render


def home(request):
    # 'render' looks into the templates folder automatically
    return render(request, 'blog/home.html')