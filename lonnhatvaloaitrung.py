n = int(input("nhap so n : "))
A = []
B = []
for i in range (n):
    k = int(input())
    A.append(k)
for i in range (len(A)):
    if A[i] == max(A):
        print(max(A), " ", i)
        break
d = {}
for i in A:
    if i not in d:
        d[i] = True
    else :
        B.append(i)
r = list(d.keys())
for i in d.keys():
    print(i,end = " ")