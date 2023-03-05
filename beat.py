def beat_list(x):
    a=[]
    for i in range(2**x):
        a.append('{:b}'.format(i).zfill(x))
    return a
def phase_equality(x,a):
    for i in a:
        if x in 2*i:return True
    return False
def phase_compress(x):
    a=[]
    for i in x:
        if not phase_equality(i,a):a.append(i)
    return a

def f(x):return phase_compress(beat_list(x))

def add(x,y):
	a=[int(i) for i in list(x)]
	b=[int(i) for i in list(y)]
	return [sum(i) for i in zip(a,b)]

#for x in range(64):
#    print(len(phase_compress(beat_list(x))))

'''
def f(x):
    s=0
    for i in range(1,x+1):
        if x%i==0:s+=i
    return s/x

for i in range(1,64):
    print(f(i))
'''
