def  jme(my_list:list):
    x = 0
    for i in my_list:
        i = int(i)
        x = x + i 
    return  x
 
print("<<<<<   jame  >>>>>")    

my_list = []
count = True
while count == True:
    num = str(input("Enter your number : "))
    if num == '' :
        break
    my_list.append(num)


jame = jme(my_list)
print(f"your jame : {jame}")


