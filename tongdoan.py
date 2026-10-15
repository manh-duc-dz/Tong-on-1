n = int(input("nhap so n : "))
q = int(input("nhap so q : "))
A = []
for i in range (n):
    k = int(input())
    A.append(k)
for i in range (q):
    t = 0
    l = int(input("nhap so l : "))
    r = int(input("nhap so r : "))
    for j in range(l,r+1):
        t = t+ A[j]
    print(t)
