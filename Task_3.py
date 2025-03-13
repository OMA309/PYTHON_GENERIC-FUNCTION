
'''Create a list with the following names
Mayowa
chizoba
Chigozie
Write a code that will extract names that begin with a capital letter and end with letter a
But If there is any name that begin with a capital letter but doesn’t end with letter a like Chigozie, convert its last letter to letter a, at the end it will turn it to Chigozia
Hint: The final list should contain just Mayowa and Chigozia 
'''
names = ['Mayowa','chizoba', 'Chigozie']
new_result = []
for items in names:
      
    '''
    if the name starts with a capital letter and ends with a, add it to the new list
    Args:
    items (str): name to be checked
    items.isupper() : checks if the first letter of the name is capital
    items.endswith("a"): checks if the name ends with a
    return:
    new_result (list): list of names that meet the conditions

    '''
    if items[0].isupper() and items.endswith('a'): # check if the name starts with a capital letter and ends with a
        new_result.append(items)
    elif items[0].isupper()  and not items.endswith('a'): # check if the name starts with a capital letter but doesn’t end with a
        not_letter_a = items[:-1] + 'a' # remove the last letter and add a
        new_result.append(not_letter_a) # add the new name to the list

print(new_result)         
        

        
