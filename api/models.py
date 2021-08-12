from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Location(MPTTModel):
    text = models.CharField(max_length=127)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    code = models.CharField(max_length=3, default='', blank=True)

    class MPTTMeta:
        order_insertion_by = ['text']

    def __str__(self):
        return self.text

    class Admin:
        list_display = ('parent', 'text')
        list_filter = ('level',)
        search_fields = ('text__icontains', 'parent__text__icontains')
        ordering = ['-text']
