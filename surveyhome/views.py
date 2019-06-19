# Create your views here.
from __future__ import print_function
from django.shortcuts import render, redirect, render_to_response
from django.views import generic
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from surveyhome.forms import Register
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from .forms import ContactForm
from django.contrib import auth, messages
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
import re

def index(request):
    context={}
    return render(request, 'index.html', context=context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username)
        print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            LOGIN_REDIRECT_URL='/surveyhome/'
            return redirect('dashboard')
        else:
            # Show an error page
            messages.info(request, 'Your User Name and Password does not match!!')
            template = 'signin.html'
            return render(request,template)
    else:
        return render(request, 'signin.html')

def register(request):
    print("entered register view")
    if request.method == 'POST':
        form = Register(data=request.POST)
        print("post is successful")
        if form.is_valid():
            print("form is valid")
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print(user.pk)
            current_site = get_current_site(request)
            mail_subject = 'Activate your Survey Booth account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            print(form.errors)
            messages.info(request,form.errors)
            print("form not valid")
            return redirect('index')

    else:
        form = Register()
        return render(request,'signup.html')


def activate(request, uidb64, token):
    try:
        print(uidb64)
        uid = urlsafe_base64_decode(uidb64)
        print(uid)
        user = User.objects.get(pk=uid)
        print(user)
        print(account_activation_token.check_token(user, token))
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')

def logout_view(request):
    auth.logout(request)
    redirect(index)

def dashboard(request):
    context={}
    return render(request, 'dashboard.html',{'context': context})

def password_change(request):
    context={}
    return render(request, 'password_reset.html',{'context': context})

def passwordreset_mail(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        user = User.objects.get(username = username)
        to_email = user.email
        current_site = get_current_site(request)
        mail_subject = 'Reset your Survey Booth Password'
        message = render_to_string('password_reset_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token':account_activation_token.make_token(user),
        })
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return render(request,'password_reset_confirm.html')

    else:
        print("the request is not post")
    return render(request,'password_reset.html')



def passwordreset(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if request.method == 'POST':
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')
        if user is not None and account_activation_token.check_token(user, token) and (password == confirm_password) :
            user.set_password(password)
            user.save()
            return render(request,'password_reset_done.html')
        else:
            return HttpResponse('Password reset link is invalid!')
    else:
        print("Request is not post yet")
        context = {
        'uid': uidb64,
        'token': token,
        }
    return render(request,'password_reset_complete.html', context = context)


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['bsaranyabogendiran@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contactus.html", {'form': form})

def successView(request):
    return render(request, "contact_success_email.html")


def validate_registerform(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password1', None)
    confirm_password = request.GET.get('password2', None)
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    email = request.GET.get('email',None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),
        'invalid_email': not (EMAIL_REGEX.match(str(email)))
    }
    if data['is_taken']:
        data['username_error_message'] = 'A user with this username already exists.'
    if data['invalid_email']:
        data['invalid_email_error'] = 'Please enter the valid email ID.'
    return JsonResponse(data)
