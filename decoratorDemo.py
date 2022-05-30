
def decorator(F):
    def new_F(a,b):
        print("input:",a,b)
        return F(a,b)
    return new_F


#get square sum
@decorator
def square_sum(a,b):
    # print("intput:", a, b)
    return a**2+b**2

#get square diff
@decorator
def square_diff(a,b):
    # print("intput:", a, b)
    return a**2-b**2

print (square_sum(2,1))
print (square_diff(2,1))