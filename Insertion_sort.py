list=[2,3,1,6,5,4]
for j in range(1,len(list)):
    key=list[j]
    i=j-1
    while(i>=0 and list[i]>key):
        list[i+1]=list[i]
        i-=1
    list[i+1]=key

print(list)
