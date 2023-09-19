import time
def bubblesort (a):
    n=len(a)
    for i in range(n-2):
        min = i
        for j in range(i+1,n):
            if a[j]<a[min]:
                temp=a[j]
                a[j]=a[min]
                a[min]=temp
c=[34,46,43,27,57,41,45,21,70]            
print("befor sortin",c)    
bubblesort(c)
print("ofter sorting",c)
                