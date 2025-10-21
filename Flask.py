import flask

app = flask.Flask("Webby_wabbo")

@app.route("/Webby_wabbo")
def index():
    with open(r"C:\Users\alumno\Documents\Programacion\index.html", "r") as Html:
        MainPage = Html.read()

    return MainPage

app.run()