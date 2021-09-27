import sys
nmov=0
subconjuntos=[]


def move(n,torre1,torre3,conj):
        global nmov
        nmov+=1
        print ("Mov numero: ", nmov,"move disco:",n," de:",torre1,"-->",torre3)

def hanoi(n,torre1,torre3,torre2,conj):
    if(n==1):
        move(n,torre1,torre3,conj)
    else:
        hanoi(n-1,torre1,torre2,torre3,conj)
        move(n,torre1,torre3,conj)
        hanoi(n-1,torre2,torre3,torre1,conj)

    
if __name__ == '__main__':

    print("Digite a quantidade de discos: ")
    ndiscos= int(input())
   
    conj=[]
    subconjuntos.append([])
    for i in range(0,ndiscos):
        conj.append(0)
    hanoi(ndiscos,'A','B','C',conj)