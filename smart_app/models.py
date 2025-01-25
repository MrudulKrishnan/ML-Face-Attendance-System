from django.db import models

# Create your models here.


class Login(models.Model):
    Username = models.CharField(max_length=80)
    Password = models.CharField(max_length=20)
    Type = models.CharField(max_length=70)

class CourseTable(models.Model):
    Course=models.CharField(max_length=250,null=True,blank=True)
    Description=models.CharField(max_length=500,null=True,blank=True)
    FeesDetails=models.IntegerField(null=True,blank=True)

class Department(models.Model):
    COURSE=models.ForeignKey(CourseTable, on_delete=models.CASCADE,null=True,blank=True)
    department = models.CharField(max_length=40)


class SubjectTable(models.Model):
    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    Subject=models.CharField(max_length=250,null=True,blank=True)



class Staff(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=30)
    age = models.IntegerField()
    DEPARTMENT_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
    
class ClassTable(models.Model):
    ClassName = models.CharField(max_length=30, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    sem = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

class Student(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    CLASS = models.ForeignKey(ClassTable, on_delete=models.CASCADE)
    AdmissionNo=models.IntegerField(null=True,blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField()
    place = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=30)

class Notification(models.Model):
    notification = models.CharField(max_length=200)
    date = models.DateField()

class LeaveTable(models.Model):
    Request=models.CharField(max_length=250,null=True,blank=True)
    Date=models.CharField(max_length=250,null=True,blank=True)
    Time=models.CharField(max_length=250,null=True,blank=True)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)

class AttendanceTable(models.Model):
    SLOT_CHOICES = [
        ('slot_9_10', 'slot_9_10'),
        ('slot_10_11', 'slot_10_11'),
        ('slot_11_12', 'slot_11_12'),
        ('slot_1_2', 'slot_1_2 '),
        ('slot_2_3', 'slot_2_3 '),
        ('slot_3_4', 'slot_3_4'),
    ]
    Date = models.DateField(max_length=20)
    Period=models.CharField(max_length=250,null=True,blank=True, choices=SLOT_CHOICES)
    Attendance = models.CharField(max_length=20)
    STUDENT_ID = models.ForeignKey(Student, on_delete=models.CASCADE)

class Complaint(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    reply = models.CharField(max_length=300)

class Timetable(models.Model):
    Day=models.CharField(max_length=250,null=True,blank=True)
    Period=models.CharField(max_length=250,null=True,blank=True)
    SUBJECT=models.ForeignKey(SubjectTable,on_delete=models.CASCADE,null=True,blank=True)
    TEACHER=models.ForeignKey(Staff,on_delete=models.CASCADE,null=True,blank=True)
    

class Timetable1(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    CLASS = models.ForeignKey(ClassTable, on_delete=models.CASCADE, blank=True, null=True)
    slot_9_10 = models.ForeignKey(SubjectTable, on_delete=models.CASCADE, related_name="slot_9_10")
    slot_10_11 = models.ForeignKey(SubjectTable, on_delete=models.CASCADE, related_name="slot_10_11")
    slot_11_12 = models.ForeignKey(SubjectTable, on_delete=models.CASCADE, related_name="slot_11_12")
    slot_1_2 = models.ForeignKey(SubjectTable, on_delete=models.CASCADE, related_name="slot_1_2")
    slot_2_3 = models.ForeignKey(SubjectTable, on_delete=models.CASCADE, related_name="slot_2_3")
    slot_3_4 = models.ForeignKey(SubjectTable, on_delete=models.CASCADE, related_name="slot_3_4")

    def __str__(self):
        return f"{self.day} Timetable"

class AllocationTable(models.Model):
    SUBJECT = models.ForeignKey(SubjectTable, on_delete=models.CASCADE)
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)

class Feedback(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    date = models.DateField()

class Rating(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.CharField(max_length=100)
    date = models.DateField()

