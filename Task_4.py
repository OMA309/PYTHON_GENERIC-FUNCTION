'''
Let’s assume we usually receive some data from the marketing team every monday inside a list. Elements expected inside that list are the names of the customers.
Let’s assume what they sent contains  Wofai, Zainab, A4atullah
Write a function that will intentionally make your code fail if what they have inside that list doesn’t look like a valid name, this will allow us to quickly get in touch with the marketing team that they have a bad entry.
In the values above, you can see A4atullah is a bad entry.
So it should fail when it gets to A4atullah.
Please when you are writing that function , make sure it gives the exact entry that is bad with a meaningful message, so that we can be sure of the specific entry and relay back to the marketing team.
'''

Names = []

def Check_error(Names):
    ''' 
    check if there is a bad entry in the list of names
    Args: 
    Names (list): list of names
    Returns:
    None if no ValueError occurs
    '''
    for name in Names:
        if not name .isalpha(): # check if the name is alphabetic
            raise ValueError (f"Invalid name: {name}. Names should only contain alphabets . Kindly check with the marketing team")

Check_error(Names)        
