from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=[
            'user',
            'message',
            'status',
            'transaction_vo',
            'payment_log_vo',
            'transaction_id',
            'msisdn',
            'operator_id',
        ]
        read_only_fields=['user']


    def validate(self,data):
        #getting data and validating it
        user= data.get('user',None)
        message= data.get('message',None)
        status= data.get('status',None)
        transaction_vo= data.get('transaction_vo',None)
        payment_log_vo= data.get('payment_log_vo',None)
        transaction_id= data.get('transaction_id',None)
        msisdn= data.get('msisdn',None)
        operator_id= data.get('operator_id',None)

        if user =="" or message =="" or status =="" or transaction_vo=="" or payment_log_vo=="" or transaction_id==""  or msisdn=="" or operator_id=="":
            raise serializers.ValidationError('data cannot be empty')
        return data
