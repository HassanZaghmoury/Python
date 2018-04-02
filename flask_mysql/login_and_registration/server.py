from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'mydb')
@app.route('/')
def index():
    query = "SELECT * FROM users"                           # define your query
    users = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_users=users) # pass data to our template
# @app.route('/users/<users_id>')
# def show(users_id):
#     query = "SELECT * FROM users WHERE id = :specific_id"
#     data = {'specific_id': users_id}
#     users = mysql.query_db(query, data)
#     return render_template('index.html', one_user=users[0])
@app.route('/users', methods=['POST'])
def create():
    # error = []
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    passwordcon = request.form['password_confirmation']
    
    if not EMAIL_REGEX.match(request.form['email']):
        flash('enter vaild email')
    if len(email) < 1:
        flash('please enter email')
    if len(firstname) < 2:
        flash('enter vaild first name')
    if len(lastname) < 2:
        flash('enter vaild last name')
    if len(password) < 7:
        flash('password must have at least 8 characters')
    if passwordcon != password:
        flash('passwords must match')
        
    else:
        query = "INSERT INTO users (first_name, last_name, email, password) values(:first_name, :last_name, :email, :password)"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email'],
                 'password': request.form['password']

                }
        mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('/success.html')
@app.route('/login', methods=['POST'])
def login():
    print ('got to route')
    query = "select * from users where email = :email and password = :password"
    data = {
                 'email': request.form['email'],
                 'password': request.form['password']

                }
    mysql.query_db(query, data)
    email1=  mysql.query_db(query, data)
    if len(email1) == 0:
        flash("no email found")
    if len(request.form['password']) == 0: 
        flash("wrong password")
        return redirect('/')    
    else:
        return redirect('/success')

app.run(debug=True)
