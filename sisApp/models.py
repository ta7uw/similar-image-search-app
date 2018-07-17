from django.db import models
from uuid import uuid4
import os

from settings import settings


class Item(models.Model):
    class Meta:
        db_table = "Item"

    name = models.CharField(verbose_name="name", max_length=128, null=False, blank=False)
    image = models.ImageField(verbose_name="image", upload_to="origin")

    def __str__(self):
        return self.name

    def get_image_path(self, filename):
        """
        To Get new customized file path
        :param filename: original file name
        :return: customized file name
        """
        prefix = "images/"
        file_type = "origin/"
        name = str(uuid4()).replace("-", "")
        extension = os.path.splitext(filename)[-1]
        return prefix + file_type + name + extension


class UploadedImage(models.Model):

    class Meta:
        db_table = "UploadedImage"

    image = models.ImageField(verbose_name="uploaded image", upload_to="uploaded")

    def delete_previous_file(function):
        """
        :param function: main function
        :return: wrapper
        """

        def wrapper(*args, **kwargs):
            """

            :param args:
            :param kwargs:
            :return: result of main function
            """
            self = args[0]
            result = UploadedImage.objects.filter(pk=self.pk)
            previous = result[0] if len(result) else None
            super(UploadedImage, self).save()

            result = function(*args, **args)

            if previous:
                os.remove(settings.MEDIA_ROOT + "/uploaded/" + previous.image.name)
            return result

        return wrapper

    @delete_previous_file
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(UploadedImage, self).save()

    @delete_previous_file
    def delete(self, using=None, keep_parents=False):
        super(UploadedImage, self).delete()

    def get_image_path(self, filename):
        """
        To Get new customized file path
        :param filename: original file name
        :return: customized file name
        """
        prefix = "images/"
        file_type = "uploaded/"
        name = str(uuid4()).replace("-", "")
        extension = os.path.splitext(filename)[-1]
        return prefix + file_type + name + extension


