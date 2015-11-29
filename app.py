from flask import Flask,redirect,url_for,request,render_template
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient()
db = client.tododb



@app.route('/')
def todo():
    _items = db.tododb.find()
    item = [i for i in _items]
    return render_template('todo.html',item=item)

@app.route('/new',methods=['POST'])
def new():
    print('We have reachd')
    item_doc = {
        'name': request.form['name'],
        'Description' : request.form['descp']
    }
    db.tododb.insert_one(item_doc)
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
