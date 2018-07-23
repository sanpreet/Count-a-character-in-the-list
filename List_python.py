# ****************************List Case**************************************************
#this is the function to evlauate the vision of this code which is to count a particular count in the list#
def list_python(list_passed,character_count):
    count=0;  #initial value of counter
    for i in list_passed: #i is the member function of list
        if i==character_count:  #checking the occurance of element in the list
            count=count+1       #increment the count
    return count

list_passed = ['a','a','a','b','f']      #list from where the elements has to be checked
value_to_be_counted= input("Enter the character to be counted:")  #user input the value to be checked from the list

output= list_python(list_passed,value_to_be_counted)               #this will go to function list_python
print("Counting of {} : ".format(value_to_be_counted),output)       #You can see the output after this line