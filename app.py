from faker import Faker
fake = Faker()
import uuid
import sqlite3 

# print(fake.name()) # Dylan Garcia
# print(fake.first_name()) # Ronald
# print(fake.email()) # nancygarner@example.org

user = {
  "user_id" : str(uuid.uuid4()),
  "user_name" : fake.first_name(),
  "user_email" : fake.email()
}

try:
  db = sqlite3.connect("database.db")
  counter = db.execute("INSERT INTO users VALUES(:user_id, :user_name, :user_email)", user).rowcount
  if not counter: print("uppps...") 
  db.commit()
except Exception as ex:
  print(ex)  
finally:
  db.close()




