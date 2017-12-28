from flasksql_modle import db
from flasksql_modle import User, Role
from flasksql_modle import app
from flask import render_template

import string
import random
import logging
import os

from datetime import datetime, timedelta

import json



'''
u1= Role.query.filter_by(name='admin').first()
print(u1)
u1dic=u1.__dict__
u1dic.pop('_sa_instance_state')
u1dic.pop('id')
#print(u1.id)
print(u1dic)
#print(type(u1dic))
json_str = json.dumps(u1dic)
print(json_str)

print(u1.name)
print(u1.phone)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
'''

roles=Role.query.all()
for item in roles:
	data=item.__dict__
	data.pop('_sa_instance_state')
	d=json.dumps(data)
	print(d)
	print(item.name)
	print(item.phone)
'''
r=Role.query.filter_by(phone='0961399930').first()
print(r)
'''
