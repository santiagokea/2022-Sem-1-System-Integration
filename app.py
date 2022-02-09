from bottle import delete, error, get, hook, post, request, response, run
import json
import uuid

items = [
  {"id":"5cee299b-6630-4aec-a7cc-f69947a64908", "name":"a"}
]

##############################
@hook("after_request")
def _():
  response.content_type = "application/json"

##############################
@get("/")
def _():
  response.status = 204
  return "home"

##############################
@get("/items")
def _():
  return json.dumps(items)


##############################
@post("/items")
def _():
  item_id = str(uuid.uuid4())
  item_name = request.json.get("name")
  item = {"id":item_id, "name":item_name}
  items.append(item)
  print( type(item_id) )
  response.status = 201
  return {"id":item_id}

##############################
@delete("/items/<item_id>")
def _(item_id):
  for index, item in enumerate(items):
    if item["id"] == item_id:
      items.pop(index)
      return {"info":"item deleted"}

  response.status = 204
  return 
  # What? This is not displayed in the client... mmmm....
  # return json.dumps({"info":f"item with id {item_id} not found"})




##############################
@error(404)
def _(error):
  response.content_type = "application/json"
  return json.dumps({"info":"page not found"})



##############################
# 65535 
# 0 - 1024
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")








