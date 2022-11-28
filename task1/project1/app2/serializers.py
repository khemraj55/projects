from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'


class SignUpSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    id=serializers.IntegerField(read_only=True)
    
    #email = serializers.EmailField()

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Duplicate")
        return lower_email
    
    class Meta:
        model=User
        fields=('id','username','password','email',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)