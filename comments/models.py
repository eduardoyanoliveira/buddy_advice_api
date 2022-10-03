from django.db import models
from products.models import ProductModel
from users.models import CustomUser


class CommentModel(models.Model):
    
    text = models.TextField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
