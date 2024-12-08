from django.contrib import admin

# local imports
from .models import (
    Student,
    Subject,
    ExamType,
    Exam,
    Grade,
    Result,
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'class_level', 'date_of_birth')
    search_fields = ('name', 'roll_number')
    ordering = ('id', )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'class_level', 'code')
    search_fields = ('subject_name', 'code')
    ordering = ('id', )


@admin.register(ExamType)
class ExamTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    ordering = ('id', )


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date', 'class_level')
    search_fields = ('name', 'type', 'date')
    ordering = ('id', )


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    ordering = ('id', )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'subject',
        'marks',
        'grade',
        'exam',
    )
    search_fields = ('student',)
    ordering = ('id', )
