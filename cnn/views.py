from django.shortcuts import render
from .forms import ImageForm
import os


def home(request):

    models = os.listdir("./cnn/classes")

    if "__pycache__" in models:
        models.remove("__pycache__")

    for i in range(len(models)):
        models[i] = models[i][:-3]

    return render(request,"cnn/home.html", {"list":models})

def maleria(request):
    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"]).replace(" ", "_")
        
        from .classes.maleria import predict
        result = predict(img_path)


        return render(request, "cnn/maleria.html", {"image_form": None, "name":"Maleria", "list":result})
    else:
        image_form = ImageForm()

        return render(request, "cnn/maleria.html", {"image_form": image_form, "name":"Maleria"})


def cifar10(request):
    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"]).replace(" ", "_")
            
        from .classes.cifar10 import predict
        result = predict(img_path)

        return render(request, "cnn/cifar10.html", {"image_form": None, "name":"Cifar10", "list":result})
    else:
        form = ImageForm()

        return render(request, "cnn/cifar10.html", {"image_form": form, "name":"Cifar10"})

def gender(request):

    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"]).replace(" ", "_")
            
        from .classes.gender import predict
        result = predict(img_path)

        return render(request, "cnn/gender.html", {"image_form": None, "name":"Gender", "list":result})
    else:
        image_form = ImageForm()

        return render(request, "cnn/gender.html", {"image_form": image_form, "name":"Gender"})

def eyensign(request):
    name = "EyeNsign"
    html_path = "cnn/eyensign.html"
    
    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"]).replace(" ", "_")
            
        from .classes.eyensign import predict
        result = predict(img_path)
        
        return render(request, html_path, {"image_form": None, "name":name, "list":result})
    else:
        form = ImageForm()
        return render(request, html_path, {"image_form": form, "name":name})