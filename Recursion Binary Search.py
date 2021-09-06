def search(a,index,start,end):
    if start==end:
        if a[start]==index:
            return start
        else:
            return -1
    else:
        mid=int((start+end)/2)
        if a[mid]==index:
            return mid
        elif a[mid]>index:
            return search(a,index,start,mid)
        else:
            return search(a,index,mid+1,end)

a=[5,8,10,45,54,56,67,78,87]
index=int(input("Enter Search Item : "))
ans=search(a,index,0,len(a)-1)
print(ans+1)
            