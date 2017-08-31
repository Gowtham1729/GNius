from django.shortcuts import render


# Create your views here.

def menu_jaiswal(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        return render(request, 'mess/menu_jaiswal.html')

