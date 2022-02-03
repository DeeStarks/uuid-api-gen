from django.db import models
import uuid

# Create your models here.
class UUID(models.Model):
    uuid = models.CharField(max_length=36, unique=True, default=uuid.uuid4().hex)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uuid