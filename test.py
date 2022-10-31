'''
    3. Write a function to take a list. From the list find the number that occurs most number of times.
       Example :
           listA=[10,20,30,40,50,60,100,11,12,13]
           result=func_exec(listA)
           print(result)
           Expected Output : []
       Example :
          listA=[10,21,30,41,50,500,100,11,12,13,21]
         result=func_exec(listA)
         print(result)
         Expected Output : [21,]
        Example :
           listA=[10,21,30,41,50,50,100,11,12,13,21]
           result=func_exec(listA)
            print(result)
            Expected Output : [21,50]
'''
#Define function name with check
def check(Org_list):
    #define new dict
    new_dict={}
    #iterates original list
    for i in Org_list:
        #storing the count of number of times occur by the element in list
        count=Org_list.count(i)
        #checking for the count is greater than one
        if(count>1):
            #Adding to new dict with key as element and value as count of the element
            new_dict[i]=count
    #Define new list        
    new_list=[]
    #storing values from new dict
    values=new_dict.values()
    #iterates keys and values from new dict simantanously
    for _key,_value in new_dict.items():
        #checking for is the present value is maximum value
        if(_value==max(values)):
            #Add key to new list
            new_list.append(_key)

    #Finally return new list
    return new_list

#Calling function
result=check([10,21,30,41,50,50,100,11,12,13,21])
print('Final output {}'.format(result))
