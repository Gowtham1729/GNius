from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import File, Folder, Course
from .forms import FileForm
from django.contrib.auth import authenticate


def files(request, course_id, folder_id):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        course = get_object_or_404(Course, pk=course_id)
        folder = get_object_or_404(Folder, pk=folder_id)
        all_courses = Course.objects.all()
        all_files = File.objects.all()
        all_folders = Folder.objects.all()
        return render(request, 'terashare/file.html',
                      {'all_courses': all_courses, 'all_files': all_files, 'all_folders': all_folders,
                       'course_id': course_id, 'course': course, 'folder': folder, 'folder_id': folder_id})


def home(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        return render(request, 'terashare/home.html')


def download(request, course_id, folder_id, file_id):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        file = get_object_or_404(File, pk=file_id)
        folder = get_object_or_404(Folder, pk=folder_id)
        course = get_object_or_404(Course, pk=course_id)
        req_file = file.filename()
        file_download = file.file
        response = HttpResponse(file_download.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % req_file
        return response


def report(request, course_id, folder_id, file_id):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        return HttpResponse("i")


ebook_file_types = ['pdf', 'doc', 'docx', 'epub', 'pdb', 'html', 'txt', 'mobi']


def upload(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        all_courses = Course.objects.all()
        all_folders = Folder.objects.all()
        all_files = File.objects.all()
        form = FileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            course = book.Course
            course_id = book.Course.id
            folder = book.Type
            folder_id = book.Type.id
            file_type = book.filename().split('.')[-1]
            file_type = file_type.lower()
            if file_type not in ebook_file_types:
                context = {
                    'form': form,
                    'error_message': 'Unsupported File Format',
                    'all_folders': all_folders,
                    'all_courses': all_courses,
                }
                return render(request, 'terashare/upload.html', context)
            book.save()
            context = {'all_courses': all_courses, 'all_folders': all_folders, 'all_files': all_files, 'course': course,
                       'folder': folder, 'course_id': course_id, 'folder_id': folder_id}
            return render(request, 'terashare/file.html', context)
        context = {'form': form, 'all_folders': all_folders, 'all_courses': all_courses}
        return render(request, 'terashare/upload.html', context)


def search(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        all_courses = Course.objects.all()
        query = request.GET.get("q")
        if query:
            query = query.split()
            for i in query:
                all_courses = all_courses.filter(
                    Q(course_code__icontains=i) |
                    Q(course_title__icontains=i)).distinct()
            context = {'all_courses': all_courses}
            return render(request, 'terashare/search_results.html', context)
        return render(request, 'terashare/search.html')


def searchres(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        return render(request, 'terashare/home.html')
