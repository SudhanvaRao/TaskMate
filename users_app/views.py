from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import CostomRegform
from django.contrib import messages

# Create your views here.
def register(request):
    
    if request.method=="POST":
        register_form = CostomRegform(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created,Login to get Started!"))
            return redirect('register')
    else:
        register_form = CostomRegform()
    return render(request, 'register.html',{'register_form':register_form})