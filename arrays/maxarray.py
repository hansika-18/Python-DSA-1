def max_of_subarrays(a,k):
     li=[]
     for i in range(k,len(a)+1):
        li.append(maximum(a,i-k,i))
     return li
def maximum(a,st,end):
    max=0
    for i in range(st,end):
        if max<a[i]:
            max=a[i]
    return max

numbers = [1,3,-1,-3,5,3,6,7]
print(max_of_subarrays(numbers,3))


