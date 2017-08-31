from django.shortcuts import render
from .models import Lost
from .models import Found
from .forms import LostForm
from .forms import FoundForm
from django.shortcuts import redirect
from django.contrib import messages
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def HomeView(request):
    return render(request,'lostfound/homelost.html')


def LostView(request):
    form = LostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted ")
            return redirect('lostfound:homelost')
        else:
            messages.error(request, "The Details were not Registered, Please Try Again")
    context = {"form":form}
    return render(request, 'lostfound/reportlost.html', context)



def FoundView(request):
    form = FoundForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted ")
            return redirect('lostfound:homelost')
        else:
            messages.error(request, "The Details were not Registered, Please Try Again")
    context = {"form":form}
    return render(request, 'lostfound/reportfound.html', context)

def CompareView(request):
    lst=[]
    for obj1 in Lost.objects.all():
        res = False
        lst.append(obj1.Item_Name +':' + obj1.Last_Seen +':' + obj1.Description)
        for obj2 in Found.objects.all():
            if similar(obj1.Item_Name,obj2.Item_Name)>0.8:
                    if obj2.Found_on > obj1.Last_Seen :#obj2.Found_on__gte=obj1.Last_seen
                        str2="We found a match:"
                        str2+=(obj2.Item_Name + ':' + obj2.Found_on +':'+ obj2.Description)
                        lst.append(str2)
                        res=True
        if res==False:
            lst.append("Sorry, no matches found")
    return render(request,'lostfound/matches.html',{"lst":lst})

