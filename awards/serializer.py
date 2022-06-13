from rest_framework import serializers
from .models import *


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ('site_title', 'site_description', 'site_image', 'author', 'pub_date', 'link', 'country')

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'photo',)