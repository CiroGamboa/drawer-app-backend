from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world! I'm gonna get that job!")

@csrf_exempt
def save_draw(request):
    print(request)
    return HttpResponse("Awesome")


