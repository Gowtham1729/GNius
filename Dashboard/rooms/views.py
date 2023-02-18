
from django.shortcuts import render
from .models import AccomodationForm
from .forms import RequestForm
from django.shortcuts import redirect
from django.contrib import messages

def HomeView(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        return render(request,'rooms/home.html')

def ShowView(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        object_list = AccomodationForm.objects.all()
        context={"object_list":object_list}
        return render(request, 'rooms/viewrequest.html', context)

def DetailView(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        return render(request,'rooms/detail.html')

def RequestView(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        form = RequestForm(request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Your Room Booking is Done!! ")
                return redirect('rooms:home')
            else:
                messages.error(request, "The Request was not Registered, Please Try Again")
        context = {"form":form}
        return render(request, 'rooms/requestroom.html', context)

