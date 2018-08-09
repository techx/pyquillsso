"""Just a simple demo Flask app.
"""

from pyquillsso import QuillSSO
from flask import Flask, request
import json

app = Flask(__name__)
quill = QuillSSO(url="http://localhost:3000")


@app.route("/")
def index():
    return """
    <a href="{link}">Sign In With Quill</a>
    """.format(
        link=quill.get_signin_url(request.url_root + "login")
    )


@app.route("/login")
def login():
    token = request.args.get("token", "")
    try:
        user_info = quill.get_user(token)
        return "Success! %s" % json.dumps(user_info)
    except Exception as e:
        return "Error: %s" % str(e)


if __name__ == "__main__":
    app.run(port=5112, debug=True)
