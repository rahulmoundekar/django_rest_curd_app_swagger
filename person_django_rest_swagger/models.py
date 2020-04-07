from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=45)
    mobile = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "person"
