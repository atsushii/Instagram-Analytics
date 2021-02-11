from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user object"""

    def create(self, validated_data):
        """Create new user"""
        return get_user_model().objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'instagram_account')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}


class LogInSerializer(serializers.Serializer):
    """Serializer for the user authentication obj"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'passsword'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            passworf=password
        )

        if not user:
            msg = ('Unable to login')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
