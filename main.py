from flask import Flask, render_template,session,redirect,url_for,request
from config import *


app = Flask(__name__)
app.config.from_object(todo)#importamos la configuracion de config.py

@app.errorhandler(404)
def not_found(error):
	return 'no exixte la pagina'

@app.route(r'/', methods=['GET','POST'])
def init():
	return 'Hola Mundo'

@app.route(r'/vista1')
@app.route(r'/vista1/<nombre>')
@app.route(r'/vista1/<nombre>/<int:edad>')
def vista1(nombre="Erick",edad='21'):
	session['username']=nombre
	return 'Hola {}, tu edad es {}'.format(nombre,edad)	

@app.route(r'/vista2')
def vista2():
	if 'username' in session:
		session.pop('username')
	return render_template('base.html')	

@app.route(r'/vista3')
def vista3():
	return render_template('index.html')	


@app.route(r'/vista4')
def vista4():
	return '{}'.format(session['username'])	

@app.before_request#todo lo que quieras que se ejecute al inicio
def before_request():
	if 'username' not in session and request.endpoint in ['vista3']:
		return redirect(url_for('vista1'))

"""
@app.after_request
def after_request(request):
	return request	
"""

if __name__ == '__main__':
	app.run('127.0.0.1', port=8080,debug=True)	