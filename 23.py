list_num = []
for i in range(0,10):
    if i == 0:
        x = int(input("Enter your first number: "))
        list_num.append(x)
    else:
        x = int(input("Enter your next number: "))
        list_num.append(x)
##print("In random order the list will be like: ",list_num)
for i in range(0,len(list_num)):
    for j in range(0,len(list_num)):
        if j == 9:
            break
        elif list_num[j] >= list_num[j+1]:
            list_num[j],list_num[j+1]=list_num[j+1],list_num[j]
        else:
            continue
##print("In sorted order the list will be: ",list_num)
print("the gratest number will be: ",list_num[9])