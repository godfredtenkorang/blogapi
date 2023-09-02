from rest_framework import serializers
from api.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    
    # username = serializers.SerializerMethodField('get_username_from_author')
    
    class Meta:
        model = Blog
        fields = ['url', 'title', 'content', 'image', 'date_posted', 'author',]
        
    # def get_username_from_author(self, blog):
    #     username = blog.author.username
    #     return username
