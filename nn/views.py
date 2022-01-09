from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import torch
import numpy


def iris(request):
    from .classes.iris import predict_iris

    values = [5,3,2,1]
    x = predict_iris(*(values))

    return render(request, "base.html", {"pred" : x[0], "prob" : x[1]})