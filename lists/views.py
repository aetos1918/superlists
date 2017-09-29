from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    test_str = '<html><head><title>To-Do lists</title></head></html>'
    return HttpResponse(test_str)
