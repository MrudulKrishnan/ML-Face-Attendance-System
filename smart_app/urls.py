from django.urls import path
from . import views

urlpatterns = [

    path("", views.log),
    path("login_action", views.login_action),
    path("logout", views.logout, name="logout"),

    # ////////////////////////////////////////// ADMIN ////////////////////////////////////////////

    path("admin_home", views.admin_home, name="admin_home"),
    path("add_department", views.add_department, name="add_department"),
    path("add_department_post", views.add_department_post, name="add_department_post"),
    path("add_dep_2", views.add_dep_2, name="add_dep_2"),
    path("delete_department/<int:department_id>", views.delete_department, name="delete_department"),
    path("manage_course", views.manage_course, name="manage_course"),
    path("add_course", views.add_course, name="add_course"),
    path("add_course_post", views.add_course_post, name="add_course_post"),
    path("delete_course/<int:course_id>", views.delete_course, name="delete_course"),
    path("manage_staff", views.manage_staff, name="manage_staff"),
    path("add_staff", views.add_staff, name="add_staff"),
    path("add_staff_action", views.add_staff_action, name="add_staff_action"),
    path('edit_staff/<int:staff_id>', views.edit_staff, name="edit_staff"),
    path('edit_staff_action', views.edit_staff_action, name="edit_staff_action"),
    path('delete_staff/<int:staff_id>', views.delete_staff, name="delete_staff"),
    path('set_hod/<int:staff_lid>', views.set_hod, name="set_hod"),
    path("manage_student", views.manage_student, name="manage_student"),
    path("add_student", views.add_student, name="add_student"),
    path("add_student_action", views.add_student_action, name="add_student_action"),
    path('update_student/<int:student_id>', views.update_student, name="update_student"),
    path('update_student_action', views.update_student_action, name="update_student_action"),
    path('delete_student/<int:student_id>', views.delete_student, name="delete_student"),
    path("send_notification", views.send_notification, name="send_notification"),
    path("sendnoti", views.sendnoti, name="sendnoti"),
    path("sendnoti_post", views.sendnoti_post),
    path("delete_notification/<int:notification_id>", views.delete_notification, name="delete_notification"),
    path("view_complaint", views.view_complaint, name="view_complaint"),
    path("reply/<int:reply_id>", views.reply, name="reply"),
    path("reply_action", views.reply_action, name="reply_action"),
    path("manage_class", views.manage_class, name="manage_class"),
    path("add_class", views.add_class, name="add_class"),
    path("add_class_post", views.add_class_post, name="add_class_post"),
    path("delete_class/<int:class_id>", views.delete_class, name="delete_class"),


    path("feedback", views.feedback, name="feedback"),
    path("view_rating", views.view_rating, name="view_rating"),
    path('rating_search', views.rating_search, name="rating_search"),

    # ////////////////////////////////////////// HOD /////////////////////////////////////////////

    path("hod_home", views.hod_home, name="hod_home"),
    path("manage_subject", views.manage_subject, name="manage_subject"),
    path("search_subject", views.search_subject, name="search_subject"),
    path("add_subject", views.add_subject, name="add_subject"),
    path("add_subject_post", views.add_subject_post, name="add_subject_post"),
    path("delete_subject/<int:subject_id>", views.delete_subject, name="delete_subject"),
    path("manage_allocation", views.manage_allocation, name="manage_allocation"),
    path("search_allocation", views.search_allocation, name="search_allocation"),
    path("assign_subject/<int:subject_id>", views.assign_subject, name="assign_subject"),
    path("staff_assign/", views.staff_assign, name="staff_assign"),
    path("view_allocated_subjects/", views.view_allocated_subjects, name="view_allocated_subjects"),
    path("allocated_subjects_search/", views.allocated_subjects_search, name="allocated_subjects_search"),
    path("remove_allocation/<int:alo_id>", views.remove_allocation, name="remove_allocation"),
    path("view_notification", views.view_notification, name="view_notification"),
    path("change_password", views.change_password, name="change_password"),
    path("change_password_action", views.change_password_action, name="change_password_action"),
    path("select_class", views.select_class, name="select_class"),
    path("select_class_attend", views.select_class_attend, name="select_class_attend"),
    path("hod_view_attendace", views.hod_view_attendace, name="hod_view_attendace"),
    path("manage_timetable", views.manage_timetable, name="manage_timetable"),
    path("add_timetable_action", views.add_timetable_action, name="add_timetable_action"),



    path("add_rating", views.add_rating, name="add_rating"),
    path('add_rating_action_clg', views.add_rating_action_clg, name="add_rating_action_clg"),
    path('view_attendance_college_action', views.view_attendance_college_action, name="view_attendance_college_action"),
    path("sendfeedback_college", views.sendfeedback_college),
    path("sendfeedback_college_send", views.sendfeedback_college_send),
    path("sent_rating", views.sent_rating),


    # //////////////////////staff//////////////////

    path("staff_home", views.staff_home, name="staff_home"),
    path("view_profile", views.view_profile, name="view_profile"),
    path("update_staff_action", views.update_staff_action, name="update_staff_action"),
    path("staff_change_password", views.staff_change_password, name="staff_change_password"),
    path("staff_change_password_action", views.staff_change_password_action, name="staff_change_password_action"),
    path("view_alocated_subject", views.view_alocated_subject, name="view_alocated_subject"),
    path("select_class_staff", views.select_class_staff, name="select_class_staff"),
    path("view_timetable", views.view_timetable, name="view_timetable"),
    path("view_timtable_action", views.view_timtable_action, name="view_timtable_action"),
    path('view_attendace_staff', views.view_attendace_staff, name="view_attendace_staff"),
    path("view_notification_staff", views.view_notification_staff, name="view_notification_staff"),



    path("add_rating_staff", views.add_rating_staff, name="add_rating_staff"),
    path('add_rating_action', views.add_rating_action, name="add_rating_action"),
    path("sendfeedback", views.sendfeedback),
    path("sendfeedback_post", views.sendfeedback_post),


    # /////////////////////////////////STUDENT////////////////////////////////


    path('StudentReg', views.StudentReg.as_view(), name="StudentReg"),
    path('login_code', views.LoginPageApi.as_view(), name="login_code"),
    path('ViewTimeTable', views.ViewTimeTable.as_view(), name="ViewTimeTable"),
    path('ViewAttendanceApi/<int:lid>', views.ViewAttendanceApi.as_view(), name="ViewAttendanceApi"),
]

