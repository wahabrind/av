import requests
import os

# url='http://127.0.0.1:8000/status/'
auth_url='http://127.0.0.1:8000/auth/jwt/'
# auth_refresh_url='http://127.0.0.1:8000/status/auth/jwt/refresh'

# with open(os.path.join(os.getcwd(),'Screenshot.png'),'rb') as img:
#     r=requests.request('POST',url, data={'user':1, 'content':'asdasd'},files={'image':img})

auth_data={
    'username':'wahab',
    'password':'wahab'
}

r=requests.post(auth_url,auth_data)
token=r.json()
print(token)


# headers={
#     'Authorization':'JWT '+token,
# }
# r1=requests.get(url , headers=headers)
# print(r1.json())


# refresh_data={
#     'token':token
# }
# rr=requests.post(auth_refresh_url,refresh_data)

# print(rr.text)

# print(r.json())

# print(r.text)
# print(r.status_code)