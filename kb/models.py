from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class TrainingManuals(models.Model):
    tmName = models.CharField(max_length=200)
    tmContent = RichTextUploadingField
