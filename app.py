from flask import Flask, render_template,request,redirect, url_for
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/routes")
def routes():
    return render_template("bus_route_page.html")

@app.route("/R1")
def route1():
    return render_template("bus_route_page1.html")

@app.route("/R2")
def route2():
    return render_template("bus_route_page2.html")

@app.route("/search")
def search():
    query = request.args.get("query")
    if query == "R1":
        return redirect(url_for("/R1"))
    elif query == "R2":
        return redirect("/R2")
    else:
        return "No route found", 404


if __name__=='__main__': 
    app.run(debug=True)