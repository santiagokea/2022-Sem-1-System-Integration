# pip install pyjwt
import jwt
import time

cpr = "12345"
iat = int(time.time())
exp = iat + 600

encoded_jwt = jwt.encode({"cpr":cpr, "iat":iat, "exp":exp}, "secret", algorithm="HS256")
print(encoded_jwt)


