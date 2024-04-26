# list comprehension
#list comprehension is a method of shortening syntax when we wan to create
# a new list from an already existing list
   #normal form
# list_of_number = []
# for i in range(10):
#     list_of_number.append(i)
# print(list_of_number)
  #comprehension
#list_of_number =[i for i in range(10)]
#print(list_of_number)


#list = [expression for item in  iterables if condition == true]
# for i in range(1,50):
#     if i %2 == 0:
#         print (i)

#even_numbers = []
#for i in range(1,50):
    #if i % 2 == 0:
        #even_numbers.append(i)
#print (even_numbers)

  #comprehension
#even_numbers = [i for i in range(1,50)if i % 2 ==0]
#print(even_numbers)

list_of_fruit=['apple','pineapple','orange','sour sop','tangerine','pear','grape','cumcumber']
# new_list =[]
# for fruit in list_of_fruit:
#     if 'p'in fruit:
#         new_list.append(fruit)
# print(new_list)
  #comprehensio
# new_list = [fruit for fruit in list_of_fruit if 'apple'not in fruit]
# print(new_list)

# for item in list_of_fruit:
#     if 'apple' not in item:
#         print (item)


list_of_number = [98,58,78,68,28,51,25,101]
# div = [i/2 for i in list_of_number]
# print(div)

# new_list = []
# for i in list_of_number:
#     new_list.append(i/2)
# print(new_list)

# odd_num1 = []
# for i in list_of_number:
#     if i%2 != 0:
#         odd_num.append(i/2)
# print(odd_num1)

odd_num =[i/2 for i in list_of_number if i%2 != 0]
print(odd_num)

