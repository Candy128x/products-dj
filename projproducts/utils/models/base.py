from django.db import models


class Base(models.Model):
    created_by = models.CharField(default='system', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(default='system', max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusBase(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    DELETED_BY_OWNER = 2

    STATUS_CHOICES = [
        (INACTIVE, 'inactive'),
        (ACTIVE, 'active'),
        (DELETED_BY_OWNER, 'deleted_by_owner')
    ]

    status = models.PositiveIntegerField(default=ACTIVE, choices=STATUS_CHOICES)

    class Meta:
        abstract = True


class EntityTypeId(models.Model):
    entity_type = models.CharField(null=False, max_length=255)
    entity_id = models.PositiveIntegerField(null=False)

    class Meta:
        abstract = True