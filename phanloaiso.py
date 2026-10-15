n = int(input("nhap so n : "))
def f(n):
    if n % 2 == 0:
        return "CHAN"
    else :
        return "LE"
if n > 0 :
    print("DUONG")
    print (f(n))
elif n < 0 :
    print("AM")
    print(f(n))
else : 
    print("So 0 ")