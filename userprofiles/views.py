from django.shortcuts import render,redirect
from userprofiles.models import gatepass  # Import the gatepass model (use lowercase for the model name)
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime

@login_required
def home(request):
    # # Get all gate passes for the logged-in user
    # gatepasses = gatepass.objects.filter(user=request.user)

    # show_apply_button = True  # Default to showing the button, assuming no valid pass

    # if gatepasses.exists():
    #     # Loop through each gate pass to check its status
    #     for user_gatepass in gatepasses:
    #         # Check if the gate pass is approved
    #         # if user_gatepass.master_admin_approval == 'pass':
    #         #     # Check if both time_in and time_out are present
    #         #     # if  user_gatepass.time_out:
    #         #     #     show_apply_button = True  # Do not show the apply button if both are present
    #         #     #     break  # Exit the loop since we found a valid pass

    #         # If the gate pass is rejected, allow applying again
            
    #         if user_gatepass.master_admin_approval == 'reject':
    #             show_apply_button = True
    #             break  # Exit the loop since a rejected pass allows applying again

    # else:
    #     # No gate pass found, allow the user to apply for a new one
    #     show_apply_button = True

    # data = {
    #     'show_apply_button': show_apply_button,
    #     'gatepasses': gatepasses  # All gate passes of the user
    # }

    return render(request, 'userprofiles/base.html')


@login_required
def apply_gatepass(request):
    print("apply_gatepass view called")  # Debug statement

    if request.method == 'POST':
        print("POST request received")  # Debug statement
        
        # Get the submitted data from the form
        date = request.POST.get('date')
        time = request.POST.get('time')
        pass_type = request.POST.get('pass_type')

        print(f"Received data - Date: {date}, Time: {time}, Pass Type: {pass_type}")  # Debug statement

        # Ensure data is provided
        if not date or not time or not pass_type:
            print("Error: Missing required fields")  # Debug statement
            return render(request, 'userprofiles/apply_gatepass.html', {
                'error_message': 'All fields are required!'
            })

        # Create a new gatepass object
        new_gate_pass = gatepass(user=request.user, date=date, time=time, pass_type=pass_type)

        # Save the new gatepass object
        try:
            new_gate_pass.save()
            print("New gatepass saved successfully")  # Debug statement
            # Redirect the user after saving the gatepass
            return redirect('home')  # Replace 'home' with the actual URL name of your home page
        except Exception as e:
            print(f"Error saving gatepass: {e}")  # Debug statement for save error
            return render(request, 'userprofiles/apply_gatepass.html', {
                'error_message': 'There was an error saving your gatepass.'
            })

    # Render the template to apply for a gatepass
    print("Rendering the gatepass application form")  # Debug statement
    return render(request, 'userprofiles/apply_gatepass.html')