from rest_framework import serializers

from .models import Advisor, User,Booking

class AdvisorSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = (
            'id','name', 'photo_url',
        )
class RegisterUserSerielizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'name', 'email', 'password',
        )
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'adv_id', 'dateTime', 'user_id')

