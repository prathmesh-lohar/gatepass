from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import qrcode
import io
from io import BytesIO
from django.db import models

from django.core.files.base import ContentFile
from datetime import date, time, datetime

from django.core.exceptions import MultipleObjectsReturned


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
class userprofile(models.Model):
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
    photo1 = models.ImageField(upload_to="userprofiles/photos", blank=True, null=True)
    photo2 = models.ImageField(upload_to="userprofiles/photos", blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.adhar_number}"




class GatepassNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 10)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        # Get the field name dynamically from the model instance
        field_name = self.attname  # Correctly get the field name from the attribute name
        
        # Check if the gatepass_number is already set
        if not getattr(model_instance, field_name):
            prefix = "GP"
            next_number = self.get_next_number(model_instance.__class__)
            formatted_number = f"{prefix}{next_number:05d}"
            setattr(model_instance, field_name, formatted_number)
            return formatted_number
        return super().pre_save(model_instance, add)

    def get_next_number(self, model_class):
        # Get the last gatepass number and increment it
        last_instance = model_class.objects.order_by('gatepass_number').last()
        if last_instance:
            last_number = int(last_instance.gatepass_number[2:])  # Assuming format 'GP00001'
            return last_number + 1
        return 1


class gatepass(models.Model):
    gatepass_number = GatepassNumberField(unique=True, blank=True, null=True, max_length=100)  # Set null=True to allow it to be empty initially
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    PASS_CHOICES = [
        ('guest', 'guest'),
        ('vip', 'vip'),
    ]
    pass_type = models.CharField(max_length=10, choices=PASS_CHOICES, default='guest')

    APP_CHOICES = [
        ('pass', 'pass'),
        ('pending', 'pending'),
        ('reject', 'reject'),
    ]
    master_admin_approval = models.CharField(max_length=10, choices=APP_CHOICES, default='pending')

    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Ensure gatepass_number is populated if not already set
        if not self.gatepass_number:
            # This explicitly calls the pre_save method of the custom field
            self.gatepass_number = GatepassNumberField().pre_save(self, False)

        # Handle QR code generation only after gatepass_number is set
        if not self.qr_code:
            qr_data = {
                "User": self.user.username,
                "Pass Type": self.pass_type,
                "Gate Pass Number": self.gatepass_number,  # Include gate pass number
                "Time": self.time.isoformat() if isinstance(self.time, (time, datetime)) else "N/A",
            }

            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')

            # Save QR code to a BytesIO object
            buf = BytesIO()
            img.save(buf)
            buf.seek(0)

            # Save QR code as an image file
            file_name = f"gatepass_qr_{self.user.username}.png"
            self.qr_code.save(file_name, ContentFile(buf.read()), save=False)

        # Proceed with the actual save after QR code and gatepass_number are set
        super().save(*args, **kwargs)
 

class entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    # gatepass = models.ForeignKey(gatepass, on_delete=models.CASCADE)
    gatepass = models.CharField(blank=True,null=True, max_length=50)
    
    time_in = models.TimeField(blank=True, null=True)
    time_out = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    
    image_type =  models.CharField(blank=True,null=True, max_length=50)
    matching_percentage = models.IntegerField(blank=True,null=True,)
    activities = models.CharField(blank=True,null=True, max_length=50)
    alert = models.CharField(blank=True,null=True, max_length=50)
    action = models.CharField(blank=True,null=True, max_length=50)
    
    detected_face  = models.ImageField(upload_to="detected_faces", height_field=None, width_field=None, max_length=None, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.gatepass}- {self.time_in}- {self.time_out} - {self.date}"
