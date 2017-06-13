from django.conf import settings
from django.core import validators
from django.db import models


class ListNames(models.Model):
    name = models.CharField(
    	max_length=50,
    	validators=[validators.MinLengthValidator(2)],
    	unique=True
    	)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']

