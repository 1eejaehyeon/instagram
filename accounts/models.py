from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.core.validators import RegexValidator
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "male", "MALE"
        FEMAILE = "Fmale", "Female"
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length= 5,choices=GenderChoices.choices)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'