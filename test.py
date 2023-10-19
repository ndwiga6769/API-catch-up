from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)#instance

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
app.app_context().push()

class TODO(db.Model):
    id = db.Column(db.Integer, primary_key = True, index = True)
    name = db.Column(db.String(32), nullable = False)
    description = db.Column(db.String(32), nullable = False)

db.create_all()

@app.route('/')
def welcome():
    return "welcome"

@app.route('/getToDo')
def getToDO():
    todo_list = []
    todo = TODO.query.all()
    for todo in todo:
        todoObj = {
            "id":todo.id,
            "name":todo.name,
            "description":todo.description
        }
        todo_list.append(todoObj)
    return todo
@app.route('/postTodo', methods=['POST'])
def addToDo():
    name = request.form['name']
    description = request.form['description']
    #add it to the table
    todo = TODO(name = name, description = description)
    db.session.add(todo)
    db.session.commit()
    return {
        "message": "added succesfully",
        "item": todo,
        "status":200
     }
if __name__ ==  "__main__":
    app.run(debug=True)