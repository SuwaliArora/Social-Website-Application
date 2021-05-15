from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    #The user one-to-one field allows you	to associate profiles with users.
    #use CASCADE for the on_delete	parameter so that its related profile also	gets deleted when a	user is	deleted.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    #install the Pilloe library to handle images.  (pip install Pillow==5.1.0)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
