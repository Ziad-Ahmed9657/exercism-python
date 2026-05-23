"""Functions for organizing and calculating student exam scores."""

import warnings
warnings.filterwarnings('ignore')
import math as m
def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    round_list = list()
    for score in student_scores:
        round_list.append(int(round(score)))
    round_list.reverse()
    return round_list

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    count = 0
    for score in student_scores:
        if score <= 40:
            count+=1
        else:
            continue
    return count
    


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    above_or_equal_threshold = list()
    for score in student_scores:
        if score >= threshold:
            above_or_equal_threshold.append(score)
        else:
            continue
    return above_or_equal_threshold

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    lower = 41
    difierent_high_low = highest - lower # 59
    number_every_step = m.ceil(difierent_high_low / 4) # 14
    lower_list = list()
    lower_list.append(41)
    for _ in range(1,5):
        lower = lower + number_every_step
        if lower < highest:
            lower_list.append(lower)
        else:
            break

    return lower_list


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    scores = list()
    for index, name in enumerate(student_names):
        scores.append(f"{index+1}. {name}: {student_scores[index]}")

    return scores

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    score_100 = []
    for name , score in student_info:
        if score == 100:
            score_100 = [name , score]
            break
    return score_100



