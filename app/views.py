from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = dict(title="title", )
    return render(request, "landing_page.html", context)

