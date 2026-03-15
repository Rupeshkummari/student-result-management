from django.contrib import admin
from .models import Student, Subject, Result

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ('roll_no', 'name', 'email', 'department', 'batch')
    search_fields = ('roll_no', 'name', 'email')
    list_filter   = ('department', 'batch', 'gender')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display  = ('code', 'name')
    search_fields = ('code', 'name')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display  = ('student', 'subject', 'marks', 'grade', 'semester', 'exam_year')
    list_filter   = ('grade', 'semester', 'exam_year')
    search_fields = ('student__name', 'student__roll_no', 'subject__name')
