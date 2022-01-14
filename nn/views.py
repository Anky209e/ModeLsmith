from django.shortcuts import render
import os


def home(request):
    models = os.listdir("./nn/classes/")
    length = len(models)
    
    for i in range(length):
        if models[i] == '__pycache__':
            del(models[i])
            break

    for i in range(length -1):
        models[i] = models[i][:-3]

    return render(request,"nn/home.html", {"list":models})
#----------------------IRIS---------------------
def iris(request):
    if request.method =="POST":
        from .classes.iris import predict_iris

        sl = float(request.POST.get("sl"))
        sw = float(request.POST.get("sw"))
        pl = float(request.POST.get("pl"))
        pw = float(request.POST.get("pw"))

        result = predict_iris(sl,sw,pl,pw)
        return render(request, "nn/iris.html", {"list": result, "name":"Iris"})

    else:
        return render(request, "nn/iris.html", {"list": [], "name":"Iris"})


#----------------------HEART---------------------
def heart(request):
    if request.method == "POST":

        from .classes.heart import predict_heart_attack
        
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

        result = predict_heart_attack(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        return render(request,"nn/heart.html",{"list":result, "name":"Heart"})
    else:
        return render(request, "nn/heart.html", {"list":[], "name":"Heart"})


