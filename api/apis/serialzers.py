from rest_framework import serializers
from api.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    
    username = serializers.SerializerMethodField('get_username_from_author')
    
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'date_posted', 'username']
        
    def get_username_from_author(self, blog):
        username = blog.author.username
        return username
