from django.shortcuts import render

# Create your views here.
def Home(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/home.html')
    else:
        return render(request, 'home/home.html')