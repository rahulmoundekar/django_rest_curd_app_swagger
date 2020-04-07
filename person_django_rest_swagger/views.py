# Create your views here.
from rest_framework import viewsets

from person_django_rest_swagger.models import Person
from person_django_rest_swagger.serializers import PersonSerializer


class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
