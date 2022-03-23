import uuid
import base64
import sqlite3

with open("file_one") as file:
  data = file.read()
  lines = data.split("\n")
  message = lines[-1] # Line with the strange symbols

  message = message.encode()
  message = base64.b64encode(message)
  # message = base64.b64decode(message).decode()
  # message = message.encode()
  # message = base64.b64encode(message) # b'w6/Cv8K9PcOvwr/CvQM='
  # message = message.decode('utf-8')
  message = base64.b64decode(message).decode()

  db = sqlite3.connect("data.db")
  db.execute("INSERT INTO messages VALUES(?,?)", (str(uuid.uuid4()), message))
  db.commit()
  print(message)
  





