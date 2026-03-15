from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    roll_no    = models.CharField(max_length=20, unique=True)
    name       = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    gender     = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.CharField(max_length=100)
    batch      = models.CharField(max_length=10)
    photo      = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"

    class Meta:
        ordering = ['roll_no']


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Result(models.Model):
    GRADE_CHOICES = [
        ('O', 'Outstanding'), ('A+', 'Excellent'), ('A', 'Very Good'),
        ('B+', 'Good'), ('B', 'Above Average'), ('C', 'Average'), ('F', 'Fail'),
    ]

    student    = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    subject    = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks      = models.DecimalField(max_digits=5, decimal_places=2)
    grade      = models.CharField(max_length=3, choices=GRADE_CHOICES)
    semester   = models.IntegerField()
    exam_year  = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - Sem {self.semester}"

    class Meta:
        unique_together = ('student', 'subject', 'semester', 'exam_year')
        ordering = ['semester', 'subject']
