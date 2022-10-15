from django.db import models

class productModel(models.Model):
    pname = models.CharField(max_length=30 ,null=False)
    pprice = models.IntegerField(null=False)
    pimage = models.CharField(max_length=40, null=False)
    pdescription = models.TextField(null=False)
