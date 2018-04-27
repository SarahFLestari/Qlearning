
import numpy as nmp
import math as mth
import random
from random import randint

file = open('DataTugasML3.txt')
R = [0]
Q = []


alfa = 1
gamma = 1

N = 10
E = 1
W = -1
S = -10

allAction = [N,E,W,S]
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
	action = []
	if (state == 1 ):
		action = action1
		forMax = [Q[state-1][0],Q[state-1][1]]
	elif (state == 91):
		action = action91
		forMax = [Q[state-1][1],Q[state-1][3]]
	elif (state == 10):
		action = action10
		forMax = [Q[state-1][0],Q[state-1][2]]
	elif (state > 1 and state < 10 ):
		action = actionBawah
		forMax = [Q[state-1][0],Q[state-1][1],Q[state-1][2]]
	elif (state > 91 and state < 100):
		action = actionAtas
		forMax = [Q[state-1][1],Q[state-1][2],Q[state-1][3]]
	elif (state % 11 == 0 ):
		action = actionKiri
		forMax = [Q[state-1][0],Q[state-1][1],Q[state-1][3]]
	elif (state % 10 == 1):
		action = actionKanan
		forMax = [Q[state-1][0],Q[state-1][2],Q[state-1][3]]
	else :
		action = allAction
		forMax = [Q[state-1][0],Q[state-1][1],Q[state-1][2],Q[state-1][3]]

	return max(forMax)

def q(state,a):
	if (a == 0):
		action = N
	elif (a == 1):
		action = E
	elif (a == 2):
		action = W
	elif (a == 3):
		action = S
	# print(action, qMax(state+action))
	r = R[state+action]
	qSA = Q[state][a]
	newQsa = qSA + alfa * (r + gamma * qMax(state+action) - qSA)

	return newQsa


n = 10
for i in range(0,n):
	#Looping untuk satu episode :
	print("Episode ", i)
	s = 1
	while (s != 100):
		print("Current State",s)
		if (s == 1 ):
			act = random.choice(action1)
		elif (s == 91):
			act = random.choice(action91)
		elif (s == 10):
			act = random.choice(action10)
		# elif(s == 100):
		# 	break
		elif (s > 1 and s < 10 ):
			act = random.choice(actionBawah)
		elif (s > 91 and s < 100):
			act = random.choice(actionAtas)
		elif (s % 10 == 1 ):
			act = random.choice(actionKiri)
		elif (s % 10 == 0):
			act = random.choice(actionKanan)
		else :
			act = random.choice(allAction)

		if (act == N):
			a = 0
		elif (act == E):
			a = 1
		elif (act == W):
			a = 2
		elif (act == S):
			a = 3
		Q[s-1][a] = (q(s,a))
		s = s+act
		print("Next STATE", s)
		print(Q)

bestAction = []

for i in range(len(Q)):
	bestAction.append(Q[i].index(max(Q[i])))

print(bestAction)























