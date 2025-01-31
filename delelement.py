'''Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
Note: There is a trailing space at the end of the list.'''


input_values = input().strip().split()
values_set = set(map(int, input_values))


element_to_delete = int(input().strip())


if element_to_delete in values_set:
    values_set.remove(element_to_delete)
    
    sorted_values = sorted(values_set)
    print(" ".join(map(str, sorted_values)) + " ")
else:
    print("Given value is not present in the set list.")
