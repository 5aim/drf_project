from dataclasses import field
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validation_data):
        user = super().create(validation_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validation_data):
        user = super().create(validation_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user