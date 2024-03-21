#13 202110846 염승태

def selection (A):
    n=len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1,n):
            if (A[j]<A[least]):
                least = j
        A[i],A[least] = A[least],A[i]
        print(A, i+1)

data = [3,7,9,4,2,8,1,5]
print('정리안됨 : ',data)
selection(data)
print('정리됨 : ',data)


#23 202110846 염승태

import collections
Q  = collections.deque()
Q.append(0)
Q.append(1)

print("F(0) = 0")
print("F(1) = 1")

for i in range(2,10) :
    ver1 =  Q.popleft()
    ver2 =  Q.popleft()
    ver = ver1 + ver2   
    Q.appendleft(ver2)
    Q.append(ver)
    print("F(%d) = "%i, ver)

#15 202110846 염승태
def string(T,P):
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j=0
        while j < m and P[j]==T[i+j]:
            j = j+1
        if j==m:
            return i
    return -1

text = '염승태'
pattern = '태'
print(pattern, 'in', text,'-->', string(text, pattern))#2는 있음, 1은 없음 
pattern = (pattern,'in',text,'-->',string(text, pattern))
