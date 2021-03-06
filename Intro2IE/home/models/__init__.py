from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Item(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.TextField(_('description'), max_length=500, blank=True)
    picture = models.ImageField(blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Record(models.Model):
    item_name = models.CharField(_('item_name'), max_length=30)
    alter = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)