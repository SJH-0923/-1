def root(a, b, c) :
    x1 = (-b + (b**2.0 - 4.0*a*c)**0.5) / 2.0*a
    x2 = (-b - (b**2.0 - 4.0*a*c)**0.5) / 2.0*a
    return x1, x2

r1,r2 = root(1,2,3)

'''print(r1,r2)'''

if type(r1) == complex :
    print('허수입니다.')

if type(r2) == complex :
    print('허수입니다.')



def root(a, b, c) :
    if -b + (b**2.0 - 4.0*a*c) < 0 :
        return None, None
    x1 = (-b + (b**2.0 - 4.0*a*c)**0.5) / 2.0*a
    x2 = (-b - (b**2.0 - 4.0*a*c)**0.5) / 2.0*a
    return x1, x2
