from .models import Person
from rest_framework import serializers

class personSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'