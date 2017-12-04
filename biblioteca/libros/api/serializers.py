from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer #paso 5
from libros.models import  Libro

class LibroModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) #PASO 5
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Libro
        fields = [
            "id",
            "user",
            "Nombre",
            "Autor",
            "Editorial",
            "ISBN",
            "precio",
            "created",
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.created.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.created) + " ago"
