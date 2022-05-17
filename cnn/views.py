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
    name = "Maleria"
    html_path = "cnn/maleria.html"

    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"]).replace(" ", "_")
        
        from .classes.maleria import predict_maleria
        result = predict_maleria(img_path)


        return render(request, "cnn/maleria.html", {"image_form": None, "name":name, "list":result})
    else:
        image_form = ImageForm()

        return render(request, "cnn/maleria.html", {"image_form": image_form, "name":name})


def cifar10(request):
    name = "Cifar10"
    html_path = "cnn/cifar10.html"

    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"]).replace(" ", "_")
            
        from .classes.cifar10 import predict_cifar10
        result = predict_cifar10(img_path)

        return render(request, html_path, {"image_form": None, "name":name, "list":result})
    else:
        form = ImageForm()

        return render(request, html_path, {"image_form": form, "name":name})

def gender(request):
    name = "Gender"
    html_path = "cnn/gender.html"

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

        return render(request, html_path, {"image_form": None, "name":name, "list":result})
    else:
        image_form = ImageForm()

        return render(request, html_path, {"image_form": image_form, "name":name})

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