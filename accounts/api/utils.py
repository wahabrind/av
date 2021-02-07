import datetime


#setting custom response for jwt token
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'message': "Login successfully",
        'status':1,
        'token': token,
           }