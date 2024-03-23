def quick_sort(array):
    """This function using quick sort algoritm to sort array
        ARGS: array: list. Not sorted list
        Returns: list. Sorted list using quick sort algoritm
    """
    if len(array)<=1:
        return array
    elem = array[0]
    left = list(filter(lambda x: x<elem, array))
    center = [i for i in array if i == elem]
    right = list(filter(lambda x: x>elem, array))
    return quick_sort(left) + center + quick_sort(right)

def finding_element_by_value(array: list, value: any)-> int:
    """This function finding index of element with value 'value' in list 'array'
        Args: array: list
            value: any. Ellement that we will find index
        Return: int. Index of the ellement """
    for i, elle in enumerate(array):
        if elle == value:
            return i
    return -1

def finding_fifth_minimum_values_in_array(array: list)-> list:
    """This function finding first five minimum values of given array
        Args: array: list
        Return: list. First five minimum values
    """
    result = []
    for i in range(5):
        minimum = min(array)
        result.append(minimum)
        array.remove(minimum)
    return result

def finding_fifth_max_values_in_array(array: list)-> list:
    """This function finding first five maximum values of given array
        Args: array: list
        Return: list. First five maximum values
    """
    result = []
    for i in range(5):
        maximum = max(array)
        result.append(maximum)
        array.remove(maximum)
    return result

def finding_arithmetic_mean_of_array(array: list)->float:
    """This function finding arithmetic mean of all elements in given array
    Args: array: list
    Return: arithmetic mean: float
    """
    return sum(array)/len(array)
def array_without_same_ellements(array: list)->list:
    """This function creating new list from given
    and delete all same elements
    Args: array: list
    Return: finded array: list"""
    res = []
    for e in array:
        if e not in res:
            res.append(e)
    return res

def search_sequence(array, sequence):
    """
    Function to search for a sequence of elements in a list.
    
    Args:
    array: list
    sequence: list
    Returns: 
    int
    """
    
    if not sequence:
        return 0
    
    for i in range(len(array) - len(sequence) + 1):
        if array[i:i + len(sequence)] == sequence:
            return i
    
    return -1