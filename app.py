from flask import Flask
from flask import render_template

app= Flask(__name__)
@app.route('/')
def url_principal():
	return render_template("index.html")

@app.route("/contact")
def url_contact():
	return render_template("contact.html")

if __name__ == "__main__":
	app.run(debug=True)