from django.shortcuts import render
from . import forms
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
import cloudinary.uploader
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        return redirect('login')
    else:
        form=forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username') 
        password = request.POST.get('password')

        user = authenticate(username=username_or_email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, "Invalid username/email or password")
            return redirect('login')
    else:
        return render(request, "login.html")

def dashboard(request):
    if not(request.user.is_authenticated):
        return render(request, '1045.html')
    return render(request,'dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect("login")

@login_required
def profile(request):
    user=request.user
    name=user
    email=user.email
    lname=user.last_name
    fname=user.first_name
    profile_picture = user.profile_picture.url if user.profile_picture else None
    return render(request,'profile.html',{'name':name,'email':email,'lname':lname,'fname':fname, 'profile_picture':profile_picture})

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            
            if form.cleaned_data.get('remove_profile_picture') and user.profile_picture:
                try:
                    public_id = user.profile_picture.public_id
                    cloudinary.uploader.destroy(public_id)  # Delete from Cloudinary
                    user.profile_picture = None  # Remove from database
                except Exception as e:
                    messages.error(request, f"Error deleting profile picture: {e}")

            user.save()
            return redirect('profile')
    else:
        form = forms.EditProfileForm(instance=request.user)
    return render(request, 'editprofile.html', {'form': form})

# @login_required
def change_password(request):
    if not(request.user.is_authenticated):
        return render(request, '1045.html')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevents logout after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')  # Redirect to profile page after success
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})