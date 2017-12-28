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
import datetime

admin="admin"
password="admin"
email="admin@localehost"
currtime=datetime.datetime.now().strftime("%d-%m-%Y")

flist=['test.log','test.db']

for f in flist:
	if os.path.isfile(f):
		os.remove(f)

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

db.create_all()
u= User(username=admin, password=password, email=email)
u.role=Role(name=admin,birthday=currtime)
db.session.add(u)
db.session.commit()


#User.query.filter(Role.id == 4, User.id == current_user.team_id).all()
#User.query.filter(Role.id == 4, User.id == current_user._id).all()
