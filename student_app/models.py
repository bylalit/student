from django.db import models

# Create your models here.

class Student(models.Model):
    gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=gender, default='Male')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default='0')
    date = models.DateField()
    img = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.fname


class Fees(models.Model):
    pay_method = (
        ('Cash', 'Cash'),
        ('Online', 'Online')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fees = models.IntegerField()
    date = models.DateField()
    # paid = models.BooleanField(default=False)
    take_by = models.CharField(max_length=30, default='Admin')
    payment_method = models.CharField(max_length=10, choices=pay_method, default='Cash')
    
    def __str__(self):
        return self.student.fname


class Attendence(models.Model):
    stastus = (
        ('Present', 'Present'),
        ('Absent', 'Absent')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=stastus)
    
    def __str__(self):
        return self.student.fname