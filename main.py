from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():     
    return render_template('index.html')

@app.route('/logon', methods=['POST', 'GET'])
def logon():
	values = [request.logon['username'], request.logon['password']]
	return render_template('logon.html', values=values) 



@app.route('/new/')
def new():
	return "Create a new PO"        
	
@app.route('/view/<int:po_number>')
def view(po_number):
	return render_template('view.html', po_number=po_number)






if __name__ == "__main__":
    app.run()