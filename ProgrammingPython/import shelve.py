import shelve

bob = {'name':'Bob Smith','age': 42,'sal': 30000, 'job':'software'}
sue = {'name':'Sue Jones','age':45,'sal': 40000, 'job':'hardware'}
tom = {'name':'Tom Doe','age' :50, 'sal':50000,'job':'manager'}
db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()