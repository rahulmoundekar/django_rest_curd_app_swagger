# Django Rest Swagger Steps :

 It automatically generates documentation for your API endpoints and all you need to do to enable this ‘cool’ feature is include it in your URL configuration file.
 Django REST framework has a support for a couple of them. One of them is Django REST Swagger, used for generating well known Swagger documentation. We’ll quickly go over a few steps necessary to get it up and running:.

# Project Setup

  - Making the project as :
     ```
        mkdir django_rest_curd_app
		cd django_rest_curd_app
    ```
  - Install Django and DjangoRestFramework:
    ```
        pip install django
		pip install djangorestframework
    ```
  - Make apps (for class based views)
    ```
       django-admin startapp person_django_rest_swagger
    ```
 - Integrating Django Rest
    ```
       pip install djangorestframework
    ```
 - Add 'rest_framework' and both apps to settings.py as:
    ```
       INSTALLED_APPS = [
				...
				'rest_framework',
				'demo',
	   ]
    ```
 - Make a model
     ```
        from django.db import models
           
        class Person(models.Model):
            name = models.CharField(max_length=45)
            mobile = models.CharField(max_length=45)
        
            def __unicode__(self):
                return self.name
        
            class Meta:
                db_table = "person"
     ``` 
 - Make a serializer
     ``` 
        from rest_framework import serializers
        from person_django_rest_swagger.models import Person
    
        class PersonSerializer(serializers.ModelSerializer):
            class Meta:
                model = Person
                fields = '__all__'
    ``` 
 - Make a view
     ``` 
       from rest_framework import viewsets
       from person_django_rest_swagger.models import Person
       from person_django_rest_swagger.serializers import PersonSerializer
        
        class PersonView(viewsets.ModelViewSet):
            serializer_class = PersonSerializer
            queryset = Person.objects.all()
    ```
 - In order to run the it apply migrations to make tables in db against models and runserver to test:
      ```
		python manage.py makemigrations
		python manage.py migrate
		python manage.py runserver
      ```
 -  Integrating Django Rest Swagger:
			In order to integrate django-rest-swagger, first install it through pip as:
    ```
      pip install django-rest-swagger==2.2.1
	  pip3 install packaging     
	  ```
  - Add it into the demo/settings.py as:
	```	
    INSTALLED_APPS = [
				...
				'rest_framework_swagger',
			]
    # Parser classes to help swagger, default ll be JSONParser only.
	REST_FRAMEWORK = {
		# Parser classes priority-wise for Swagger
		'DEFAULT_PARSER_CLASSES': [
			'rest_framework.parsers.FormParser',
			'rest_framework.parsers.MultiPartParser',
			'rest_framework.parsers.JSONParser',
		],
		'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
	}	  
	 ```	
 - Make swagger schema view in demo/urls.py and assign it a url as :
	```		
        from rest_framework_swagger.views import get_swagger_view
		schema_view = get_swagger_view(title='Demo Swagger API')
        urlpatterns = [
			url(r'^swagger/', schema_view),
		]
	 ```
 - python manage.py runserver
    * Your swagger should run at: http://127.0.0.1:8000/swagger/	 

 - if you will get an Error like this 
				```django_rest_swagger - 'staticfiles' is not a registered tag library. Must be one of:	```
      #### It's a bug in the developer's code, in 
    site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html

	The line with {% load staticfiles %} (line 1) should be {% load static %}. You can edit it manually.

   ### Output like this :
   ![N|Solid](https://github.com/rahulmoundekar/django_rest_curd_app_swagger/blob/master/swagger-ui.PNG)
