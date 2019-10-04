list1=[]
for i in range(0,101,2):
    list1.append(i)
x=int(input("Enter the number to be searched"))
print("number has been stored")
ul=int(len(list1)-1)
print("UL has been set")
ll=0
k=0
print(ul)
print(list1[12])
print("LL has been set.")
while ll<=ul:
    print("Inside the while loop")
    if(ul==0):
        if(list1[ul]==x):
            print("The number is found at the first position of the list.")
            k=1
        else:
            print("The number is not present in the list.")
            k=1
        break
    mid=int((ul+ll)//2)
    print(mid)
    if(list1[mid]==x):
        print("The number has been found at index "+str(mid))
        k=1
        break
    elif(list1[mid]>x):
        ul=mid-1
    else:
        ll=mid+1
if(k==0):
    print("The number is not found")

