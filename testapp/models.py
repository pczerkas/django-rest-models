#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals, print_function, absolute_import
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=135)
    code = models.CharField(max_length=3, primary_key=True)

    class APIMeta:
        pass


class Topping(models.Model):
    name = models.CharField(max_length=125)
    cost = models.FloatField()

    class APIMeta:
        pass


class Pizza(models.Model):

    name = models.CharField(max_length=125)
    price = models.FloatField()
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateTimeField()

    # creator is removed from hier but is in the serializer

    # creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    toppings = models.ManyToManyField(Topping, related_name='pizzas')
    menu = models.ForeignKey(Menu, null=True)

    # extra field from serializers
    cost = models.FloatField()

    class APIMeta:
        pass