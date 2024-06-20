from .models import Picture
from rest_framework import serializers

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = [
            'picture_id',
            'robot_id',
            'url',
            'file_name',
            'file_data',
            'inf_result',
            'inf_conf',
            'cap_time',
            'status',
            'inference_ms',
            ]
        
    def create(self, validated_data):
        print("Validated Data:",validated_data)
        instance = Picture.objects.create(**validated_data)
        return instance