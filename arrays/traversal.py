def traversal(arr):
  print('[',end="")
  for i in range(len(arr)-1):
    print(arr[i],end=",")
  print(arr[i+1],end=']')  

def shiftleft(a,val):
  temp=val
  ar=[0 for i in range (len(a))]
  for i in range(0,val):
    ar[val]=a[i]
    val+=1
  val=temp
  j=0
  for i in range(val,len(a)):
      ar[j]=ar[i]
      j+=1
  print(ar)

a=[1,2,3,4,5]
print()
traversal(a)
print()
shiftleft(a,1)



