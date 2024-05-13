from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from django.urls import reverse
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import QuotationRequestForm, UserExperienceForm
from .models import QuotationRequest, UserExperience

# Create your views here.
def admin_dashboard(request):
    if request.user.is_superuser and request.user.profile.is_verified:
        # Get the search query from the request GET parameters
        search_query = request.GET.get('q', '')
        
        # Filter quotation requests based on search query
        quotation_requests = QuotationRequest.objects.filter(
            Q(name__icontains=search_query) |  # Add more fields for searching as needed
            Q(email__icontains=search_query) |
            Q(contact_number__icontains=search_query) |
            Q(quotation_request__icontains=search_query)
        ).order_by('is_mailed','created_at')

        paginator = Paginator(quotation_requests, 3)
        page = request.GET.get('page')
        try:
            quotation_requests = paginator.page(page)
        except PageNotAnInteger:
            quotation_requests = paginator.page(1)
        except EmptyPage:
            quotation_requests = paginator.page(paginator.num_pages)

        return render(request, 'admin_dash.html', {'quotation_requests': quotation_requests, 'search_query': search_query})
    else:
        return render(request, 'register_login.html')
    
@login_required(login_url='register_login')
def list_users(request):
    if not (request.user.is_superuser and request.user.profile.is_verified ):
        return render(request, 'register_login.html')

    # Get the search query from the request GET parameters
    search_query = request.GET.get('q', '')

    User = get_user_model()

    # Filter users based on search query
    users_with_profiles = User.objects.select_related('profile').filter(
        Q(is_superuser=False),
        Q(email__icontains=search_query) |
        Q(profile__fullname__icontains=search_query)
    ).distinct()

    paginator = Paginator(users_with_profiles, 3)
    page = request.GET.get('page')

    try:
        users_data = paginator.page(page)
    except PageNotAnInteger:
        users_data = paginator.page(1)
    except EmptyPage:
        users_data = paginator.page(paginator.num_pages)

    return render(request, 'user_list.html', {'users': users_data, 'search_query': search_query})

@login_required(login_url='register_login')
def delete_user(request, user_id):
    if request.user.is_superuser and request.user.profile.is_verified:
        user = get_object_or_404(get_user_model(), id=user_id)
        user.delete()
        messages.success(request, f'User "{user.email}" has been deleted successfully')
        return redirect('list_users')
    else:
        messages.error(request, 'Failed to delete the user')
        return HttpResponseForbidden("You are not authorized to perform this action")

