from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Gate(req):
    res = HttpResponse()
    res.write("ok")
    print(req)
    return res