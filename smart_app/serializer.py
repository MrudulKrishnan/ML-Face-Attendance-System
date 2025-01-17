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
    subject = serializers.CharField(source='SUBJECT.Subject')
    class Meta:
        model = Timetable
        fields = ['Day', 'Period', 'subject']  # Include relevant fields like `id` and `name`

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['Date', 'Attendance']  # Include relevant fields like `id` and `name`

