list_num_2 = []
list_num_3 = []
list_num_in_2 = []
list_num_in_3 = []
n = int(input("Number where do you want to terminate: "))
for i in range(1,n+1):
    x = i**2
    y = i**3
    list_num_2.append(x)
    list_num_3.append(y)

for i in range(1,n+1):
    x = 1/(i**2)
    y = 1/(i**3)
    list_num_in_2.append(x)
    list_num_in_3.append(y)    

print(list_num_2)
print(list_num_3)
print(list_num_in_2)
print(list_num_in_3)