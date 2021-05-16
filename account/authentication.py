#authentication backend. Django	allows	you	to	authenticate	against	different	sources.	The
#AUTHENTICATION_BACKENDS	setting	includes	the	list	of	authentication
#backends	for	project.
from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    #The authenticate()	method receives	a request object & username	and password as optional parameters.
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password): #built-in check_password() method	of user	model.
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id): #get a user through the iD set in the user_id parameter
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None