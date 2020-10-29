# Exercise 1: 
# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns 
# a new list that contains all but the first and last elements.

def chop(inc_list):
    i = len(inc_list) - 1

    del inc_list[i]
    del inc_list[0]

    return None
    
def middle(inc_list):
    i = len(inc_list) - 1
    out_list = inc_list[:]

    del out_list[i]
    del out_list[0]

    return out_list

start_list = [1,2,3,4,5]

print("Original list:", start_list)
print("Return of chop:", chop(start_list))
print("Changed list:", start_list)
print("New List:", middle(start_list), "Old list:", start_list)