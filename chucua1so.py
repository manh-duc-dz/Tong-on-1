n = int(input("nhap so n : "))
m = n
t = 0
while m > 0 :
    i = m % 10 
    t += i
    m //= 10
s = str(n)
def f(n):
    if s == s[::-1] : 
        return "YES"
    else :
        return "NO"
print(len(s))
print(t)
print(f(n))
