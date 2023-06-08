from rest_framework import serializers
from .models import Students
class studentsSerilizers(serializers.ModelSerializer):

    class Meta:
        model=Students
        fields='__all__'





    # name= serializers.CharField(max_length=50)
    # roll=serializers.IntegerField()
    # city=serializers.CharField(max_length=50)

    # def create(self, validated_data):
    #     return Students.objects.create(**validated_data)