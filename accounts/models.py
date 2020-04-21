from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    id_num = models.IntegerField(default=99101015030080)
    house_num = models.IntegerField(default=0000)
    street_name = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=30)
