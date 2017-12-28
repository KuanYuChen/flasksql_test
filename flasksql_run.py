from flasksql_modle import db
from flasksql_modle import User, Role
from flasksql_modle import app
from flask import render_template, jsonify, request

import json

#User.query.filter(Role.id == 4, User.id == current_user.team_id).all()
#User.query.filter(Role.id == 4, User.id == current_user._id).all()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login')
def login(): 
	pass

# query by username
@app.route('/role/<username>',methods=['GET','DELETE'])
def role_username(username):
	r= Role.query.filter_by(name=username).first()
	if r  is None:
		return jsonify({"status":username+" Not Found"}),400
	
	if request.method == 'GET' :		
		data=r.__dict__
		data.pop('_sa_instance_state')
		#data_json = json.dumps(data)
		#print(data_json)
		return jsonify(data),200

	if request.method == 'DELETE' :
		print("DEL!!!!!!!!!!!!")
		u=User.query.filter_by(username=r.name).first()
		db.session.delete(r)
		db.session.delete(u)
		db.session.commit()
		return jsonify({"status":"success "}),200	


def role_query_phone(phone):
	u= Role.query.filter_by(cellphone=phone).first()
	if u  is None:
		u= Role.query.filter_by(phone=phone).first()
	return u	

# query by phone
@app.route('/role/<int:phone>',methods=['GET','DELETE'])
def role_phone(phone):

	r=role_query_phone(phone)
	if r is None:
		return jsonify({"status":username+" Not Found"}),400
	if request.method == 'GET' :		
		data=r.__dict__
		data.pop('_sa_instance_state')
		#data_json = json.dumps(data)
		#print(data_json)
		return jsonify(data),200
	if request.method == 'DELETE' :
		print("DEL!!!!!!!!!!!!")
		u=User.query.filter_by(username=r.name).first()
		db.session.delete(r)
		db.session.delete(u)
		db.session.commit()
		return jsonify({"status":"success "}),200			


def role_add(request):
    role = request.json
	#u= User(username=name,password=name, email=name+'@example.com')
	# relationship
	#u.role=Role(name=name,birthday=birthday)
	#u.role.phone=item['phone']
	    
    if "name" in role:
        name=role["name"]
       	print("name: "+role["name"]+"Find")
       	u=User.query.filter_by(username=name).first()
       	if u:
       		return 0
    else:   	
        return 0
    if "password" in role:
       	password=role["password"]
    else :
        password="99999999"

    if "email" in role:
        email=role["email"]
    else :
    	return 0

    u=User(username=name,password=password,email=email)
    u.role=Role(name=name)
    db.session.add(u)

    if "gender" in role:
        gender=role["gender"]
        u.role.gender=gender


    if "phone" in role:
        phone=role["phone"]
        u.role.phone=phone



    db.session.commit()

    return 1     
    

@app.route('/role',methods=['POST','GET'])
def role():
	if request.method == 'POST' :
		print(request.json)
		if not request.json :
			return jsonify({"status":"fail","message":"post json error"}),400	  
		else :
			if role_add(request) == 1 :
				return jsonify({"status":"success "}),200			
			else :
				return jsonify({"status":"fail","message":"ooxxzz"}),400
	if request.method == 'GET' :
		roles=Role.query.all()
		r=[]
		print(type(roles))
		for item in roles:
		 	data=item.__dict__
		 	data.pop('_sa_instance_state')
		 	r.append(data)
		print(type(r))
		return jsonify(r),200
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
'''

app.run(host='0.0.0.0',port=9908)

