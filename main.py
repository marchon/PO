from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():     
	
    return "Login - redirect to view main"     

@app.route("/new/po_number")
def new():
	return "Create a new PO"        
	
@app.route("/view/po_number")
def view():
	return "View a PO number"      




if __name__ == "__main__":
    app.run()