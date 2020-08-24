from flask import Flask

from flask import render_template

application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html")



# EB looks for an 'application' callable by default.



# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
