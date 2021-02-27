from django.shortcuts import render
from django.http import HttpResponse
from .models import School, School_Teacher, Student, Student_School_Teacher, Student_Subject, Subject
from .forms import TestForm
from django.core.paginator import Paginator

def registration(request):
    if request.method == "POST":
        save_record = Student()
        save_record.name = request.POST.get('name')
        save_record.gender = request.POST.get('gender')
        save_record.address = request.POST.get('location')
        if request.POST.get('age') == "":
            save_record.age = request.POST.get(None)
        else:
            save_record.age = request.POST.get('age')

        day = str(request.POST.get('birth_date_year'))
        day = day+"-" + str(request.POST.get('birth_date_month'))+"-" + str(request.POST.get('birth_date_day'))
        save_record.dob = day
        save_record.save()

        t = School_Teacher.objects.filter(school_name_id=request.POST.get('school'), teacher_name_id=request.POST.get('teacher')).first()
        s_s_t_save_record = Student_School_Teacher()
        s_s_t_save_record.student_name = save_record
        s_s_t_save_record.school_teacher_name = t
        s_s_t_save_record.save()

        subject_obj = Subject.objects.filter(id=request.POST.get('subject1')).first()
        student_subject_obj = Student_Subject()
        student_subject_obj.student_name = save_record
        student_subject_obj.subject = subject_obj
        student_subject_obj.save()
        return HttpResponse("<h1>Registration Completed</h1>")


    form = TestForm()
    return render(request, 'registration.html', {'form': form})

def list(request):
    stu_teacher_obj = Student_School_Teacher.objects.all()

    paginator = Paginator(stu_teacher_obj, 10)

    page = request.GET.get('page')
    stu_teacher_obj = paginator.get_page(page)

    return render(request, 'table.html', {'stu_teacher_obj': stu_teacher_obj})



def load_teacher(request):
    teacher_id = request.GET.get('teacher_id')
    all_teacher = []
    t = School_Teacher.objects.filter(school_name_id=teacher_id)
    for teach in t:
        all_teacher.append(teach.teacher_name)
    return render(request, 'teacher_dropdown_list_options.html', {'all_teacher': all_teacher})
