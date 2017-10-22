def median(L):
    l=sorted(L)
    if len(l)%2==0:
        return 0.5*(l[len(l)//2] + l[len(l)//2-1])
    elif len(l)%2!=0:
        return l[(len(l)-1)//2]


print (median([1]))
print (median([1,3,4,7]))
