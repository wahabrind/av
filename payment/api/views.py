from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PaymentSerializer
from rest_framework import generics

class MakePayment(APIView):
    permission_classes  =[permissions.IsAuthenticated]
    
    def post(self, request):
        
        # fetching the post data
        product_id = request.POST.get('product_id','')
        mobile_no = request.POST.get('mobile_no','')
        user_id = request.POST.get('user_id','')
        operator_id = request.POST.get('operator_id','')

        #all the logic for payment  as it is not clear

        return Response({"message": "0-Transaction Successful",
            "status": 1,
            "transaction_vo": "null",
            "payment_log_vo": "null",
            "transaction_id": "xxxxx",
            "product_id": "1001",
            "user_id": "xxxxx",
            "msisdn": "301xxxxxxx",
            "operator_id": 100001
            })
         


# {
#  "product_id": 1001,
#  "mobile_no":"301xxxxxxx",
#  "user_id":"xxxxx",
#  "operator_id":100001
# }