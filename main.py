from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
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
     <form class="cipher-form" action ="/" method="POST">
                   <textarea name="text" placeholder="Enter Message to Encrypt:">{0}</textarea>
                   <label for "rot">Enter Amount to Rotate:</label>
                   <input type="text" id="rot" name="rot" value="0">
                   <input type="submit" value="Encrypt">
               </form>
    
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route('/', methods=['POST'])
def encrypt():
  text = str(request.form['text'])
  rot = int(request.form['rot'])
  encrypted = rotate_string(text,rot)
  return form.format(encrypted)
  
app.run()