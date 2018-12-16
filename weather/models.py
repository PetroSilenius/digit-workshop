from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def Meta(self):
        verbose_name_prular = 'cities'