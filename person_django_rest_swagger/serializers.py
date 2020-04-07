from rest_framework import serializers

from person_django_rest_swagger.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
