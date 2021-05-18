from django.db import models
from django.conf import settings
from django.db.models.fields import related
from django.utils.text import slugify

# Create your models here.

#models used to store images bookmarked from different sites
class Image(models.Model):
    #one-to-many relationship as 1 user can share may images
    #user that bookmarked the image
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)       # a title for the image
    slug = models.SlugField(max_length=200, blank=True)      # short labels for seo friendly urls
    url = models.URLField()           #The original URL for this image.
    image = models.ImageField(upload_to='images/%Y/%m/%d/')  #inage file
    description = models.TextField(blank=True)    #optional description for the image
    created = models.DateField(auto_now_add=True, db_index=True)     #the date time indicated when object was created in database
                                                      #db_index=true so that django creates index in database
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) #slugify() function	provided by Django	to	automatically	generate
                                          #	the	image	slug	for	the	given	title when	no	slug	is	provided
        super(Image, self).save(*args, **kwargs)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='iamges_liked', blank=True)
    #manytomany relation coz many images can be liked by many users
