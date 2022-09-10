from django.shortcuts import render
from .models import Followrs


def home_page(request):    #### new 1

    # if request.POST:      ## new 3
    #     model=Followrs()     ##### new 5 obeck olyapmz
    #     model.email=request.POST.get("email", "")   ### new 6
    #     model.save()   #### new 7

    if request.POST:      ## new 3
        model=Followrs()     ##### new 5 obeck olyapmz
        email, name=request.POST.get("email", None),request.POST.get("name", None)   ### new 6
        if email:
            model.email = email
        elif name:
            model.name=name
        else:
            model.email= None
        model.save()   #### new 7
        #print(request.POST)       ### new 4
    return render(request, 'index.html')   ### new 2



