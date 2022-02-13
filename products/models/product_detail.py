from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class ProductDetail(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)
    description = models.TextField(null=True, blank=True, max_length=2048)
    price = models.PositiveIntegerField(null=False, blank=False)
    category = models.PositiveIntegerField(null=True, blank=True)
    available_quantity = models.PositiveSmallIntegerField(null=False, blank=False)

    class Meta:
        db_table = 'product_details'
        ordering = ['-id']

    def __str__(self):
        return self.name