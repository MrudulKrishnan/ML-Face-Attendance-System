from datetime import datetime, timedelta
import time
import cv2
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import redirect, render
import json
from django.http import JsonResponse
from smart_app.models import *
from smart_app.serializer import *
from django.shortcuts import render, get_object_or_404
import os
from django.conf import settings
import face_recognition


# Create your views here.

def log(request):
    return render(request, "login_index.html")


def logout(request):
    auth.logout(request)
    return render(request, "login_index.html")


def login_action(request):
    username1 = request.POST['username']
    password1 = request.POST['password']
    ob = Login.objects.get(Username=username1, Password=password1)
    try:
        if ob.Type == 'admin':
            auth_obj = auth.authenticate(username="admin", password="admin")
            if auth_obj is not None:
                auth.login(request, auth_obj)
            return HttpResponse('''<script>alert("welcome ");window.location="/admin_home"</script>''')
        elif ob.Type == 'hod':
            auth_obj = auth.authenticate(username="admin", password="admin")
            if auth_obj is not None:
                auth.login(request, auth_obj)
            request.session['hod_lid'] = ob.id
            return HttpResponse('''<script>alert("welcome ");window.location="/hod_home"</script>''')
        elif ob.Type == 'staff':
            auth_obj = auth.authenticate(username="admin", password="admin")
            if auth_obj is not None:
                auth.login(request, auth_obj)
            request.session['staff_lid'] = ob.id
            return HttpResponse('''<script>alert("welcome ");window.location="/staff_home"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid user");window.location="/"</script>''')
    except:
        return HttpResponse('''<script>alert("invalid user");window.location="/"</script>''')



# ////////////////////////////////////////////// ADMIN////////////////////////////////////////////////


@login_required(login_url='/')
def admin_home(request):
    return render(request, "admin_index.html")

@login_required(login_url='/')
def add_department(request):
    department_obj = Department.objects.all()
    return render(request, "admin/add_department.html", {'department_obj': department_obj})

@login_required(login_url='/')
def add_dep_2(request):
    obj=CourseTable.objects.all()
    return render(request, "admin/add_dep_2.html", {'obj':obj})

@login_required(login_url='/')
def add_department_post(request):
    departments = request.POST['textfield']
    course = request.POST['course']
    ob = Department()
    ob.department = departments
    ob.COURSE = CourseTable.objects.get(id=course)
    ob.save()
    return HttpResponse('''<script>alert("Department Added ");window.location="/add_department#about"</script>''')

@login_required(login_url='/')
def delete_department(request, department_id):
    department_obj = Department.objects.get(id=department_id)
    department_obj.delete()
    return HttpResponse('''<script>alert("Department Deleted ");window.location="/add_department#about"</script>''')

@login_required(login_url='/')
def manage_course(request):
    course_obj = CourseTable.objects.all()
    return render(request, "admin/manage_course.html", {'obj': course_obj})

@login_required(login_url='/')
def add_course(request):
    return render(request, "admin/add_course.html")

@login_required(login_url='/')
def add_course_post(request):
    Course = request.POST['Course']
    Description = request.POST['Description']
    FeesDetails = request.POST['FeesDetails']
    ob = CourseTable()
    ob.Course = Course
    ob.Description = Description
    ob.FeesDetails = FeesDetails
    ob.save()
    return HttpResponse('''<script>alert("Course Added ");window.location="/manage_course#about"</script>''')

@login_required(login_url='/')
def delete_course(request, course_id):
    obj = CourseTable.objects.get(id=course_id)
    obj.delete()
    return HttpResponse('''<script>alert("course Deleted ");window.location="/manage_course#about"</script>''')


@login_required(login_url='/')
def manage_staff(request):
    staff_obj = Staff.objects.all()
    return render(request, "admin/manage_staff.html", {'staff_obj': staff_obj})


@login_required(login_url='/')
def add_staff(request):
    department_obj = Department.objects.all()
    return render(request, "admin/add_staff.html", {'department_obj': department_obj})


