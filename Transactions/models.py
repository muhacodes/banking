from django.db import models
from Clients.models import Client

# Create your models here.

class Transaction(models.Model):
    client                                      = models.ForeignKey(Client, on_delete=models.CASCADE)
    mode                                        = models.CharField(choices=(('deposit', 'deposit'), ('withdraw', 'withdraw')), max_length=10)
    amount                                      = models.DecimalField(max_digits=10, decimal_places=2)
    reason                                      = models.CharField(max_length=500, blank=True, null=True)
    balance                                     = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description                                 = models.CharField(max_length=1000, null=True, blank=True)
    created_at                                  = models.DateTimeField(auto_now=True,)
    updated_at                                  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.last_name
    