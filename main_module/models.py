from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["-name"]
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Language")
        verbose_name_plural = ("Languages")

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="image", null=False)
    main_image = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-category"]

    def __str__(self):
        return self.name
