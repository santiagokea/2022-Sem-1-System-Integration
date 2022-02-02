from bottle import run, error, get

##############################
@get("/")
def _():
  return "My first micro service"

##############################
@error(404)
def _(error):
  print(type(error)) # terminal only... for the developer
  print(dir(error))
  return "Uppps... page not found"



##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)


