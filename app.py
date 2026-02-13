from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import psycopg2

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
POSTGRES_URL = os.environ['POSTGRES_URL']

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/create')
def create():
	try:
		con = psycopg2.connect(POSTGRES_URL, sslmode='require')
		cur = con.cursor()
		cur.execute(	"""	CREATE TABLE Users(
						Username VARCHAR(20) NOT NULL PRIMARY KEY,
						Password VARCHAR(20) NOT NULL
							  )
				""")
		con.commit()
		return 'CREATE'
	except Exception as e:
		return str(e)

@app.route('/insert')
def insert():
	try:
		con = psycopg2.connect(POSTGRES_URL, sslmode='require')
		cur = con.cursor()
		cur.execute("INSERT INTO users VALUES ('Bob', '123')")
		con.commit()
		return 'INSERT'
	except Exception as e:
		return str(e)

@app.route('/select')
def select():
	try:
		con = psycopg2.connect(POSTGRES_URL, sslmode='require')
		cur = con.cursor()
		cur.execute("SELECT * FROM users")
		rows = cur.fetchall()
		con.close()
		return str(rows)
	except Exception as e:
		return str(e)

@app.route('/login', methods=['POST'])
def login():
	try:
		username = request.form.get('uname')
		password = request.form.get('psw')
		
		con = psycopg2.connect(POSTGRES_URL, sslmode='require')
		cur = con.cursor()
		cur.execute("SELECT * FROM users WHERE Username = %s AND Password = %s", (username, password))
		user = cur.fetchone()
		con.close()
		
		if user:
			session['username'] = username
			return redirect(url_for('success'))
		else:
			flash('Invalid username or password')
			return redirect(url_for('home'))
	except Exception as e:
		return str(e)

@app.route('/success')
def success():
	if 'username' in session:
		return render_template('success.html', username=session['username'])
	else:
		return redirect(url_for('home'))

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('home'))

