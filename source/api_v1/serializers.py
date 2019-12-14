from rest_framework.serializers import ModelSerializer
from webapp.models import Comments


class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'text', 'created_at', 'status',
                  'author_name', 'author_email', 'rating')
