from django.db import models

class Todo_Item(models.Model):
    todo = models.CharField(max_length=200)

    def __str__(self):
        return self.title

