fname = input('Enter File: ')
if len(fname) < 1 : fname = 'hitungkata.txt'
hand = open(fname)

di =  dict()
for lin in hand:
	lin = lin.rstrip()
	wds = lin.split()
	for w in wds:
		print(w)
		di[w] =  di.get(w,0) + 1

#temukan kata
largest = -1
theword = None
for k,v in di.items() :
	print(k,v)
	if v > largest :
		largest = v
		theword = k
print('Selesai',theword,largest)