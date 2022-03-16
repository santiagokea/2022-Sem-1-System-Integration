import requests
from get_name import name
from get_last_name import last_name
from get_email import email
from get_phone import mobile
from get_api_key import api_key

message = f"Hi {name} {last_name}, your email is {email}"
payload = {"to_phone": mobile, "message": message, "api_key":api_key}
r = requests.post("https://fatsms.com/send-sms", data=payload)
print("response status code:", r.status_code)
print("response:", r.text)
print(message)




