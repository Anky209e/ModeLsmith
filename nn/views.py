from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import torch
import numpy


#----------------------IRIS---------------------
def iris(request):
    return render(request, "iris.html")

def iris_ans(request):
    from .classes.iris import predict_iris

    sl = float(request.GET.get("sl"))
    sw = float(request.GET.get("sw"))
    pl = float(request.GET.get("pl"))
    pw = float(request.GET.get("pw"))

    result = predict_iris(sl,sw,pl,pw)

    return render(request, "result.html", {"pred" : result[0], "prob" : result[1]})


#----------------------HEART---------------------
def heart(request):
    return render(request, "heart.html")

def heart_ans(request):
    from .classes.heart import predict_heart_attack

    age =float(request.GET.get("age"))
    sex = float(request.GET.get("sex"))
    cp = float(request.GET.get("cp"))
    trestbps = float(request.GET.get("trestbps"))
    chol = float(request.GET.get("chol"))
    fbs = float(request.GET.get("fbs"))
    restecg = float(request.GET.get("restecg"))
    thalach = float(request.GET.get("thalach"))
    exang = float(request.GET.get("exang"))
    oldpeak = float(request.GET.get("oldpeak"))
    slope = float(request.GET.get("slope"))
    ca = float(request.GET.get("ca"))
    thal = float(request.GET.get("thal"))

    result = predict_heart_attack(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

    return render(request,"result.html",{"pred":result[0],"prob":result[1]})

