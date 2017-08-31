from django.shortcuts import render
from .models import ToChandhkedaWD, ToChandhkedaHD, ToPalajHD,ToPalajWD
from time import strftime, localtime

import datetime

def BusView(request):
    strng2 = strftime("%H:%M:%S", localtime())
    day = datetime.datetime.today().weekday()
    try:
        if day == 5 or day == 6:
            instance1 = ToPalajHD.objects.filter(time__gte=strng2)[0]
        else:
            instance1 = ToPalajWD.objects.filter(time__gte=strng2)[0]
    except IndexError:
        if day == 5 or day == 6:
            instance1 = ToPalajHD.objects.all()[0]
        else:
            instance1 = ToPalajWD.objects.all()[0]
    try:
        if day == 5 or day == 6:
            instance2 = ToChandhkedaHD.objects.filter(time__gte=strng2)[0]
        else:
            instance2 = ToChandhkedaWD.objects.filter(time__gte=strng2)[0]
    except IndexError:
        if day == 5 or day == 6:
            instance2 = ToChandhkedaHD.objects.all()[0]
        else:
            instance2 = ToChandhkedaWD.objects.all()[0]
    arry1 = [str(instance1.time),str(instance1.routepic.url),str(instance2.time),str(instance2.routepic.url)]
    return render(request,'shuttleservice/buses.html', {'array1': arry1})


