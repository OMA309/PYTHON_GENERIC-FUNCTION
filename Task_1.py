

# Create a function that return the first name of anyone
def get_first_name(first_name: str):
    """ 
    A function that return the first name of anyone
    Args:
    first_name (str): the first name of anyone 
    Returns:
    str : the first name of anyone

    """
    return first_name


 # Create another function that return the last name of anyone
def get_last_name(last_name: str):
    """ 
    A function that return the first name of anyone
    Args:
    last_name (str): the first name of anyone 
    Returns:
    str : the last name of anyone

    """
    return last_name

#Then Create a function that will concatenate the first name and the last name that will be returned from those 2 functions
def get_full_name(first_name,last_name):
    """
    the function that concatenate the first name and the last name together
    Args:
    first_name (str): the first name of anyone
    last_name (str): the last name of anyone
    Returns:
    str: the full name of anyone
    """
    from_first_function = get_first_name(first_name) # call the function get_first_name and store the result in a variable
    from_second_function = get_last_name(last_name) # call the function get_last_name and store the result in a variable
    return f"My full name is {from_first_function} {from_second_function}." # concatenate the first name and the last name together and return the result





       
