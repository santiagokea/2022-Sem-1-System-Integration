from bottle import get, post, request, response, run
import json
import uuid

items = [
  {"id":"5cee299b-6630-4aec-a7cc-f69947a64908", "name":"a"}
]


##############################
@get("/")
def _():
  return "home"

##############################
@get("/items")
def _():
  response.content_type = "application/json"
  return json.dumps(items)


##############################
@post("/items")
def _():
  item_id = str(uuid.uuid4())
  item_name = request.json.get("name")
  print( type(item_id) )
  return item_name



##############################
# 65535 
# 0 - 1024
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")








