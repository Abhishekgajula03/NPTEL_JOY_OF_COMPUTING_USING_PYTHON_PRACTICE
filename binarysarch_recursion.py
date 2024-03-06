def binarysearch(l,x,start,end):
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        mid=int((start+end)/2)
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            return binarysearch(l, x, start, mid-1)
        elif l[mid]<x:
            return binarysearch(l, x, mid+1, end)
l=[20,22,34,55,90]
x=int(input("enter the number"))
a=binarysearch(l, x, 0,len(l)-1)
print(a)
    
