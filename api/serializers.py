from rest_framework import serializers
from userprofiles.models import gatepass,entry

class GatepassSerializer(serializers.ModelSerializer):
    class Meta:
        model = gatepass
        # fields = ['gatepass_number', 'user', 'date', 'time',  'pass_type', 'master_admin_approval', 'qr_code']
        fields = '__all__'

    def create(self, validated_data):
        # You can handle the gatepass_number and qr_code generation here
        gatepass_instance = super().create(validated_data)
        
        # Add custom logic for generating gatepass_number and QR code if needed
        gatepass_instance.save()  # Save after custom logic
        
        return gatepass_instance
    
    



class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = entry
        # fields = ['id', 'user', 'gatepass', 'time_in', 'time_out', 'date']
        fields = '__all__'
        