@login_required(login_url='/')
def add_staff_action(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    department = request.POST['select']
    age = request.POST['textfield9']
    phone = request.POST['textfield4']
    pin = request.POST['textfield5']
    email = request.POST['textfield6']
    username = request.POST['textfield7']
    password = request.POST['textfield8']

    login_obj = Login()
    login_obj.Username = username
    login_obj.Password = password
    login_obj.Type = 'staff'
    login_obj.save()

    staff_obj = Staff()
    staff_obj.name = name
    staff_obj.place = place
    staff_obj.post = post
    staff_obj.DEPARTMENT_ID = Department.objects.get(id=department)
    staff_obj.age = age
    staff_obj.phone = phone
    staff_obj.pin = pin
    staff_obj.email = email
    staff_obj.LOGIN = login_obj
    staff_obj.save()
    return HttpResponse('''<script>alert("Added ");window.location="/manage_staff#about"</script>''')


@login_required(login_url='/')
def edit_staff(request, staff_id):
    request.session['staff_id'] = staff_id
    department_obj = Department.objects.all()
    staff_obj = Staff.objects.get(id=staff_id)
    return render(request, "admin/edit_staff.html", {'department_obj': department_obj, 'staff_obj': staff_obj})


@login_required(login_url='/')
def edit_staff_action(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    department = request.POST['select']
    age = request.POST['textfield9']
    phone = request.POST['textfield4']
    pin = request.POST['textfield5']
    email = request.POST['textfield6']
    staff_obj = Staff.objects.get(id=request.session['staff_id'])
    staff_obj.name = name
    staff_obj.place = place
    staff_obj.post = post
    staff_obj.department = department
    staff_obj.age = age
    staff_obj.phone = phone
    staff_obj.pin = pin
    staff_obj.email = email
    staff_obj.save()
    return HttpResponse('''<script>alert("Updated");window.location="/manage_staff#about"</script>''')


@login_required(login_url='/')
def delete_staff(request, staff_id):
    staff_obj = Staff.objects.get(id=staff_id)
    staff_obj.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_staff#about"</script>''')

@login_required(login_url='/')
def set_hod(request, staff_lid):
    staff_obj = Login.objects.get(id=staff_lid)
    staff_obj.Type = "hod"
    staff_obj.save()
    return HttpResponse('''<script>alert("set as hod");window.location="/manage_staff#about"</script>''')


@login_required(login_url='/')
def manage_student(request):
    student_obj = Student.objects.all()
    return render(request, "admin/manage_student.html", {'student_obj': student_obj})


@login_required(login_url='/')
def add_student(request):
    ob = ClassTable.objects.all()
    return render(request, "admin/add_student.html", {'val': ob})


@login_required(login_url='/')
def add_student_action(request):
    if request.method == 'POST':
        # Extract data from the request
        admission = request.POST['admission']
        firstname = request.POST['textfield']
        lastname = request.POST['textfield10']
        place = request.POST['place']
        post = request.POST['textfield3']
        pin = request.POST['textfield2']
        phone = request.POST['textfield4']
        email = request.POST['textfield5']
        photo = request.FILES['photo']
        ClassNO = request.POST['select']
        username = request.POST['textfield6']
        password = request.POST['textfield7']

        # Save login record
        login_obj = Login(
            Username=username,
            Password=password,
            Type='student'
        )
        login_obj.save()  # Save to the database

        # Save the photo using FileSystemStorage
        fss = FileSystemStorage()
        photo_file_name = fss.save(photo.name, photo)  # Save photo
        photo_file_path = fss.url(photo_file_name)  # Get URL of the saved file

        # Save student record
        student_obj = Student(
            AdmissionNo=admission,
            first_name=firstname,
            last_name=lastname,
            place=place,
            post=post,
            pin=pin,
            phone=phone,
            email=email,
            photo=photo_file_name,  # Save the file path in the model
            LOGIN=login_obj,  # Link with the saved login object
            CLASS=ClassTable.objects.get(id=ClassNO)  # Get the class object
        )
        student_obj.save()  # Save the student object to the database

        # Create a unique directory for the student's images
        student_dir = os.path.join(settings.MEDIA_ROOT, 'known_images', firstname)
        os.makedirs(student_dir, exist_ok=True)

        # Save the uploaded image to the unique directory
        uploaded_image_path = os.path.join(student_dir, photo.name)
        with open(uploaded_image_path, 'wb+') as destination:
            for chunk in photo.chunks():
                destination.write(chunk)

        # Update the `photo` field to point to the new path
        student_obj.photo.name = os.path.join('known_images', firstname, photo.name)
        student_obj.save()  # Save the updated student object

        # Update the `known_faces.txt` file
        known_faces_path = os.path.join(settings.MEDIA_ROOT, 'known_faces.txt')
        with open(known_faces_path, 'a') as f:
            f.write(f"{student_obj.id}\n")

        return HttpResponse(
            '''<script>alert("Student added successfully");window.location="/manage_student#about"</script>'''
        )
    else:
        return HttpResponse(
            '''<script>alert("Invalid request method");window.location="/manage_student#about"</script>'''
        )
@login_required(login_url='/')
def update_student(request, student_id):
    request.session['student_id'] = student_id
    student_obj = Student.objects.get(id=student_id)
    ob = Department.objects.all()
    return render(request, "admin/update_student.html", {'val': ob, 'student_obj': student_obj})


@login_required(login_url='/')
def update_student_action(request):
    student_obj = Student.objects.get(id=request.session['student_id'])
    admission = request.POST['admission']
    firstname = request.POST['textfield']
    lastname = request.POST['textfield10']
    place = request.POST['place']
    post = request.POST['textfield3']
    pin = request.POST['textfield2']
    phone = request.POST['textfield4']
    email = request.POST['textfield5']
    dept = request.POST['select']

    student_obj.AdmissionNo = admission
    student_obj.first_name = firstname
    student_obj.last_name = lastname
    student_obj.place = place
    student_obj.post = post
    student_obj.pin = pin
    student_obj.phone = phone
    student_obj.department = dept
    student_obj.email = email
    student_obj.DEPARTMENT = Department.objects.get(id=dept)
    student_obj.save()
    
    return HttpResponse('''<script>alert("Updated ");window.location="/manage_student#about"</script>''')


@login_required(login_url='/')
def delete_student(request, student_id):
    student_obj = Student.objects.get(id=student_id)
    student_obj.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location="/manage_student#about"</script>''')


@login_required(login_url='/')
def send_notification(request):
    noti_obj = Notification.objects.all()
    return render(request, "admin/send_notification.html", {'noti_obj': noti_obj})

@login_required(login_url='/')
def sendnoti(request):
    return render(request, "admin/send_notific2.html")


@login_required(login_url='/')
def sendnoti_post(request):
    notification = request.POST['textarea']
    oc = Notification()
    oc.notification = notification
    oc.date = datetime.today()
    oc.save()
    return HttpResponse('''<script>alert("Notification sent ");window.location="/send_notification#about"</script>''')


@login_required(login_url='/')
def delete_notification(request, notification_id):
    notification_obj = Notification.objects.get(id=notification_id)
    notification_obj.delete()
    return HttpResponse('''<script>alert("Notification deleted ");window.location="/send_notification#about"</script>''')

@login_required(login_url='/')
def view_complaint(request):
    comp_obj = Complaint.objects.all()
    return render(request, "admin/view_complaint.html", {'comp_obj': comp_obj})

@login_required(login_url='/')
def reply(request, reply_id):
    request.session['reply_id'] = reply_id
    return render(request,"admin/reply.html")

@login_required(login_url='/')
def reply_action(request):
    reply1 = request.POST['textarea']
    comp_obj = Complaint.objects.get(id=request.session['reply_id'])
    comp_obj.reply = reply1
    comp_obj.save()
    return HttpResponse('''<script>alert("Reply sent ");window.location="/view_complaint#about"</script>''')


@login_required(login_url='/')
def manage_class(request):
    obj = ClassTable.objects.all()
    return render(request, "admin/manage_class.html", {'obj': obj})

@login_required(login_url='/')
def add_class(request):
    obj=Department.objects.all()
    return render(request, "admin/add_class.html", {'obj':obj})

@login_required(login_url='/')
def add_class_post(request):
    dept = request.POST['dept']
    class_name = request.POST['textfield']
    semester = request.POST['textfield1']
    ob = ClassTable()
    ob.ClassName = class_name
    ob.sem = semester
    ob.department = Department.objects.get(id=dept)
    ob.save()
    return HttpResponse('''<script>alert("class Added ");window.location="/manage_class#about"</script>''')

@login_required(login_url='/')
def delete_class(request, class_id):
    obj = ClassTable.objects.get(id=class_id)
    obj.delete()
    return HttpResponse('''<script>alert("Class Deleted ");window.location="/manage_class#about"</script>''')




@login_required(login_url='/')
def feedback(request):
    fb_obj = Feedback.objects.all()
    return render(request, "admin/feedback.html", {'fb_obj': fb_obj})


@login_required(login_url='/')
def view_rating(request):
    rating_obj = Rating.objects.all()

    # Generate the range from 0 to 4 (for 5 stars)
    star_range = list(range(5))
    return render(request, "admin/view_rating.html", {'rating_obj': rating_obj, 'star_range': star_range})


@login_required(login_url='/')
def rating_search(request):
    type = request.POST['select']
    rating_obj = Rating.objects.filter(LOGIN__Type=type)
    return render(request, "admin/view_rating.html", {'rating_obj': rating_obj})


# //////////////////////////////////////// HOD /////////////////////////////////////////////////


@login_required(login_url='/')
def hod_home(request):
    return render(request, "HOD/hod_home.html")

@login_required(login_url='/')
def manage_subject(request):
    subject_obj = SubjectTable.objects.all()
    obj = Department.objects.all()
    return render(request, "HOD/manage_subject.html", { 'dept':obj})

@login_required(login_url='/')
def search_subject(request):
    department_id = request.POST['department_id']
    subject_obj = SubjectTable.objects.filter(DEPARTMENT_id=department_id)
    department = Department.objects.all()
    return render(request, "HOD/manage_subject.html", {'obj': subject_obj, 'dept':department, 'dept_id': department_id})

@login_required(login_url='/')
def add_subject(request):
    dept = Department.objects.all()
    return render(request, "HOD/add_subject.html", {'dept':dept})

@login_required(login_url='/')
def add_subject_post(request):
    dept = request.POST['dept_id']
    subject = request.POST['subject']
    ob = SubjectTable()
    ob.DEPARTMENT = Department.objects.get(id=dept)
    ob.Subject = subject
    ob.save()
    return HttpResponse('''<script>alert("Subject Added ");window.location="/manage_subject#about"</script>''')

@login_required(login_url='/')
def delete_subject(request, subject_id):
    obj = SubjectTable.objects.get(id=subject_id)
    obj.delete()
    return HttpResponse('''<script>alert("subject Deleted ");window.location="/manage_subject#about"</script>''')

@login_required(login_url='/')
def manage_allocation(request):
    obj = Department.objects.all()
    return render(request, "HOD/manage_allocation.html", { 'dept':obj})

@login_required(login_url='/')
def search_allocation(request):
    department = request.POST['department_id']
    subject_obj = SubjectTable.objects.filter(DEPARTMENT_id=department)
    department = Department.objects.all()
    return render(request, "HOD/manage_allocation.html", {'obj': subject_obj, 'dept':department})



@login_required(login_url='/')
def assign_subject(request, subject_id):
    request.session['subject_id']=subject_id
    subject_obj = SubjectTable.objects.get(id=subject_id)
    obj = Staff.objects.filter(DEPARTMENT_ID_id=subject_obj.DEPARTMENT.id)
    return render(request, "HOD/assign_subject.html", { 'obj':obj})

@login_required(login_url='/')
def staff_assign(request):
    staff_obj=Staff.objects.get(id=request.POST['staff_id'])
    obj = AllocationTable()
    obj.SUBJECT = SubjectTable.objects.get(id=request.session['subject_id'])
    obj.STAFF = staff_obj
    obj.save()
    return HttpResponse('''<script>alert("subject Assigned");window.location="/manage_allocation#about"</script>''')


@login_required(login_url='/')
def view_allocated_subjects(request):
    department = Department.objects.all()
    return render(request, "HOD/view_allocated_subjects.html", {'dept':department})

def allocated_subjects_search(request):
    department_id = request.POST['department_id']
    department = Department.objects.all()
    obj = AllocationTable.objects.filter(SUBJECT__DEPARTMENT_id=department_id)
    return render(request, "HOD/view_allocated_subjects.html", {'dept':department, 'obj': obj})

def remove_allocation(request, alo_id):
    obj = AllocationTable.objects.get(id=alo_id)
    obj.delete()
    return HttpResponse('''<script>alert("Removed");window.location="/manage_allocation#about"</script>''')

@login_required(login_url='/')
def view_notification(request):
    notification_obj = Notification.objects.all()
    return render(request, "HOD/view_notification.html", {'notification_obj': notification_obj})

@login_required(login_url='/')
def change_password(request):
    return render(request, "HOD/change_password.html")

def change_password_action(request):
    current_password = request.POST['current_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    obj = Login.objects.get(id=request.session['hod_lid'])
    if obj.Password == current_password:
        if new_password == confirm_password:
            obj.Password = confirm_password
            obj.save()
            return HttpResponse('''<script>alert("password changed successfully");window.location="/hod_home#about"</script>''')
        else:
            return HttpResponse('''<script>alert("wrong current password");window.location="/change_password#about"</script>''')
    else:
        return HttpResponse('''<script>alert("current password faild");window.location="/change_password#about"</script>''')

def select_class(request):
    obj = ClassTable.objects.all()
    return render(request, "HOD/select_class.html", {'obj': obj})



def hod_view_attendace(request):
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        date = request.POST.get('date')
        
        # Get students in the selected class
        students = Student.objects.filter(CLASS_id=class_id)
        
        # Fetch attendance for the selected date and class
        attendance_data = []
        for student in students:
            student_attendance = AttendanceTable.objects.filter(
                STUDENT_ID=student, Date=date
            ).order_by('Period')
            attendance_record = {
                'student': student,
                'attendance': {att.Period: att.Attendance for att in student_attendance},
            }
            attendance_data.append(attendance_record)
        
        return render(request, 'HOD/show_attendance.html', {
            'attendance_data': attendance_data,
            'date': date,
        })
    
    # Fetch all classes for the dropdown
    classes = ClassTable.objects.all()
    return render(request, 'HOD/select_class_attend.html', {'obj': classes})

def manage_timetable(request):
    class_id=request.POST['class_id']
    request.session['class_id']=class_id
    class_obj = ClassTable.objects.get(id=class_id)
    subjects = SubjectTable.objects.filter(DEPARTMENT_id=class_obj.department.id)
    existing_days = Timetable1.objects.filter(CLASS_id=class_obj).values_list('day', flat=True)
    all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    available_days = [day for day in all_days if day not in existing_days]
    return render(request, 'HOD/manage_timetable.html', {
        'subjects': subjects,
        'available_days': available_days
    })
def add_timetable_action(request):
    day = request.POST['day']
    slot_9_10 = request.POST['slot_9_10']
    slot_10_11 = request.POST['slot_10_11']
    slot_11_12 = request.POST['slot_11_12']
    slot_1_2 = request.POST['slot_1_2']
    slot_2_3 = request.POST['slot_2_3']
    slot_3_4 = request.POST['slot_3_4']
    obj = Timetable1()
    obj.CLASS=ClassTable.objects.get(id=request.session['class_id'])
    obj.day=day
    obj.slot_9_10=SubjectTable.objects.get(id=slot_9_10)
    obj.slot_10_11=SubjectTable.objects.get(id=slot_10_11)
    obj.slot_11_12=SubjectTable.objects.get(id=slot_11_12)
    obj.slot_1_2=SubjectTable.objects.get(id=slot_1_2)
    obj.slot_2_3=SubjectTable.objects.get(id=slot_2_3)
    obj.slot_3_4=SubjectTable.objects.get(id=slot_3_4)
    obj.save()
    return HttpResponse('''<script>alert("successfully added");window.location="/select_class#about"</script>''')

@login_required(login_url='/')
def add_rating(request):
    return render(request, "college/add_rating.html")


@login_required(login_url='/')
def add_rating_action_clg(request):
    rating = request.POST['select']
    review = request.POST['review']
    ob = Rating()
    ob.LOGIN = Login.objects.get(id=request.session['college_lid'])
    ob.rating = rating
    ob.review = review
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("THANKYOU FOR YOUR RATING ");window.location="/college_home#about"</script>''')


@login_required(login_url='/')
def sendfeedback_college(request):
    return render(request, "college/send_feedback.html")


@login_required(login_url='/')
def sendfeedback_college_send(request):
    feedback = request.POST['textarea']
    ob = Feedback()
    ob.LOGIN = Login.objects.get(id=request.session['college_lid'])
    ob.feedback = feedback
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("FEEDBACK SENT ");window.location="/college_home#about"</script>''')



@login_required(login_url='/')
def select_class_attend(request):
    obj = ClassTable.objects.all()
    return render(request, "HOD/select_class_attend.html",{'obj': obj})

@login_required(login_url='/')
def view_attendance_college_action(request):
    student_name = request.POST['student']
    department = request.POST['department']
    attendance_obj = AttendanceTable.objects.filter(STUDENT_ID__first_name__startswith=student_name, STUDENT_ID__DEPARTMENT=department)
    return render(request, "college/view_attendance_college.html", {'attendance_obj': attendance_obj})


#//////////////////////////STAFF////////////////////


@login_required(login_url='/')
def staff_home(request):
    return render(request, "staff/staff_home.html")

@login_required(login_url='/')
def view_profile(request):
    dept = Department.objects.all()
    obj = Staff.objects.get(LOGIN_id=request.session['staff_lid'])
    return render(request, "staff/view_profile.html", {'obj': obj, 'dept': dept})


@login_required(login_url='/')
def update_staff_action(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    department = request.POST['select']
    age = request.POST['textfield9']
    phone = request.POST['textfield4']
    pin = request.POST['textfield5']
    email = request.POST['textfield6']

    staff_obj = Staff.objects.get(LOGIN_id=request.session['staff_lid'])
    staff_obj.name = name
    staff_obj.place = place
    staff_obj.post = post
    staff_obj.DEPARTMENT_ID = Department.objects.get(id=department)
    staff_obj.age = age
    staff_obj.phone = phone
    staff_obj.pin = pin
    staff_obj.email = email
    staff_obj.save()
    return HttpResponse('''<script>alert("Added ");window.location="/view_profile#about"</script>''')


@login_required(login_url='/')
def staff_change_password(request):
    return render(request, "staff/change_password.html")

def staff_change_password_action(request):
    current_password = request.POST['current_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    obj = Login.objects.get(id=request.session['staff_lid'])
    if obj.Password == current_password:
        if new_password == confirm_password:
            obj.Password = confirm_password
            obj.save()
            return HttpResponse('''<script>alert("password changed successfully");window.location="/hod_home#about"</script>''')
        else:
            return HttpResponse('''<script>alert("wrong current password");window.location="/change_password#about"</script>''')
    else:
        return HttpResponse('''<script>alert("current password faild");window.location="/change_password#about"</script>''')
   
def view_alocated_subject(request):
    obj = AllocationTable.objects.filter(STAFF__LOGIN_id=request.session['staff_lid'])
    return render(request, 'staff/view_allocated_subject.html',{'obj': obj})

@login_required(login_url='/')
def view_notification_staff(request):
    notification_obj = Notification.objects.all()
    return render(request, "staff/view_notification.html", {'notification_obj': notification_obj})


@login_required(login_url='/')
def add_rating_staff(request):
    return render(request, "staff/add_rating_staff.html")


def view_attendace_staff(request):
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        date = request.POST.get('date')
        
        # Get students in the selected class
        students = Student.objects.filter(CLASS_id=class_id)
        
        # Fetch attendance for the selected date and class
        attendance_data = []
        for student in students:
            student_attendance = AttendanceTable.objects.filter(
                STUDENT_ID=student, Date=date
            ).order_by('Period')
            attendance_record = {
                'student': student,
                'attendance': {att.Period: att.Attendance for att in student_attendance},
            }
            attendance_data.append(attendance_record)
        
        return render(request, 'staff/show_attendance.html', {
            'attendance_data': attendance_data,
            'date': date,
        })
    
    # Fetch all classes for the dropdown
    classes = ClassTable.objects.all()
    return render(request, 'staff/select_class_attend.html', {'obj': classes})

@login_required(login_url='/')
def add_rating_action(request):
    rating = request.POST['select']
    review = request.POST['review']
    ob = Rating()
    ob.LOGIN = Login.objects.get(id=request.session['staff_lid'])
    ob.rating = rating
    ob.review = review
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("THANKYOU FOR YOUR RATING ");window.location="/staff_home#about"</script>''')


