from django.db import models
import datetime

class EntryManager(models.Manager):
    
    def get_entries_for_column(self, column, **kwargs):
        return self.get_entries(column=column, **kwargs)

    def get_entries_for_category(self, category, **kwargs):
        return self.get_entries(categories__in=[category], **kwargs)
    
    def get_entries(self, **kwargs):
        return self.filter(parent=None, published=True, pub_date__lte=datetime.datetime.now()).order_by("-pub_date").filter(**kwargs)
        