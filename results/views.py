from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, Subject, Result


# ── Authentication ────────────────────────────────────────────────────

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'results/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ── Dashboard ─────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    total_students = Student.objects.count()
    total_subjects = Subject.objects.count()
    total_results  = Result.objects.count()
    recent_students = Student.objects.order_by('-created_at')[:5]
    context = {
        'total_students': total_students,
        'total_subjects': total_subjects,
        'total_results':  total_results,
        'recent_students': recent_students,
    }
    return render(request, 'results/dashboard.html', context)


# ── Student CRUD ──────────────────────────────────────────────────────

@login_required
def student_list(request):
    query    = request.GET.get('q', '')
    students = Student.objects.filter(name__icontains=query) if query else Student.objects.all()
    return render(request, 'results/student_list.html', {'students': students, 'query': query})


@login_required
def student_add(request):
    if request.method == 'POST':
        Student.objects.create(
            roll_no    = request.POST.get('roll_no'),
            name       = request.POST.get('name'),
            email      = request.POST.get('email'),
            gender     = request.POST.get('gender'),
            department = request.POST.get('department'),
            batch      = request.POST.get('batch'),
            photo      = request.FILES.get('photo'),
        )
        messages.success(request, 'Student added successfully.')
        return redirect('student_list')
    return render(request, 'results/student_form.html', {'action': 'Add'})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.roll_no    = request.POST.get('roll_no')
        student.name       = request.POST.get('name')
        student.email      = request.POST.get('email')
        student.gender     = request.POST.get('gender')
        student.department = request.POST.get('department')
        student.batch      = request.POST.get('batch')
        if request.FILES.get('photo'):
            student.photo = request.FILES.get('photo')
        student.save()
        messages.success(request, 'Student updated successfully.')
        return redirect('student_list')
    return render(request, 'results/student_form.html', {'action': 'Edit', 'student': student})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('student_list')


# ── Result CRUD ───────────────────────────────────────────────────────

@login_required
def result_list(request):
    results = Result.objects.select_related('student', 'subject').all()
    return render(request, 'results/result_list.html', {'results': results})


@login_required
def result_add(request):
    if request.method == 'POST':
        Result.objects.create(
            student   = get_object_or_404(Student, pk=request.POST.get('student')),
            subject   = get_object_or_404(Subject, pk=request.POST.get('subject')),
            marks     = request.POST.get('marks'),
            grade     = request.POST.get('grade'),
            semester  = request.POST.get('semester'),
            exam_year = request.POST.get('exam_year'),
        )
        messages.success(request, 'Result added successfully.')
        return redirect('result_list')
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'results/result_form.html', {
        'action': 'Add', 'students': students, 'subjects': subjects
    })


@login_required
def result_delete(request, pk):
    result = get_object_or_404(Result, pk=pk)
    result.delete()
    messages.success(request, 'Result deleted successfully.')
    return redirect('result_list')


# ── Public Result View ────────────────────────────────────────────────

def view_result(request):
    student = result = error = None
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        try:
            student = Student.objects.get(roll_no=roll_no)
            result  = Result.objects.filter(student=student).select_related('subject')
        except Student.DoesNotExist:
            error = 'No student found with this roll number.'
    return render(request, 'results/view_result.html', {
        'student': student, 'result': result, 'error': error
    })
