from bottle import get, run

##############################
@get("/")
def _():
  return "home"

##############################
@get("/items")
def _():
  return "items"


##############################

##############################
# 65535 
# 0 - 1024
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")








