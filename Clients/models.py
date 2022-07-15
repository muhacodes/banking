from django.db import models

# Create your models here.

class Client(models.Model):
    first_name                          = models.CharField(max_length=100)
    last_name                           = models.CharField(max_length=100)
    email                               = models.CharField(max_length=500, null=True, blank=True)
    company                             = models.CharField(max_length=500, null=True, blank=True)
    address                             = models.CharField(max_length=500, null=True, blank=True)
    currency                            = models.CharField(choices=(('UGX', 'UGX'), ('Dollar', 'Dollar')), null=True, max_length=10)
    telephone                           = models.CharField(max_length=10)
    amount                              = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency                            = models.CharField(choices=(('UGX', 'UGX'), ('Dollar', 'Dollar')), null=True, max_length=10, default='UGX')
    photo                               = models.ImageField(upload_to="uploads/clients/", null=True, blank=True)

    def __str__(self):
        return self.last_name

