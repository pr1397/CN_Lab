def gcd(e,z):
    if (z == 0):
        return e
    else:
        return gcd(z,e%z)
p = 3
q = 11
pt = 7
n = p*q
z = (p-1)*(q-1)
print("p= ",p, " q= ", q, " n= ", n, " phi= ",z)
e = 2
while e < z:
    if gcd(e,z) == 1:
        break
    else:
        e+=1
print("e = ",e)
d = 2
while d < z:
    if (e*d) % z == 1:
        break
    else:
        d+=1
enc = (pt**e)%n
print("d= ",d,"\nenc = ", enc, "\ndec= ",(enc**d)%n)