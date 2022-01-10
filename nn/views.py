from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import torch
import numpy


#----------------------IRIS---------------------
def iris(request):
    if request.method =="POST":
        from .classes.iris import predict_iris

        try:
            sl = float(request.POST.get("sl"))
            sw = float(request.POST.get("sw"))
            pl = float(request.POST.get("pl"))
            pw = float(request.POST.get("pw"))
        except:
            return render(request, "iris.html", {"pred" : "Enter the", "prob" : "Values First"})

        result = predict_iris(sl,sw,pl,pw)

        return render(request, "iris.html", {"pred" : result[0], "prob" : result[1]})

    else:
        return render(request, "iris.html", {"pred" : "Enter the", "prob" : "Values First"})

#----------------------HEART---------------------
def heart(request):
    return render(request, "heart.html", {"pred" : "Dunno", "prob" : "00.00"})

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

