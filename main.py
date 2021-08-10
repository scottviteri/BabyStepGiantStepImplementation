#baby step giant step

def divmod(a,b):
    q,r = a//b,a%b
    return q,r

#extended euclidian
def gcd(a,b,alpha_1=0,alpha_2=1,beta_1=1,beta_2=0):
    if b == 0: return (a,alpha_2,beta_2)
    q = a//b
    return gcd(b,a%b,alpha_2-alpha_1*q, alpha_1, beta_2-beta_1*q, beta_1)

def inv(x, p=101):
    _,i,_ = gcd(x,p)
    return i % p

def square_exp(a,b,p):
    if b == 0: return 1
    if b % 2 == 0: return (square_exp(a,b//2,p)%p)**2 % p
    return (a * square_exp(a,b-1,p)) % p


def precompute_dlogs(b, c, p=101):
    d = {}
    invb = inv(b,p)
    for i in range(int(p**.5)+1):
        d[(square_exp(invb, i%(p-1), p)*c)%p] = i
    return d

def discrete_logarithm(b, c, p=101):
    dlogs = precompute_dlogs(b,c,p)
    rt = int(p**.5)
    for i in range(0,p,rt):
        k = square_exp(b,i,p) % p
        if k in dlogs:
            return i + dlogs[k]
    return -1

# sqrt(p) discrete logarithm operation
p = 10**9 + 7
discrete_logarithm(34,245,p) #316464245
square_exp(34,316464245,p) #245
