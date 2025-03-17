from django.shortcuts import render

from App1.models import Enrollment

def list_Students_Course(request):
    enrollments = Enrollment.objects.prefetch_related('student', 'course')

    context = {
        'enrollments': enrollments
    }

    return render(request, 'index.html', context)
