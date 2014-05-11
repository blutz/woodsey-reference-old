from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def dashboard(request):
    return HttpResponse("Hello")
