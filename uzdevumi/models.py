from django.db import models


class User(models.Model):

        username = models.CharField(max_length=100)
        e_mail = models.EmailField(max_length=100)




