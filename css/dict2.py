i=0                                         #starting point for loop
num=int(input("Enter he value In num:"))    #Number Of times it has to be repeated
ff = []                                     #Empty List
while i<num:                                #while 0 less than inputted value
    a=str(input("Enter Name:"))             #enter a str value
    b=int(input("Enter Integer Number:"))   #enter a int value
    f={"Name":a,"Int":b}                    #automatically adds int and sting in  dictionary
    ff.append(f)                            #adds value in dictionary in list
    i+=1                                    #ends while loop
print(ff)                                   #prints list