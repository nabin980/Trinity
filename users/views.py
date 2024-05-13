from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
# from django.contrib.auth.models import get_user_model
import random
import string
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from .forms import CustomUserForm, ProfileForm
from django.contrib import messages



def register_user(request):
    if request.method == 'POST':
        custom_user_form = CustomUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if custom_user_form.is_valid() and profile_form.is_valid():
            password = custom_user_form.cleaned_data['password']
            confirm_password = request.POST.get('cpword', None)

            if password != confirm_password:
                messages.error(request, "Registration Failed: Passwords do not match", extra_tags='failure')
            else:
                user = custom_user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                messages.success(request, 'Registration Successful', extra_tags='success')
        else:
            # Handle errors from both forms
            for field, errors in custom_user_form.errors.items():
                for error in errors:
                    messages.error(request, f'Registration Failed: {field.capitalize()} - {error}')
            for field, errors in profile_form.errors.items():
                for error in errors:
                    messages.error(request, f'Registration Failed: {field.capitalize()} - {error}')

    else:
        custom_user_form = CustomUserForm()
        profile_form = ProfileForm()
    
    return render(request, 'register_login.html', {'custom_user_form': custom_user_form, 'profile_form': profile_form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                verification_code = ''.join(random.choices(string.digits, k=6))
                user.profile.verification_code = verification_code
                user.profile.save()
                try:
                    send_mail(
                        'Admin Login Verification Code',
                        f'Your verification code is: {verification_code}',
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        fail_silently=False,
                    )
                    messages.success(request, 'Login Successful!. Check your email for verification code', extra_tags='success')
                    return redirect('admin-verify')
                except:
                    messages.error(request, 'Email not found. Please check valid email address.')
            else:
                messages.success(request, 'Login Successful', extra_tags='success')  # Added extra_tags
                return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'register_login.html')

def register_login(request):
    custom_user_form = CustomUserForm()
    profile_form = ProfileForm()

    return render(request, 'register_login.html', {'custom_user_form': custom_user_form, 'profile_form': profile_form})

def logout_view(request):
    user = request.user
    if user.is_authenticated and user.profile.is_verified:
        user.profile.is_verified = False
        user.profile.save()
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email = email).first()
        if user is not None:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(
                reverse('reset-password', args=[uid, token])
            )
            
            send_mail(
                'Password Reset',
                f'Click the link to reset your password: {reset_link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Email with password reset link has been sent')
        else: 
            messages.error(request, 'There was a problem submitting')
    return render(request, 'forgot_password.html')

def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            user.set_password(new_password)
            user.save()
            # Optionally, log in the user after password reset
            # login(request, user)
            messages.success(request, 'Password reset successful')
            return redirect('register_login')  
        return render(request, 'reset_password.html')  
    else:
        messages.error(request, 'Invalid reset link/token. Please try again.')
        return redirect('forgot-password') 

def admin_verify(request):
    if request.method == 'POST':
        submitted_code = request.POST.get('verification_code')
        user = request.user  # Assuming the admin user is already authenticated

        if user.profile.verification_code == submitted_code:
            user.profile.is_verified = True
            user.profile.verification_code = None
            user.profile.save()
            messages.success(request, 'Verification successful. You are now logged in.')
            return redirect('admin_dashboard')  
        else:
            messages.error(request, 'Invalid verification code. Please try again.')

    return render(request, 'admin_verify.html')