@login_required(login_url='/')
def sent_rating(request):
    rating = request.POST['select']
    ob = Rating()
    ob.LOGIN = Login.objects.get(id=request.session['staff_lid'])
    ob.rating = rating
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("THANKYOU FOR YOUR RATING ");window.location="/staff_home#about"</script>''')


@login_required(login_url='/')
def sendfeedback(request):
    return render(request, "staff/send_feedback.html")


@login_required(login_url='/')
def sendfeedback_post(request):
    feedback = request.POST['textarea']
    ob = Feedback()
    ob.LOGIN = Login.objects.get(id=request.session['staff_lid'])
    ob.feedback = feedback
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("FEEDBACK SENT ");window.location="/staff_home#about"</script>''')

def view_timtable_action(request):
    day = request.POST['day']
    obj = Timetable.objects.filter(Day=day)
    return render(request, "staff/view_timetable.html",{'obj': obj})

def select_class_staff(request):
    obj = ClassTable.objects.all()
    return render(request, "staff/select_class.html", {'obj': obj})


def view_timetable(request):
    class_id=request.POST['class_id']
    # Query all timetable entries from the database
    timetable_entries = Timetable1.objects.filter(CLASS_id=class_id).order_by('day')

    # Render the timetable in a template
    return render(request, 'staff/timetable.html', {'timetable_entries': timetable_entries})

