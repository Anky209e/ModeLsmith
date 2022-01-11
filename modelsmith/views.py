from django.shortcuts import redirect, render



def base(request):
    return render(request,"home/home.html")
def home(request):
    return redirect("/")