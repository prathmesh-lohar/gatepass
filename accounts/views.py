from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from userprofiles.models import userprofile


def register(request):
    if request.method == 'POST':
        # Get user data
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        gender = request.POST.get('gender', '')
        address_line = request.POST.get('address_line', '')
        address_distract = request.POST.get('address_distract', '')
        address_taluka = request.POST.get('address_taluka', '')
        address_pin_code = request.POST['address_pin_code']
        adhar_number = request.POST.get('adhar_number', '')
        mobile_number = request.POST.get('mobile_number', '')
        photo1 = request.FILES.get('photo1')
        photo2 = request.FILES.get('photo2')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("A user with this username already exists.")  # Or render an error message in the template

        # Check if the mobile number already exists
        if userprofile.objects.filter(mobile_number=mobile_number).exists():
            return HttpResponse("A user with this mobile number already exists.")  # Or render an error message in the template

        # Check if the Aadhaar number already exists
        if userprofile.objects.filter(adhar_number=adhar_number).exists():
            return HttpResponse("A user with this Aadhaar number already exists.")  # Or render an error message in the template

        # Create User
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create UserProfile linked to the user
        profile = userprofile(
            user=user,
            gender=gender,
            address_line=address_line,
            address_distract=address_distract,
            address_taluka=address_taluka,
            address_pin_code=address_pin_code,
            adhar_number=adhar_number,
            mobile_number=mobile_number,
            photo1=photo1,
            photo2=photo2
        )
        profile.save()

        # Log the user in after successful registration
        login(request, user)

        return redirect('login')  # Redirect to the login page after registration

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        adhar_number = request.POST['adhar_number']
        password = request.POST['password']

        # Get the userprofile using Aadhaar number
        try:
            user_profile = userprofile.objects.get(adhar_number=adhar_number)
            user = user_profile.user  # Get the related User object

            # Authenticate using the user and password
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("Login successful.")  # Redirect to a success page
            else:
                return HttpResponse("Invalid Aadhaar number or password.")
        
        except userprofile.DoesNotExist:
            return HttpResponse("User with this Aadhaar number does not exist.")

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # 