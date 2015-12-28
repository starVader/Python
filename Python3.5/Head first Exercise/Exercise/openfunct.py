def fileopen(filename,mode,listname):
	try:
		with open(filename,mode) as ff:
			data = ff.readline()
		listname = data.strip().split()
	except IOError as io:
		print("File error:" + str(io))
		return(None)
		

