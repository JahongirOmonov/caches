from django.db import models
from utils.models import BaseModel
# Create your models here.


class Book(BaseModel):
    title = models.CharField(max_length=31)
    page = models.PositiveIntegerField()

    def __str__(self):
        return self.title
