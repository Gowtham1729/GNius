from django.shortcuts import render, get_object_or_404
from .forms import ComplaintForm
from .models import Category, Complaint

# Create your views here.
def Home(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        return render(request, 'welfare/home.html')


def complaint(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        form = ComplaintForm(request.POST or None)
        if form.is_valid():
            complaint  = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            complaints = Complaint.objects.filter(user=request.user)
            return render(request, 'welfare/complaints.html', {'complaints':complaints})
        else:
            return render(request, 'welfare/complaint.html', {'form':form})


def complaints(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        complaints = Complaint.objects.filter(user=request.user)
        return render(request, 'welfare/complaints.html', {'complaints':complaints})

