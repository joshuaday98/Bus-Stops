from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    GENDER_CHOICES = (('M', 'MALE'),
                      ('F', 'FEMALE'),
                      ('O', 'OTHER'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateTimeField(auto_now=False)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=999)
    last_name = models.CharField(max_length=999)
    gender = models.CharField(max_length=1000)

    def __str__(self):
        return self.user, self.email

    def __repr__(self):
        pass
