from .models import Question
from rest_framework import serializers

class QusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'status','create_by')