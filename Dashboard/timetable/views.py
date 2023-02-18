from django.shortcuts import render, get_object_or_404
from .forms import CourseRegistrationForm
from profiles.models import UserProfile
from terashare.models import Course
from .models import CoursesReg, Event
from datetime import datetime

def timetable(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        user_p = get_object_or_404(UserProfile, user=request.user)
        if not user_p.course_reg:
            form = CourseRegistrationForm(request.POST or None)
            if form.is_valid():
                reg_courses = form.save(commit=False)
                reg_courses.user_profile = user_p
                user_p.course_reg = True
                reg_courses.save()
                user_p.save()
                return render(request, 'timetable/timetable.html')
        else:
            now = datetime.now().isoweekday()
            courses = CoursesReg.objects.get(user_profile=UserProfile.objects.get(user=request.user))
            none = Course.objects.get(pk=6)
            reg_courses = [courses.course1, courses.course2, courses.course3, courses.course4, courses.course5,
                           courses.course6, courses.course7, courses.course8, courses.course9, courses.course10]
            return render(request, 'timetable/timetable.html',
                          {'courses': reg_courses, 'none': none, 'now': now})
    context = {'form': form}
    return render(request, 'timetable/course_reg.html', context)


def events(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        now = datetime.now().date()
        events = Event.objects.all()
        return render(request, 'timetable/events.html', {'events': events, 'now': now})
