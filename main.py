from flask import Flask, render_template
from tools.main import dateFinder

app = Flask(__name__)
app.register_blueprint(dateFinder, url_prefix="/tools")

@app.route('/')
def home():
   return '<h1>Welcome to the website</h1>'

if __name__ == '__main__':
	app.run(debug=True)

