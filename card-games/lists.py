"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

import warnings 
warnings.filterwarnings('ignore')
def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    rounds = list()
    [rounds.append(number+i) for i in range(3)]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    
    concatenate_list = rounds_1 + rounds_2
    return concatenate_list

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    check = True if number in rounds else False
    return check


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    average = sum(hand)/len(hand)
    return average

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    # 1st way: Take the average of the first and last number in the hand:
    Average_first_last = (hand[0] + hand[-1]) / 2
    # 2nd way: Using the median (middle card) of the hand:
    Median_middle_card = len(hand) // 2
    Median_middle_card = hand[Median_middle_card]
    # Average with normal way:
    average = sum(hand) / len(hand)  
    if Average_first_last == average or Median_middle_card == average:
        return True
    else:
        return False
    
def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    odd_list = list()
    even_list = list() 
    odd_ave = 0
    even_avg = 0
    for index , value in enumerate(hand):

        if index % 2 == 0:
            even_list.append(hand[index])
        else:
            odd_list.append(hand[index])
        
    odd_avg = sum(odd_list) / len(odd_list)
    even_avg = sum(even_list) / len(even_list)

    if odd_avg == even_avg:
        return True
    else:
        return False
    


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1]*2
    return hand


