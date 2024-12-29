from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home(request):
    
    return render (request, "superuser\home.html")


def entry(request,id):
    from userprofiles.models import entry

    entry = entry.objects.filter(id=id).first()
    
    user=entry.user
   
    data = {
        'entry': entry,
        'user': user
    }
    return render (request, "superuser/entry.html",data)


def latest_entry_json(request):
    from userprofiles.models import entry
    entry = entry.objects.last()  # Fetch the latest entry
    
    profile_picture = entry.user.userprofile.photo1.url
    
    
    if entry:
        data = {
            'entry': {          
                'user': entry.user.username,  # Adjust field as per your model
                'gatepass': entry.gatepass,  # Example
                'time_in': entry.time_in,  # Example
                'time_out': entry.time_out,  # Example
                'date': entry.date,  # Example
                # 'image_type': entry.image_type,  # Example
                'matching_percentage': entry.matching_percentage,  # Example
                'activities': entry.activities,  # Example
                'alert': entry.alert,  # Example
                'action': entry.action,  # Example
                'detected_face': entry.detected_face.url,  # Example
                'profile_picture':profile_picture,
                'dtected_face_file_id':entry.dtected_face_file_id
              
            }
        }
    else:
        data = {'entry': None}
    return JsonResponse(data)


def live_entry(request):
    from userprofiles.models import entry

    # entry = entry.objects.all().last()
    # user=entry.user
   
    # data = {
    #     'entry': entry,
    #     'user': user
    # }
    return render (request, "superuser/real_time_entry.html")
