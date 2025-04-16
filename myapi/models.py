from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)      
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
