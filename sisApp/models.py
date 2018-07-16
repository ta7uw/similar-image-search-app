from django.db import models


class Item(models.Model):

    class Meta:
        db_table = "Item"

    name = models.CharField(verbose_name="name", max_length=128, null=False, blank=False)
    image = models.ImageField(verbose_name="image", upload_to="origin")

    def __str__(self):
        return self.name


class UploadedImage(models.Model):

    class Meta:
        db_table = "UploadedImage"

    image = models.ImageField(verbose_name="uploaded image", upload_to="uploaded")
