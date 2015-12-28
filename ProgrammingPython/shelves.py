from initdata import bob, sue, tom

import shelve

db = shelve.open('pickleddata')
bob = db['bob'] 
tom = db['tom']
sue = db['sue']

db.close()