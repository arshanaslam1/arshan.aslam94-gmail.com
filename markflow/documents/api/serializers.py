from rest_framework import serializers

from markflow.documents.models import Document


class DocumentSerializer(serializers.ModelSerializer[Document]):
    class Meta:
        model = Document
        fields = "__all__"
