from bottle import default_app, get, post, view, run, static_file

##############################
@get("/images/mitid.png")
def _():
  return static_file("mitid.png", root="./images")

##############################
@get("/")
@view("mitid")
def _():
  return

##############################
@post("/api-login")
def _():
  return "NO"


##############################
try:
  import production
  application = default_app()
except Exception as ex:
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
