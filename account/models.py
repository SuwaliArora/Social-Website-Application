from django.db import models
from django.conf import settings
from django.db.models.fields import related
from django.contrib.auth.models import User
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

class Contact(models.Model):
    #user_from - for user that creates relationship,
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
    #user_to - for the user being followed
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    #to store the time when relationship was created
    created = models.DateTimeField(auto_now_add=True, db_index=True)    #db_index is true to create db index for created field
   
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)

following = models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)
#This	is	a	many-to-many	relationship	from	the	User model	to	itself:	we	refer	to	'self'	in	the	ManyToManyField	field	to	create	a
# relationship	to	the	same	model.

#add following field to user dynamically ,  symmetrical=False to define	a	non-symmetric relation.
User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
    
