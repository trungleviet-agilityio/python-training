from rest_framework import serializers
from .models import BlogPost


class BaseModelSerializer(serializers.ModelSerializer):
    """Base serializer with common functionality."""
    
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        abstract = True


class BlogPostSerializer(BaseModelSerializer):
    """Serializer for BlogPost model."""
    
    author_name = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'content', 'author', 'author_name',
            'status', 'featured_image', 'view_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['view_count', 'created_at', 'updated_at']
    
    def get_author_name(self, obj):
        """Get the author's full name."""
        return obj.author.get_full_name() or obj.author.email 