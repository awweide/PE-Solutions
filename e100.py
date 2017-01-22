#git
lim = 1000000000
sqrt = 3+2*(2**0.5)

def calc(x,y):
	return y*(y+1.0) / (x * (x+1) )

i = 1000000000000	
while True:
	j = int(sqrt*i)
	while calc(i,j) < 2: j+=1
	if calc(i,j) == 2: break
	i += 1

print i+1,j+1

