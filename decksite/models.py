from django.db import models
from .storage import OverwriteStorage

# Create your models here.

class Project(models.Model):
    projectName = models.CharField(max_length=200)
    projectPrice = models.IntegerField()
    projectDescription = models.TextField()

    projectID = models.AutoField(primary_key = True)
    date_added = models.DateTimeField(auto_now_add=True)

    projectThumb = models.FileField(blank=True, null=True, storage=OverwriteStorage())

    def __str__(self):
        return self.projectName