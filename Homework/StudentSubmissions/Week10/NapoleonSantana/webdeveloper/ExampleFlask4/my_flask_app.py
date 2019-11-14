from flask import Flask
from flask import render_template
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '/home/webdeveloper/sites/SedJedi/4/build/')
app = Flask(__name__, template_folder=template_path)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('index.html')

# run the application
if __name__ == "__main__":
    app.run(debug=True)

