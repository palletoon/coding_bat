'''
the Warmup-1/monkey_trouble problem from Coding Bat
'''
def monkey_trouble(a_smile: bool, b_smile: bool):
    '''
    Takes two parameters that indicate if the two monkeys are smiling or not. If both or neither are smiling, we are in trouble. Otherwise, wer're okday.
    '''
    #                   Both             or           NEITHER
    return True if (a_smile and b_smile) or (not a_smile and not b_smile) else False