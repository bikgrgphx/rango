from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!Go to about Page<a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says you are at about page. Go to indexx page <a href='/rango/'>Index<a>")