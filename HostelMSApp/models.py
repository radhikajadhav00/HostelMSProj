from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICE=[
        ('male','male'),
        ('female','female')
    ]
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE)
    dob = models.DateField()
    address = models.TextField()
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)
    hostel_block = models.CharField(max_length=20)
    
    
def __str__(self):
    return f"{self.full_name} {self.email} {self.address}"

