from django.shortcuts import render
from .forms import ImageForm

def maleria(request):
    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"])
            
        from .classes.maleria import predict_maleria
        result = predict_maleria(img_path)


        return render(request, "maleria.html", {"image_form": "", "pred" : result[0], "prob" : result[1]})
    else:
        image_form = ImageForm()

        return render(request, "maleria.html", {"image_form": image_form, "pred" : "Please Upload Image", "prob" : None})


def cifar10(request):
    if request.method =="POST":        
        form = ImageForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
        except:
            pass

        img_path ="./media/cnn_images/" + str(request.FILES["image_field"])
            
        from .classes.cifar10 import predict_cifar10
        result = predict_cifar10(img_path)

        return render(request, "cifar10.html", {"image_form": "", "pred" : result[0], "prob" : result[1]})
    else:
        image_form = ImageForm()

        return render(request, "cifar10.html", {"image_form": image_form, "pred" : "Please Upload Image", "prob" : None})