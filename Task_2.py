
'''Task 2
Create a list of the below attributes
first name
last_name
date of birth
Transform the name of the attributes to follow the naming convention we have in the last_name
Meaning, at the end, the final list should be first_name, last_name, date_of_birth
Please make sure the newly transformed attributes are put inside another list.
'''

# Define the list of attributes
biodata = ["first name", "last_name", "date of birth"]

def transform_attribute(biodata):
    ''' 
     Transform the name of the attributes to follow the naming convention we have in the last_name
     Args:
     biodata (list): A list of attributes
     Returns:
     list: A list of transformed attributes
     '''
    newly_transformed = []  # Create a new list to store the transformed attributes

    for item in biodata:
        result = item.replace(" ","_") # Replace spaces with underscores
        newly_transformed.append(result)
    return newly_transformed

print(transform_attribute(biodata))     


    
