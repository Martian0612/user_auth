from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length = 200,required = True)
    last_length = models.CharField(max_length = 200, required = True)
    email = models.EmailField()

    #
    # date_of_birth = models.DateField()

    # image field
    profile_photo = models.ImageField(null= True, blank= True, upload_to= 'images/')