from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

#to store user activities
class Action(models.Model):
    #user- that performed the action
    user = models.ForeignKey('auth.User', related_name='actions', db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # the verb describe the action that user performed
    # a foreign key field that points to content type model
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE)
    # a positiveIntegerField for storing prmary key of related object
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    #genericForeignkey based on combination of 2 prev fileds
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True, db_index=True)  #date time e=when action was created

    class Meta:
        ordering = ('-created',)
