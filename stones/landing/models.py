from django.db import models


class Header(models.Model):
    line1 = models.CharField(max_length=250)
    subline = models.CharField(max_length=250)


class Service(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to="images/services", default=None)


class Material(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/materials", default=None)


class Navigation(models.Model):
    block1 = models.CharField(max_length=250)
    block2 = models.CharField(max_length=250)
    block3 = models.CharField(max_length=250)


class Contact(models.Model):
    phone_number = models.CharField(max_length=11)
    button_text = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)


class Footer(models.Model):
    phone_number = models.CharField(max_length=11, default=None)
    text = models.CharField(max_length=250, default=None)
    address = models.CharField(max_length=250, default=None)
    email = models.CharField(max_length=250, default=None)
