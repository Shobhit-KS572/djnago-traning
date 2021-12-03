from django.shortcuts import render, redirect

from .models import *


def signup(request):
    return render(request, 'registration.html')


def teacher(request):
    data = Teacher.objects.all()
    print(data)
    teacher_data = {'data': data}
    print(teacher_data)
    return render(request, 'teacher.html', teacher_data)


def homepage(request):
    name = request.session.get('username')
    data = Student.objects.get(student_name=name)
    sub = Subject.objects.all()
    context = {'item': data,
               'subject': sub
               }
    print(context)
    return render(request, 'homepage.html', context)


def login(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        password = request.POST['password']
        user = Student.objects.filter(student_name=student_name, password=password).exists()
        if user:
            request.session['username'] = student_name
            return redirect('homepage')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def displaydata(request):
    results = Student.objects.all()
    # total_pages = Paginator(results, 2)      #for creating pagenation
    # page_number = total_pages.get_page(2)
    # return HttpResponse(list(page_number))
    # return render(request, ' displaydata.html', {'page_number':page_number})
    context = {'results': results}

    return render(request, 'displaydata.html', context)


def registration(request):
    class_data = Class.objects.all()

    subject_data = Subject.objects.all()
    context = {"class_data": class_data,
               "subject_data": subject_data}
    if request.method == 'POST':
        student_name = request.POST['student_name']
        student_dob = request.POST['student_dob']
        address = request.POST['address']
        email = request.POST['email']
        school = request.POST['school']
        password = request.POST['password']
        class_id = request.POST['class_id']
        subject = request.POST['subject']
        for i in subject:
            print(i)
        stu = Student(student_name=student_name, student_dob=student_dob, address=address, email=email, school=school,
                      password=password)
        stu.class_id = Class.objects.get(id=class_id)

        for sub in subject:
            print(sub)
            stu.subject.add(sub)
        stu.save()
        return render(request, 'login.html')
    else:
        return render(request, 'registration.html', context)
