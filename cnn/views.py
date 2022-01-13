from django.shortcuts import render
from .forms import ImageForm
import os


def home(request):

    models = os.listdir("./cnn/classes")
    length = len(models)

    for i in range(length):
        if models[i] == '__pycache__':
            del(models[i])
            break

    for i in range(length -1):
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
        
        from .classes.maleria import predict_maleria
        result = predict_maleria(img_path)


        return render(request, "cnn/maleria.html", {"image_form": "", "pred" : result[0], "prob" : result[1], "name":"Maleria"})
    else:
        image_form = ImageForm()

        return render(request, "cnn/maleria.html", {"image_form": image_form, "pred" : "Please Upload Image", "prob" : None, "name":"Maleria"})


def cifar10(request):
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

        return render(request, "cnn/cifar10.html", {"image_form": "", "pred" : result[0], "prob" : result[1], "name":"Cifar10"})
    else:
        image_form = ImageForm()

        return render(request, "cnn/cifar10.html", {"image_form": image_form, "pred" : "Please Upload Image", "prob" : None, "name":"Cifar10"})

def gender(request):
    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"]).replace(" ", "_")
            
        from .classes.gender import predict_gender
        result = predict_gender(img_path)

        return render(request, "cnn/gender.html", {"image_form": "", "pred" : result[0], "prob" : result[1], "name":"Gender"})
    else:
        image_form = ImageForm()

        return render(request, "cnn/gender.html", {"image_form": image_form, "pred" : "Please Upload Image", "prob" : None , "name":"Gender"})