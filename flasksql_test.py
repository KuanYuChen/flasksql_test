from flasksql_modle import db
from flasksql_modle import User, Role
from flasksql_modle import app
from flask import render_template

import string
import random
from datetime import datetime, timedelta
def gen_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

import logging
import os

SIZE=10

flist=['test.log','test.db']

for f in flist:
	if os.path.isfile(f):
		os.remove(f)

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

ll=[]
#admin
d={}
d["name"]='admin'
d["date"]=gen_datetime().strftime("%d-%m-%Y")
d["phone"]="0961399930"
ll.append(d)

for x in range(SIZE):
	d={}
	d["name"]=gen_string()
	d["date"]=gen_datetime().strftime("%d-%m-%Y")
	d["phone"]=gen_string(10, string.digits)
	ll.append(d) 
    
print(ll)


db.create_all()

for item in ll:
	logging.debug("A")
	name=item['name']
	birthday=item['date']
	u= User(username=name,password=name, email=name+'@example.com')
	# relationship
	u.role=Role(name=name,birthday=birthday)
	u.role.phone=item['phone']
	db.session.add(u)

'''
logging.debug("G")
guest = User(username='guest', email='guest@example.com')
db.session.add(guest)
'''
logging.debug("----")
db.session.commit()


#User.query.filter(Role.id == 4, User.id == current_user.team_id).all()
#User.query.filter(Role.id == 4, User.id == current_user._id).all()

item=ll[4]
name=item['name']
print(name)
u1 = User.query.filter_by(username=name).first()
print(u1)
print(u1.role)
print(u1.role.name)
print(u1.role.name)

u2= Role.query.filter_by(name=name).first()
print(u2)
print(u2.name)


# u1=User(username='sean',email="")
# r1=Role(name='sean')
# u1.role=r1
# db.session.add(u1)
# db.session.commit()