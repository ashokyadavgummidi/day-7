

set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break

    if c==3:
        for val in set3:
            if val in set2 or val in set1:
               flag=1
               break
if flag==0:
    print("Disjoint")
else:
    print("joint")
            

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3=[]
i=0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)
