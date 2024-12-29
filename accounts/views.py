from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from userprofiles.models import userprofile
from django.contrib import messages


# def register(request):
#     if request.method == 'POST':
#         # Get user data
#         username = request.POST['username']
#         password = request.POST['password']
#         first_name = request.POST.get('first_name', '')
#         last_name = request.POST.get('last_name', '')
#         gender = request.POST.get('gender', '')
#         address_line = request.POST.get('address_line', '')
#         address_distract = request.POST.get('address_distract', '')
#         address_taluka = request.POST.get('address_taluka', '')
#         address_pin_code = request.POST['address_pin_code']
#         adhar_number = request.POST.get('adhar_number', '')
#         mobile_number = request.POST.get('mobile_number', '')
#         photo1 = request.FILES.get('photo1')
#         photo2 = request.FILES.get('photo2')

#         # Check if the username already exists
#         if User.objects.filter(username=username).exists():
#             return HttpResponse("A user with this username already exists.")  # Or render an error message in the template

#         # Check if the mobile number already exists
#         if userprofile.objects.filter(mobile_number=mobile_number).exists():
#             return HttpResponse("A user with this mobile number already exists.")  # Or render an error message in the template

#         # Check if the Aadhaar number already exists
#         if userprofile.objects.filter(adhar_number=adhar_number).exists():
#             return HttpResponse("A user with this Aadhaar number already exists.")  # Or render an error message in the template

#         # Create User
#         user = User.objects.create_user(username=username, password=password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()

#         # Create UserProfile linked to the user
#         profile = userprofile(
#             user=user,
#             gender=gender,
#             address_line=address_line,
#             address_distract=address_distract,
#             address_taluka=address_taluka,
#             address_pin_code=address_pin_code,
#             adhar_number=adhar_number,
#             mobile_number=mobile_number,
#             photo1=photo1,
#             photo2=photo2
#         )
#         profile.save()

#         # Log the user in after successful registration
#         login(request, user)

#         return redirect('login')  # Redirect to the login page after registration

#     return render(request, 'accounts/register.html')

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



def register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('/accounts/register')

        try:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose a different username.")
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, "Account created successfully!")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    # messages.success(request, "Login successful!")
                    # return redirect('/')  # Replace with the name of your home or dashboard URL.
                else:
                    messages.error(request, "Invalid username or password.")
                    # return redirect('/accounts/login')
                return redirect('/accounts/adhar_verify')  # Replace 'login' with the name of your login URL.
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('/accounts/register')
        
    
    return render(request, 'accounts/create_account.html')



def adhar_verify(request):

    if request.method == "POST":
        aadhaar_number = request.POST.get("adhar")

        try:
            # Assuming `UserProfile` is the correct model name
            user_profile = userprofile.objects.get(user=request.user)  # Use the correct model name here
            user_profile.adhar_number = aadhaar_number
            user_profile.save()
            messages.success(request, "Aadhaar number updated successfully.")
        except userprofile.DoesNotExist:  # Reference the model class, not the variable
            messages.error(request, "User profile not found. Please ensure your account is properly set up.")
        
        return redirect("/accounts/profile_register")
    
    return render(request, 'accounts/adhar_verify.html')




def profile_register(request):
    
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        mobile_number = request.POST.get('mobile_number')
        photo1 = request.FILES.get('picture__input')
        photo2 = request.FILES.get('picture__input2')
        photo3 = request.FILES.get('picture__input3')

        # Save to the database
        user_profile = userprofile.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            address=address,
            mobile_number=mobile_number,
            photo1=photo1,
            photo2=photo2,
            photo3=photo3,
        )
        user_profile.save()

        # Redirect to success page or render a success message
        messages.success(request, "profiles saved")
        return redirect('/')  # Replace 'success_page' with your success URL
    
    return render(request, 'accounts/profile_register.html')
