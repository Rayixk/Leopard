from django.shortcuts import render,HttpResponse
from django.utils.safestring import mark_safe

def index(request):
    return HttpResponse(mark_safe("<h1>index</h1>"))
