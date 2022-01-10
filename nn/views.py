from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import torch
import numpy


def iris(request):
    from .classes.iris import predict_iris

    values = [4.8,3.4,1.6,0.2]
    result = predict_iris(*(values))

    return render(request, "base.html", {"pred" : result[0], "prob" : result[1]})

def heart(request):
    from .classes.heart import predict_heart_attack

    values = [50,1,0,144,200,0,0,126,1,0.9,1,0,3]
    result = predict_heart_attack(*values)

    return render(request,"base.html",{"pred":result[0],"prob":result[1]})