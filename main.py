from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form, method='POST'>
      <input id="rotate by" type="text" name="rot" />
      <br>
      <textarea name="text"></textarea>
      <br>
      <input type="submit" />
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route('/')
def encrypt():
  text = request.format['text']
  rot = request.format['rot']
  return rotate_string(text, rot)

if __name__=="__main__":
   app.run()