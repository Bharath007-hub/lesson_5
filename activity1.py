lst = ["Apple", "banana", "kiwi", "orange", "Guava"]
print("length of the list: ", len(lst))
print("First element: ", lst[0])
print("last element",lst[-1])

lst.append("kiwi")
print("updated list: ", lst)

lst.reverse()
print("Updated list: ",lst)

lst.sort()
print("Sorted list: ",lst)

lst.pop(1)
print("Updated list: ",lst)

lst.reverse()
print("Updated list: ", lst)

print("Multiplication on the list: ", lst*2)

lst = lst[:4]
print("Sliced list: ",lst)

lst.clear()
print("Updated list: ",lst)