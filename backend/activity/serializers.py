from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'activity_id',
            'robot_id',
            'on_time',
            'off_time',
            'active_time',
            'scans',
            'wifi',
            'cam',
            ]


    def create(self, validated_data):
        print("Validated_data:",validated_data)
        instance = Activity.objects.create(**validated_data)
        return instance

