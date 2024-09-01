from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',            
            'username',
            'full_name',
            'gender',
            'national_code',
            'birthday_date',
            'ceremony_datetime',
            'country'
        ]
        extra_kwargs = {
            'username': {'required': True},
            'full_name': {'required': True},
            'gender': {'required': True},
            'country': {'required': True},
            'national_code': {'required': False},
            'birthday_date': {'required': False},
            'ceremony_datetime': {'required': False},
        }
        
        

    # def validate_birthday_date(self, value):

    #     return value

    # def validate_ceremony_datetime(self, value):

    #     return value
