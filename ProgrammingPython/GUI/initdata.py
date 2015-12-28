#! /usr/bin/python3
#init data
#records
import pickle

bob = {'name':'Bob smith','age':42,'pay':30000,'job':'dev'}
sue = {'name':'Sue jones','age':45,'pay':40000,'job':'hdw'}
tom = {'name':'Tom','age':50,'pay':0000,'job':'None'}

db ={}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


try:
	with open('pickleddata.pickle','wb') as pick:
		pickle.dump(db,pick)
except IOError as ioerr:
	print("File read :" +str(ioerr))
