from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route( "/" )
@app.route( "/home" )
def go_home():
    if "num_of_visits" in session:
        session["num_of_visits"] += 1
    else:
        session["num_of_visits"] = 1
    return render_template( "index.html" )

@app.route( "/destroy_session" )
def destroy_session():
    session.clear()
    return redirect( "/home" )


if __name__ == "__main__":
    app.run(debug = True)