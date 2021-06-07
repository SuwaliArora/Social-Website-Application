# Django Social-Website Application
### About project-
This is a basic social network website developed using Django(Python Framework). It is an application that will allow users to share images they find	on	the internet.It has features like user's profile page, bookmarklet.

For Developers/Contributers: To Set up follow these steps -

   1. Run on git terminal
   
     git clone https://github.com/SuwaliArora/Social-Website-Application


   2. Change working directory to /Social-Website-Application

   3. make virtualenv

     virtual env <env-name>

   4. Activate your virtual environment

     source env/bin/activate

   5. Install requirements.txt

     pip install -r requirements.txt

   6. Run migrations :

     python manage.py migrate

   7. Run server :

     python manage.py runserver <port>

### Other Information

<strong>The following elements are used for this project:</strong>
1. An authentication system for users to register, log in, edit their profile, and change	or	reset	their	password.
2. A followers' system to allow users to follow	each other.
3. A functionality to display shared images and implement a bookmarklet for users to share images	from any website.
4. An	activity	stream for each user	that allows	users	to	see the content uploaded by the people they follow.

### Django Authentication Views
Django provides the following	class-based views	to	deal with authentication. All	of them are located in django.contrib.auth.views.<br>
<strong>LoginView:</strong> Handles	a login form and logs in a	user.<br>
<strong>LogoutView:</strong> Logs out a user.<br>

Django provides the following	views	to	handle password changes:<br>
<strong>PasswordChangeView:</strong> Handles	a form to change the	user password.<br>
<strong>PasswordChangeDoneView:</strong> The success view the user is redirected	to after a successful password change.<br>

Django also	includes	the following views to allow users to reset their password:<br>
<strong>PasswordResetView:</strong> Allows users to reset their password. It generates a one-time use link with a token and sends it to the user's email account.<br>
<strong>PasswordResetDoneView:</strong> Tells users that	an	email—including a	link to reset their password—has	been sent to them.<br>
<strong>PasswordResetConfirmView:</strong> Allows users to set	a new	password.<br>
<strong>PasswordResetCompleteView:</strong> The success view the user is redirected to after successfully resetting the password.

The Django development server	is	intended	only for	development and doesn't	support HTTPS. To	test the	bookmarklet	over HTTPS, we	will use	Ngrok. Ngrok is a	tool that creates	a tunnel	to	expose your	localhost to the internet through HTTP	and HTTPS.

Download	Ngrok for your	operating system from https://ngrok.com/download and run it from the	shell	using	the following command:

   ```
./ngrok http 8000
```

A decorator is a function that takes another	function and extends	the behavior of the latter	without explicitly modifying it.
