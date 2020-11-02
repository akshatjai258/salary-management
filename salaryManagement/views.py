from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    # print("called home view")
    return render(request, 'main/homepage.html')