def select_slot(request):
    return render(request, 'staff/view_slots.html')

def take_attendance(request):
    slot = request.POST['slot']
    print("---------------->Camera started")
    name_list=[]
                
    # Path to the known images folder and the text file with names
    known_images_path = "E:\\WORK\\PROGRAM FILES\\TRYCODE\Projects\\Smart_Attendance\\Smart_Attendance\\media\\known_images"
    names_file = "E:\\WORK\\PROGRAM FILES\\TRYCODE\\Projects\\Smart_Attendance\\Smart_Attendance\\media\\known_faces.txt"

    # Function to load names from the text file
    def load_names(names_file):
        with open(names_file, "r") as f:
            names = [line.strip() for line in f.readlines()]
        return names

    # Load known face names from the text file
    person_names = load_names(names_file)
    known_face_encodings = []
    known_face_names = []

    # Loop through each person folder inside known_images
    for i, person_folder in enumerate(os.listdir(known_images_path)):
        person_folder_path = os.path.join(known_images_path, person_folder)
        person_name = person_names[i]  # Fetch name corresponding to the person folder
        
        # Loop through each image in the person's folder
        for image_file in os.listdir(person_folder_path):
            image_path = os.path.join(person_folder_path, image_file)
            image = face_recognition.load_image_file(image_path)
            
            # Encode the face and store it with the person's name
            face_encoding = face_recognition.face_encodings(image)
            if face_encoding:
                known_face_encodings.append(face_encoding[0])
                known_face_names.append(person_name)
                print(f"Encoded {image_file} for {person_name}")
            else:
                print(f"No face found in {image_file}, skipping")

    # Final check for any mismatches
    print(f"Number of encodings: {len(known_face_encodings)}, Number of names: {len(known_face_names)}")

    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)
    check_flag=0
    while check_flag==0:
        start_time = time.time()
        while time.time() - start_time < 5:
            ret, frame = cap.read()
            cv2.imshow("Real-time Face Recognition", frame)
            cv2.waitKey(1)
        cv2.imwrite("imageeee.jpg",frame)
        cap.release()
        cv2.destroyAllWindows()

        frame = cv2.imread("imageeee.jpg")

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get face encodings for each face in the frame
        face_encodings = face_recognition.face_encodings(rgb_frame)

        for face_encoding in face_encodings:
            name = "Unknown"

            # Compare the face encodings with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                match_index = matches.index(True)
                if match_index < len(known_face_names):
                    name = int(known_face_names[match_index])
                    print(type(name))
                    name_list.append(name)
                    print(name_list)
                    check_flag=1
                else:
                    print(f"Error: match_index {match_index} out of range")
                    
        if name_list:
             
            current_time = datetime.now() 
            print("----------->", current_time)
            
            for i in name_list:
                obj = AttendanceTable()
                obj.Date=current_time
                obj.Attendance="Present"
                obj.Period = slot
                obj.STUDENT_ID=Student.objects.get(id=i)
                obj.save()
            return HttpResponse('''<script>alert("Done");window.location="/staff_home#about"</script>''')
        else:
            return HttpResponse('''<script>alert("No Faces");window.location="/staff_home#about"</script>''')
    

    #////////////////////////////////WEBSERVICE/////////////////////////////////
    #/////////////////////////////////STUDENT///////////////////////////////////

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from .models import Department  # Ensure your Department model is imported

