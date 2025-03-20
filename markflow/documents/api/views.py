
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from markflow.documents.api.serializers import DocumentSerializer

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Document


class DocumentViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    lookup_field = "pk"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["title", "content","tags"]
    search_fields = ['created', 'updated']
