from django.contrib import admin

from App1.models import Student, Course, Enrollment

class AdminStudent(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


class AdminCourse(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date']


class AdminEnrollment(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrollment_date', 'grade']


admin.site.register(Student, AdminStudent)
admin.site.register(Course, AdminCourse)
admin.site.register(Enrollment, AdminEnrollment)

