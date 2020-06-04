
import math
import random
import copy


#Algoritmo de Backtraking del pdf semana 4

def queens(A,m,x):
	if m==0:
		print(A)
	else:
		for i in range(m,0,-1):
			if(b[A[i]+m] and  d[(A[i]-m)+x]):
				b[A[i]+m]=False
				d[(A[i]-m)+x]=False
				swap(A, m, i)
				queens(A, m-1, x)
				swap(A, m, i)
				b[A[i]+m]=True
				d[(A[i]-m)+x]=True






#Algoritmo de backtracking que retorna solo la solucion mas eficiente







def queensFastBT(A,m,x,b,d):
	if m==0:
		return True
	else:
		for i in range(m,0,-1):

			if(b[A[i]+m] and  d[(A[i]-m)+x]):
				b[A[i]+m]=False
				d[(A[i]-m)+x]=False
				swap(A, m, i)
				if(queensFastBT(A, m-1, x,b,d)):
					return A
				swap(A, m, i)
				b[A[i]+m]=True
				d[(A[i]-m)+x]=True






#N=4
#b = ((2*N)+1) * [True]
#d = ((2*N)-1) * [True]


#Algoritmo Proabbilistico de la tarea selecciona la posicion a probar en un random en vez de  hacerlo incrementando el iterador

def queensProb(A,m,x,b,d):
	#print(A)
	if m==0:
		#print("akjfbkjdsabkjb")
		return True
	else:
		arr=[]
		for i in range(m):
			arr+=[i+1]
		for i in range(m):
			ran = random.choice(arr)
			#print(ran)
			arr.remove(ran)

			if(b[A[ran]+m] and  d[(A[ran]-m)+x]):
				b[A[ran]+m]=False
				d[(A[ran]-m)+x]=False
				swap(A, m, ran)
				if(queensProb(A, m-1, x,b,d)):
					return A
				swap(A, m, ran)
				b[A[ran]+m]=True
				d[(A[ran]-m)+x]=True	





def swap(A, x, y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp



import time



#Codigo que imprime las pruebas al correr el archivo en el formato cantidaReinas;t1;t2
#t1 = tiempo del algoritmo de backtracking
#t2 = tiempo del algoritmo de las vegas

for i in range( 100):
	N = random.randrange(4,20)
	a =[]
	for i in range(N+1):
		a+=[i]
	m = N
	x = N-1
	b = ((2*N)+1) * [True]
	d = ((2*N)-1) * [True]
	res =""
	start_time = time.time()
	(queensFastBT(copy.deepcopy(a), m, x,copy.deepcopy(b),copy.deepcopy(d)))
	t1 = time.time() - start_time 
	res+=(str(N)+";"+str((t1)))
	start_time2 = time.time()
	(queensProb(copy.deepcopy(a), m, x,copy.deepcopy(b),copy.deepcopy(d)))
	t2=time.time() - start_time2
	res+=(";"+str((t2)))
	print(res)



