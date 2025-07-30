lst_numbers=[11,12,23,34,56,78,12,12]
print("Original list ",lst_numbers)

# append item/element into list
lst_numbers.append("Hello")
print(f" After append {lst_numbers}")

#created another list
lst_name=['Pooja','Khushali']
#appeding list/list item into list
lst_numbers.append(lst_name[1])
print(f" After append list  {lst_numbers}")

#insert item/element into list at specified position
lst_numbers.insert(3,900)
print(f" After insert list  {lst_numbers}")

#remove specified element from list
lst_numbers.remove(23)
print(f" After remove list  {lst_numbers}")

#delete
del lst_numbers[-2]
print(f" After deleting list element  {lst_numbers}")

#to extend list
lst_number2 = [12.23,3.23,56.45]
lst_numbers.extend(lst_number2)
print(f" After extends list element  {lst_numbers}")

count_i=lst_numbers.count(19992)
print(count_i)

index_i=lst_numbers.index(12,3)
print(index_i)