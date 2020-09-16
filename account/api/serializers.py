from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    # the meta class for calling the fields and model
    class Meta:
        model = User
        fields = ['username','first_name','email','password','password2']

    # function for saving a new user
    def save(self):
        account = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'passwords do not match'})
        account.set_password(password)
        account.save()
        return account