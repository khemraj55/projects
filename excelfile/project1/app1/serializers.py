from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class SignUpSerializers(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=('id','username','password','first_name')
    
    #def create(self, validated_data):
       # return User.objects.create_user(**validated_data)
