from django.db import models as m

class Product(m.Model):
    name = m.CharField(max_length=100)
    def __str__(self):
        return self.name

