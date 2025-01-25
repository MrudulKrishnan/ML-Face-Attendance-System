from rest_framework.serializers import ModelSerializer, ImageField 
from rest_framework import serializers

from smart_app.models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['AdmissionNo', 'first_name', 'last_name', 'photo', 'place', 'post', 'pin', 'phone', 'email']

class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        fields = ['Username', 'Password']


from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department']  # Include relevant fields like `id` and `name`


class TimetableSerializer(serializers.ModelSerializer):
    subject1 = serializers.CharField(source='slot_9_10.Subject')
    subject2 = serializers.CharField(source='slot_10_11.Subject')
    subject3 = serializers.CharField(source='slot_11_12.Subject')
    subject4 = serializers.CharField(source='slot_1_2.Subject')
    subject5 = serializers.CharField(source='slot_2_3.Subject')
    subject6 = serializers.CharField(source='slot_3_4.Subject')
    class Meta:
        model = Timetable1
        fields = ['day', 'subject1','subject2', 'subject3', 'subject4', 'subject5', 'subject6']  # Include relevant fields like `id` and `name`

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceTable
        fields = ['Date', 'Attendance', 'Period']  # Include relevant fields like `id` and `name`

