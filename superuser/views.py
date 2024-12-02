from django.shortcuts import render

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
    return render (request, "superuser\entry.html",data)