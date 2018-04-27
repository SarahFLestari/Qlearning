
import numpy as nmp
import math as mth
import random
from random import randint

file = open('DataTugasML3.txt')
R = [0]
Q = []
Reward = []

alfa = 1
gamma = 1

N = 10
E = 1
W = -1
S = -10

actionBawah = [N,E,W]
actionKiri = [N,E,S]
actionKanan = [N,W,S]
actionAtas = [E,W,S] 
action1 = [N,E]
action91 = [S,E]
action10 = [N,W]


with open('DataTugasML3.txt') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]

for i in range(len(x)) :
    R.append(x[i])

for i in range(len(x)) :
    Q.append([0,0,0,0])

print(R)
print(Q)

# state = randint(1,100)


def qMax(state):
	N = Q[state][0]
	E = Q[state][1]
	W = Q[state][2]
	S = Q[state][3]
	maks = [N,E,W,S]
	return max(maks)

def q(state,action):
	if (action == N):
		a = 0
	elif (action == E):
		a = 1
	elif (action == W):
		a = 2
	elif (action == S):
		a = 3	
	r = R[state+action]
	qSA = Q[state][a]
	newQsa = qSA + alfa * (r + gamma * qMax(state+action) - qSA)
	return newQsa

s = 1

# if (s == 1 ):
# 	a = random.choice(action1)
# elif (s == 91):
# 	a = random.choice(action91)
# elif (s == 10):
# 	a = random.choice(action10)
# elif (s > 1 and s < 10 ):
# 	a = random.choice(actionBawah)
# elif (s > 91 and s < 100):
# 	a = random.choice(actionAtas)
# elif (s % 11 == 0 ):
# 	a = random.choice(actionKiri)
# elif (s % 10 == 1):
# 	a = random.choice(actionKanan)

# if (a == N):
# 	a = 0
# elif (a == E):
# 	a = 1
# elif (a == W):
# 	a = 2
# elif (a == S):
# 	a = 3

# Q[s-1][a] = (q(s,a))

#Looping untuk satu episode :


while (s != 100):	
	if (s == 1 ):
		a = random.choice(action1)
	elif (s == 91):
		a = random.choice(action91)
	elif (s == 10):
		a = random.choice(action10)
	elif (s > 1 and s < 10 ):
		a = random.choice(actionBawah)
	elif (s > 91 and s < 100):
		a = random.choice(actionAtas)
	elif (s % 11 == 0 ):
		a = random.choice(actionKiri)
	elif (s % 10 == 1):
		a = random.choice(actionKanan)

	if (a == N):
		a = 0
	elif (a == E):
		a = 1
	elif (a == W):
		a = 2
	elif (a == S):
		a = 3
	Q[s-1][a] = (q(s,a))
	state = s+a

print(Q)
# print(sum(Reward))





	






















