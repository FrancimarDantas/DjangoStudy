from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Postagem(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    created_in = models.DateTimeField(auto_now_add=True)
    autho = models.ForeignKey(User,models.CASCADE)

    class Meta:
        ordering = ["-created_in"]
        verbose_name_plural = "Postagens"

    def __str__(self):
        return f"titulo: {self.title}\nautor: {self.autho}\npublicado em: {self.created_in}"