@login_required(login_url='register_login')
def booking_list(request):
    if not (request.user.is_superuser and request.user.profile.is_verified ):
        return render(request, 'register_login.html')

    # Get the search query from the request GET parameters
    search_query = request.GET.get('q', '')

    quotation_requests = QuotationRequest.objects.filter(
        Q(name__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(contact_number__icontains=search_query) |
        Q(quotation_request__icontains=search_query)
    ).order_by('is_mailed','created_at')

    paginator = Paginator(quotation_requests, 3)
    page = request.GET.get('page')

    try:
        quotation_requests = paginator.page(page)
    except PageNotAnInteger:
        quotation_requests = paginator.page(1)
    except EmptyPage:
        quotation_requests = paginator.page(paginator.num_pages)

    return render(request, 'booking_list.html', {'quotation_requests': quotation_requests, 'search_query': search_query})

@login_required(login_url='register_login')
def user_experiences(request):
    if request.user.is_superuser and request.user.profile.is_verified:
        # Get the search query from the request GET parameters
        search_query = request.GET.get('q', '')

        # Filter user experiences based on search query
        user_experiences = UserExperience.objects.filter(
            Q(profile__fullname__icontains=search_query) |
            Q(comment__icontains=search_query)
        ).order_by('-created_at')

        paginator = Paginator(user_experiences, 3)
        page = request.GET.get('page')

        try:
            user_experiences = paginator.page(page)
        except PageNotAnInteger:
            user_experiences = paginator.page(1)
        except EmptyPage:
            user_experiences = paginator.page(paginator.num_pages)

        return render(request, 'user_experiences.html', {'user_experiences': user_experiences, 'search_query': search_query})
    else:
        return render(request, 'register_login.html')

@login_required(login_url='register_login')
def delete_user_experience(request, user_experience_id):
    if request.user.is_superuser and request.user.profile.is_verified:
        user_experience = get_object_or_404(UserExperience, id=user_experience_id)
        user_experience.delete()
        # Redirect to the user experiences tab after deletion
        messages.success(request, 'User Experience has been deleted')
        return HttpResponseRedirect(reverse('user_experiences'))
    else:
        return render(request, 'register_login.html')

# @login_required(login_url='register_login')
def contact_us(request):
    # if not request.user.is_authenticated:
    #     messages.warning(request, 'Login is required')
    #     return redirect('register_login')
    # else:
    return render(request, 'contact.html')

def quotation_request(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = QuotationRequestForm(request.POST)
            if form.is_valid():
                quotation_request_instance = form.save(commit=False)
                quotation_request_instance.profile = request.user.profile 
                quotation_request_instance.save()
                messages.success(request, 'Quotation requested successfully')
                return render(request, 'home.html')
            else:
                if 'contact_number' in form.errors:
                    messages.error(request, form.errors['contact_number'][0])
                    return render(request, 'contact.html')
                else:
                    messages.error(request, 'Failed to submit')
        else:
            form = QuotationRequestForm()
        return render(request, 'quotation_request.html', {'form': form})
    else:
        messages.error(request, 'You need to be logged in to request a quotation.')
        return redirect('register_login')

@login_required(login_url='register_login')
def delete_quotation_request(request, quotation_request_id):
    if request.user.is_superuser and request.user.profile.is_verified and request.method == 'POST':
        quotation_request = get_object_or_404(QuotationRequest, id=quotation_request_id)
        quotation_request.delete()
        messages.success(request, 'Quotation requested deleted successfully')
        return redirect('booking_list')
    else:
        messages.error(request, 'Could not delete quotation request')
        return redirect('booking_list')

def index(request):
    return render(request, 'index.html')

def homepage(request):
    testimonials = UserExperience.objects.filter(is_published=True).order_by('-created_at')[:3]
    return render(request, 'home.html', {'testimonials': testimonials})

@login_required(login_url='register_login')
def send_email(request, quotation_request_id):
    if request.user.is_superuser and request.user.profile.is_verified:  # Check if the user is a superuser
        if request.method == 'POST':
            quotation_request = get_object_or_404(QuotationRequest, id=quotation_request_id)
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            recipient_name = quotation_request.name
            recipient = quotation_request.email
            recipient_list = [recipient]  # Create a list for send_mail

            full_message = f"Hello {recipient_name},\n\n{message}"

            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            # Add success message or redirect to appropriate page

            quotation_request.is_mailed = True
            quotation_request.save()
            messages.success(request, 'Mail sent successfully')
            search_query = request.GET.get('q', '')
            redirect_url = reverse('admin_dashboard') + f'?q={search_query}' if search_query else reverse('admin_dashboard')
            return HttpResponseRedirect(redirect_url)
        else:
            messages.error(request, 'Could not send mail')
            
        return render(request, 'booking_list.html')
    else:
        messages.error(request, 'You are not authorized to perform this action.')
        return redirect('register_login')
    
@login_required(login_url='register_login')
def share_user_experience(request):
    quotation_request = QuotationRequest.objects.filter(
        profile = request.user.profile,
    ).first()

    if quotation_request:
        if request.method == 'POST':
            experience_form = UserExperienceForm(request.POST, request.FILES)
            # print(request.user.profile)
            if experience_form.is_valid():
                experience = experience_form.save(commit=False)
                experience.profile = request.user.profile

                if 'image' in request.FILES:
                    uploaded_image = request.FILES['image']
                    print(f"Uploaded image: {uploaded_image.name}")
                    print(f"Content Type: {uploaded_image.content_type}")
                    print(f"Size: {uploaded_image.size} bytes")
                    experience.picture = uploaded_image

                print(experience)
                experience.save()
                messages.success(request, 'Thank you for sharing you experience!')
            else:
                messages.error(request, 'There was a problem submitting. Please try again later.')
        else:
            experience_form = UserExperienceForm()

        return render(request, 'home.html', {'experience_form': experience_form})
    else:
        return redirect('contact_us')

@login_required(login_url='register_login')   
def publish_testimonials(request):
    if request.user.is_superuser and request.user.profile.is_verified and request.method == 'POST':
        user_experience_id = request.POST.get('user_experience_id')
        user_experience = get_object_or_404(UserExperience, id=user_experience_id)
        user_experience.is_published = True
        user_experience.save()
        messages.success(request, 'Testimonial published successfully!')
    else:
        messages.error(request, 'Could not publish testimonial')
        return redirect('user_experiences')