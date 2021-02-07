from django.db import models
from django.contrib.auth.models import User


# creting model for paymenet 

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True , null=True)
    status = models.IntegerField(  blank=True , null=True)
    transaction_vo = models.TextField( blank=True , null=True)
    payment_log_vo = models.TextField( blank=True , null=True)
    transaction_id = models.TextField( blank=True , null=True)
    msisdn = models.TextField( blank=True , null=True)
    operator_id = models.TextField( blank=True , null=True)
    