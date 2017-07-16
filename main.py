from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body, html{{
                font-size: 1rem;
                line-height: 1.5;
                font-family: sans-serif;
                width: 100vw;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
        <label>
            Rotate By: 
            <input type="number" name="rot" value="{0}">
        </label>
        <textarea name="text">{1}</textarea>
        <input type="submit" value="Submit Query">
      </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format(0, "")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_string = rotate_string(text, rot)
    return form.format(rot, encrypted_string)

app.run()