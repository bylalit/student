from django.shortcuts import render, redirect
# from models import Student
from .models import Student, Fees, Attendence

# Create your views here.

def index(request):
    return render(request, 'index.html')

def payment(request):
    students = Student.objects.all()
    if request.method == 'POST':
        name_id = request.POST.get('name')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        payment = request.POST.get('payment')
        method = request.POST.get('method')
        
        student = Student.objects.get(id=name_id)
        fees = Fees(student=student, fees=amount, date=date, take_by=payment, payment_method=method)
        fees.save()
        return redirect('payment-show-list')
        
    return render(request, 'payment.html', {'students': students})

def payment_show_list(request):
    fees = Fees.objects.all()
    return render(request, 'payment-show-list.html', {'fees': fees})

def student_show_list(request):
    students = Student.objects.all()
    fees = Fees.objects.all()
    # print(students)
    return render(request, 'showlist.html', {'students': students, 'fees': fees})

def attendent_view(request):
    students = Student.objects.all()
    attendents = Attendence.objects.all()
    
    if request.method == 'POST':
        name_id = request.POST.get('name')
        date = request.POST.get('date')
        status = request.POST.get('status')
        
        student = Student.objects.get(id=name_id)
        attendence = Attendence(student=student, date=date, status=status)
        attendence.save()
        return redirect('attendent-view')
    return render(request, 'attendent-view.html', {'attendents': attendents, 'students': students})

def add_student(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        courses = request.POST.get('courses')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        img = request.FILES.get('img')

        student = Student(fname=fname, mname=mname, lname=lname, gender=gender, email=email, phone=phone, address=address, city=city, courses=courses, amount=amount, date=date, img=img)
        
        student.save()
        
        return redirect('student-show-list')
    
    return render(request, 'add-student.html')

def student_view(request, id):
    student = Student.objects.get(id=id)
    fees = Fees.objects.filter(student=student).order_by('-date')
    attendents = Attendence.objects.filter(student=student).order_by('-date')
    return render(request, 'show-student.html', {'student': student, 'fees': fees, 'attendents': attendents})


def update_student(request, id):
    student = Student.objects.get(id=id)
    
    if request.method == 'POST':
        student.fname = request.POST.get('fname')
        student.mname = request.POST.get('mname')
        student.lname = request.POST.get('lname')
        student.gender = request.POST.get('gender')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.address = request.POST.get('address')
        student.city = request.POST.get('city')
        student.courses = request.POST.get('courses')
        student.amount = request.POST.get('amount')
        if request.POST.get('date'):
            student.date = request.POST.get('date')
        if request.FILES.get('img'):
            student.img = request.FILES.get('img')
        student.save()
        
        return redirect('student-show-list')
    
    return render(request, 'update-student.html', {'student': student})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student-show-list')
