list_num_2 = []
list_num_3 = []
list_num_in_2 = []
list_num_in_3 = []
n = int(input("Number where do you want to terminate: "))
i = 1
while i<=n:
    x = i**2
    y = i**3
    list_num_2.append(x)
    list_num_3.append(y)
    #m = 1/x
    #n = 1/y
    ##list_num_in_2.append(m)
    ##list_num_in_3.append(n)
    i=i+1

print(list_num_2)
print(list_num_3)
print(list_num_in_2)
print(list_num_in_3)