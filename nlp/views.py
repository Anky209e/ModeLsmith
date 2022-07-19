import string
from django.shortcuts import render
import os

def home(request):
    models = os.listdir("./nlp/classes")

    if "__pycache__" in models:
        models.remove("__pycache__")

    for i in range(len(models)):
        models[i] = models[i][:-3]

    return render(request,"nlp/home.html",{"list":models})

def poem_generation(request):
    if request.method =="POST":
        from .classes.poem_generation import generate_poem

        sl = str(request.POST.get("sl"))

        result = generate_poem(sl)
        return render(request, "nlp/poem_generation.html", {"list": result, "name":"Poem Generation"})

    else:
        return render(request, "nlp/poem_generation.html", {"list": [], "name":"Poem Generation"})

def sarcastic_news(request):
    if request.method =="POST":
        from .classes.sarcastic_news import predict_sarcasm

        sl = str(request.POST.get("sl"))

        result = predict_sarcasm(sl)
        return render(request, "nlp/sarcastic_news.html", {"list": result, "name":"Sarcastic News"})

    else:
        return render(request, "nlp/sarcastic_news.html", {"list": [], "name":"Sarcastic News"})