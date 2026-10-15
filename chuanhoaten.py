s = input("nhập chuỗi : ")
s1 = ""
d = 0
A = []
t = 0
s = " " + s
s = s.rstrip()
for i in s :
    i = i.lower()
    if i == " ":
        t += 1
    else : 
        t = 0 
        A.append(i)
    if t != 1:
        continue
    A.append(i)
for i in range (len(A)):
    if A[i] == " ":
        d += 1
        A[i+1] = A[i+1].upper()
    s1 = s1 + A[i]
s1 = s1.lstrip()
print(d)
print(s1)
    