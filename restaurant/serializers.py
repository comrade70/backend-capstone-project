from django.contrib.auth.models import User
from models import Booking, Menu
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializers(serializers.ModelSerializers):
    class Meta:
        model = Booking
        fields = []

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = []
