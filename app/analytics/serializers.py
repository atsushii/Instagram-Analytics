from rest_framework import serializers
from core.models import InstagramAccount, \
    InstagramComment, \
    InstagramMedia, \
    InstagramMediaTag, \
    InstagramMediaLocation


class InstagramAccountSerializer(serializers.ModelSerializer):
    """Serializer for instagram account"""

    class Meta:
        model = InstagramAccount
        fields = ('id', 'tag')


class InstagramCommentSerializer(serializers.ModelSerializer):
    """Serializer for comments"""

    class Meta:
        model = InstagramComment
        fields = ('id',
                  'from_username',
                  'comment',
                  'created_time')
