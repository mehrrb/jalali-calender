from django.db import models
import jdatetime

class CustomUser(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    username = models.CharField(max_length=256, unique=True)
    full_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    national_code = models.CharField(max_length=10, unique=True)
    birthday_date = models.DateField()
    ceremony_datetime = models.DateTimeField()
    country = models.CharField(max_length=100, default='Iran')

    def get_first_and_last_name(self):
        first_name, last_name = self.full_name.split()
        return {'first_name': first_name, 'last_name': last_name}

    def get_age(self):
        today = jdatetime.date.today()
        age = today.year - self.birthday_date.year
        if today.month < self.birthday_date.month or (today.month == self.birthday_date.month and today.day < self.birthday_date.day):
            age -= 1
        return age

    def is_birthday(self):
        today = jdatetime.date.today()
        return today.day == self.birthday_date.day and today.month == self.birthday_date.month
