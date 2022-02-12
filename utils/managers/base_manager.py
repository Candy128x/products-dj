from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class BaseManager(models.Manager):

    @classmethod
    def get_or_none(classmodel, **kwargs):
        try:
            return classmodel.objects.get(**kwargs)
        except classmodel.DoesNotExist:
            return None
