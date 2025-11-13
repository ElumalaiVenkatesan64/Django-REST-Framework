from rest_framework.serializers import ModelSerializer
from .models import *


class UserProfile_Serializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

        