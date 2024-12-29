import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from userprofiles.models import gatepass  # Replace 'your_app' with your actual app name
from datetime import datetime

# Generate unique gatepass numbers
def generate_unique_gatepass_number():
    # Example logic for unique gatepass numbers; customize as needed
    last_gatepass = gatepass.objects.order_by('-gatepass_number').first()
    return (last_gatepass.gatepass_number + 1) if last_gatepass and last_gatepass.gatepass_number else 1

# Fetch all users
users = User.objects.all()

for user in users:
    try:
        # Check if a gate pass already exists for the user
        if not gatepass.objects.filter(user=user).exists():
            # Create a new gate pass
            current_datetime = datetime.now()
            gate_pass = gatepass(
                user=user,
                gatepass_number=generate_unique_gatepass_number(),
                date=current_datetime.date(),
                time=current_datetime.time(),
                pass_type='guest',  # Default pass type, can be customized
                master_admin_approval='pass',  # Default approval status
            )

            # Generate QR code for the gate pass
            qr_data = {
                "User": user.username,
                "Pass Type": gate_pass.pass_type,
                "Gate Pass Number": gate_pass.gatepass_number,
                "Date": str(gate_pass.date),
                "Time": str(gate_pass.time),
            }

            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')

            # Save QR code as an image file
            buf = BytesIO()
            img.save(buf)
            buf.seek(0)
            file_name = f"gatepass_qr_{user.username}.png"
            gate_pass.qr_code.save(file_name, ContentFile(buf.read()), save=False)

            # Save the gate pass to the database
            gate_pass.save()
            print(f"Gate pass generated for user: {user.username}, Gate Pass Number: {gate_pass.gatepass_number}")
        else:
            print(f"Gate pass already exists for user: {user.username}")
    except Exception as e:
        print(f"Error generating gate pass for user: {user.username}, Error: {e}")
