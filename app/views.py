from django.shortcuts import render


def index(request):
    context = dict(title="title", )
    return render(request, "landing_page.html", context)

