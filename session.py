from flask import Flask,render_template,request
#from flask session import Session
app = Flask(__name__)
#app.config["SESSION_PERMANANT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#session(app)
notes = [] 
@app.route('/', methods=["POST","GET"])
def index():
	if request.method == "POST":
		note = request.form.get("note");
		notes.append(note)

	return render_template("index.html" , notes=notes)