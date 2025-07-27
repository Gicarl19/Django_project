from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# List View
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
    
# Index View
def index(request):
    return render(request,'students/index.html')

# Lyrics View
def lyrics(request):
    return render(request,'students/lyrics.html')

# Lyrics 1 View
def lyrics1(request):
    return render(request, 'students/lyrics1.html')

#Enrollment View
def enrollment(request):
    return render(request, 'students/enrollment.html')
    
# Song Lyrics View
def song_lyrics(request):
    return render(request, 'students/song_lyrics.html')

# Create View
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Enrolled successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# Update View
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student saved successfully!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# Delete View
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})