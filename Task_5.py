
'''
Build a generic function that will filter out bad entries and also accomodate yield
'''

Info = []  

def filter_entries(Info): # generic function to filter out bad entries
    '''
    Build a generic function that will filter out bad entries and also accomodate yield
    Args:
    Info (list): A list of entries to be filtered
    Results:
    A generator that yields the filtered entries
    '''
    final_outcome = [] # the new list that the error entries will be added to
    for entry in Info:
        if type(entry) != str:  # if the entry is not a string, it's a bad entry
            if entry.isalpha():
                final_outcome.append(entry)
    yield final_outcome  # yield the list of bad entries

cross_check = filter_entries(Info)  # call the function with the list of entries

for item in cross_check:# loop through the generator
    print(item) # print each item in the generator


