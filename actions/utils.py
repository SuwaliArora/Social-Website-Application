# to define a shortcut function that will allow us to create new Action Objects
import datetime
from django.contrib.contenttypes.fields import create_generic_related_manager
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action

#function to add new actions to the activity stream
def create_action(user, verb, target=None):
    #check for any similar action made in last minute
    now = timezone.now()   #for current time
    last_minute = now - datetime.timedelta(seconds=60)  #last_minute variable to store the datetime from 1 min ago.
    similar_actions = Action.objects.filter(user_id=user.id, verb=verb, created_gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)

    if not similar_actions:
        #no existing actions found 
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False