class LoginPageApi(APIView):
    def post(self, request):
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = Login.objects.filter(Username=username, Password=password).first()
            print("user_obj :-----------", user)
        except Login.DoesNotExist:
            response_dict["message"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
      
        if user.Type == "student":
            response_dict = {
                "login_id": str(user.id),
                "user_type": user.Type,
                "status": "success",
            }   
            print("User details :--------------> ",response_dict)
            return Response(response_dict, HTTP_200_OK)
        else:
            response_dict["message "] = "Your account has not been approved yet or you are a CLIENT user."
            return Response(response_dict, HTTP_200_OK)




class StudentReg(APIView):
    def get(self, request):
        # Query all departments
        departments = Department.objects.all()
        # Serialize the department data
        serializer = DepartmentSerializer(departments, many=True)
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        """
        Handle student registration.
        """
        print("###############", request.data)
        
        # Serialize user and login data
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        
        # Validate the serializers
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            print("&&&&&&&&&&&&&&&&& Data is valid")
            
            # Save login and user data
            password = request.data['Password']
            department = request.data['department']
            obj = Department.objects.get(id=department)
            login_profile = login_serial.save(Type='student', Password=password)
            user_serial.save(LOGIN=login_profile, DEPARTMENT=obj)
            
            # Respond with the serialized user data
            return Response(user_serial.data, status=status.HTTP_201_CREATED)

        # Log detailed errors for debugging
        print("User Serializer Errors:", user_serial.errors)
        print("Login Serializer Errors:", login_serial.errors)

        # Return validation errors
        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)


class ViewTimeTable(APIView):
    def get(self, request,lid):
        obj = Student.objects.get(LOGIN_id=lid)
        obj = Timetable1.objects.filter(CLASS_id=obj.CLASS.id)
        serializer = TimetableSerializer(obj, many = True)
        print("time----------------> ", serializer)
        return Response(serializer.data)


class ViewAttendanceApi(APIView):
    def get(self, request, lid):
        obj = AttendanceTable.objects.filter(STUDENT_ID__LOGIN_id=lid)
        serializer = AttendanceSerializer(obj, many = True)
        print("time----------------> ", serializer)
        return Response(serializer.data)

class ViewProfileApi(APIView):
    def get(self, request, lid):
        obj = Student.objects.filter(LOGIN_id=lid)
        serializer = UserSerializer(obj, many = True)
        print("time----------------> ", serializer)
        return Response(serializer.data)

