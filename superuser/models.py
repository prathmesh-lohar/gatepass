from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Custom Field for Registration Number
class RegistrationNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        # Set default max_length only if it's not provided in kwargs
        kwargs.setdefault('max_length', 10)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if not getattr(model_instance, self.attname):
            prefix = "A"  # Replace with your desired prefix
            next_number = self.get_next_number(model_instance.__class__)
            formatted_number = f"{prefix}{next_number:05d}"
            setattr(model_instance, self.attname, formatted_number)
            return formatted_number
        return super().pre_save(model_instance, add)

    def get_next_number(self, model_class):
        last_instance = model_class.objects.order_by('register_number').last()
        if last_instance:
            last_number = int(last_instance.register_number[1:6])
            return last_number + 1
        return 1



# User Profile Model
class adminprofile(models.Model):
    register_number = RegistrationNumberField(unique=True)  # No need to pass max_length here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    
    address_line = models.CharField(max_length=255, blank=True, null=True)
    address_distract = models.CharField(max_length=255, blank=True, null=True)
    address_taluka = models.CharField(max_length=255, blank=True, null=True)
    address_pin_code = models.IntegerField()
    
    adhar_number = models.IntegerField(blank=True, null=True)
    mobile_number = models.IntegerField(blank=True, null=True)
    photo1 = models.ImageField(upload_to="admin/photos", blank=True, null=True)
    photo2 = models.ImageField(upload_to="admin/photos", blank=True, null=True)
    
    type = models.CharField(max_length=255, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.user.username} - {self.adhar_number}"
