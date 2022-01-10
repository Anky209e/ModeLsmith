from pickle import NONE
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import torch
import numpy


"""
Note: you can set None to prob variable in dictionary if u want to throw a error at html page and
        set the error message as value to pred.
"""





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
            return render(request, "iris.html", {"pred" : "Enter the values.", "prob" : None})
        result = predict_iris(sl,sw,pl,pw)
        return render(request, "iris.html", {"pred" : result[0], "prob" : result[1]})
    else:
        return render(request, "iris.html", {"pred" : "Enter the values.", "prob" : None})


#----------------------HEART---------------------
def heart(request):
    if request.method == "POST":

        from .classes.heart import predict_heart_attack
        try:
            age = float(request.POST.get("age"))
            sex = float(request.POST.get("sex"))
            cp = float(request.POST.get("cp"))
            trestbps = float(request.POST.get("trestbps"))
            chol = float(request.POST.get("chol"))
            fbs = float(request.POST.get("fbs"))
            restecg = float(request.POST.get("restecg"))
            thalach = float(request.POST.get("thalach"))
            exang = float(request.POST.get("exang"))
            oldpeak = float(request.POST.get("oldpeak"))
            slope = float(request.POST.get("slope"))
            ca = float(request.POST.get("ca"))
            thal = float(request.POST.get("thal"))
        except:
            return render(request,"heart.html",{"pred":"Please enter correct values.","prob":None})
        result = predict_heart_attack(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        return render(request,"heart.html",{"pred":result[0],"prob":result[1]})
    else:
        return render(request, "heart.html", {"pred" : "Enter the values.", "prob" : None})


