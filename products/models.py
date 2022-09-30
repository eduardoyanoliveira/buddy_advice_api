from django.db import models


class ProductModel(models.Model):
    
    name = models.CharField(max_length=70, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)