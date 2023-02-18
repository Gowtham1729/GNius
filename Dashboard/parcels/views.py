from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

# Create your views here.
def homepage(request):
    parcels_list = Post.objects.all().order_by("-date")
    query = request.GET.get("q")
    if query:
        query = query.split()
        for i in query:
            parcels_list = parcels_list.filter(
                Q(company__icontains=i) |
                Q(receiver__icontains=i) |
                Q(hostelname__icontains=i) |
                Q(room__icontains=i)).distinct()
    context={"couriers":parcels_list}
    return render(request, "posts/index.html", context )