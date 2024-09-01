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
        birthday_jalali = jdatetime.date.fromgregorian(date=self.birthday_date)
        today_jalali = jdatetime.date.today()
        age = today_jalali.year - birthday_jalali.year
        if (today_jalali.month, today_jalali.day) < (birthday_jalali.month, birthday_jalali.day):
            age -= 1
        return age

    def is_birthday(self):
        today_jalali = jdatetime.date.today()
        birthday_jalali = jdatetime.date.fromgregorian(date=self.birthday_date)
        return today_jalali.month == birthday_jalali.month and today_jalali.day == birthday_jalali.day

    def birthday_jalali(self):
        return jdatetime.date.fromgregorian(date=self.birthday_date)

    def ceremony_datetime_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.ceremony_datetime)
