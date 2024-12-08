from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    class_level = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    class_level = models.IntegerField()
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.subject_name


class ExamType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(
        ExamType, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField()
    class_level = models.IntegerField()

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True
    )
    marks = models.IntegerField()
    grade = models.ForeignKey(
        Grade, on_delete=models.SET_NULL, null=True, blank=True
    )
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"
