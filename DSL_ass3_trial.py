r = int(input("enter no of rows"))
c= int(input("enter no of coloumns"))
def A(r,c):
    A=[]
    for i in range (r):
        row=[]
        for j in range (c):
            inp=int(input())
            row.append(inp)
        A.append(row)    
    print("matrix A is")
  
    for i in range(r):
        for j in range(c):
            print(A[i][j], end=" ")
        print()
    return A

def B(r,c):
    B=[]
    for i in range (r):
        row=[]
        for j in range (c):
            inp=int(input(""))
            row.append(inp)
        B.append(row)
    print("matrix B is")
    for i in range(r):
        for j in range(c):
            print(B[i][j], end=" ")
        print()
    return B
    
def sum(a,b):
    sum=[]
    for i in range (len(a)): # or i in range r
        row=[]
        for j in range (len(a[0])): # or j in range c
            
            row.append(a[i][j]+b[i][j])
        sum.append(row)
    for i in range(r):
        for j in range(c):
            print(sum[i][j], end=" ")
        print()
    
def sub(a,b):
    sub=[]
    for i in range (len(a)): # or i in range r
        row=[]
        for j in range (len(a[0])): # or j in range c
            
            row.append(a[i][j]-b[i][j])
        sub.append(row)
    for i in range(r):
        for j in range(c):
            print(sub[i][j], end=" ")
        print()
    
def transA(a):
    trans=[]
    for i in range (len(a)):
        row=[]
        for j in range (len(a[0])):
            
            row.append(a[j][i])
        trans.append(row)
    for i in range(r):
        for j in range(c):
            print(trans[i][j], end=" ")
        print()

def transB(b):
    trans=[]
    for i in range (len(b)):
        row=[]
        for j in range (len(b[0])):
            
            row.append(b[j][i])
        trans.append(row)
    for i in range(r):
        for j in range(c):
            print(trans[i][j], end=" ")
        print()

def multiplication(a,b):
    mul=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                mul[i][j] += a[i][k] * b[k][j]
    for i in range(r):
        for j in range(c):
            print(mul[i][j], end=" ")
        print()

print("enter matrix A row wise")
a=A(r,c)

print("enter matrix B row wise ")
b=B(r,c)

print("sum of these matrices is")
s=sum(a,b) 
# sum(a,b) 

print("subtraction of these matrices is")
e=sub(a,b) 
# sub(a,b)

print("transpose of matrix A is")
transA(a) 

print("transpose of matrix B is") 
transB(b) 

print ("multiplication of these matrices is")
multiplication(a,b)
