"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    for i, s in enumerate(student_scores):
        student_scores[i] = round(s)
    return student_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    amount_of_lower_scores = 0
    for s in student_scores:
        if s <= 40:
            amount_of_lower_scores += 1
    return amount_of_lower_scores


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_scores_list = []
    for s in student_scores:
        if s >= threshold:
            best_scores_list.append(s)
    return best_scores_list


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    difference = highest - 40
    threshold = round(difference / 4)
    lower_scores = []
    for i in range(4):
        lower_scores.append(highest - difference + 1 + threshold * i)
    return lower_scores
        


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    student_ranks = []
    for i in range(len(student_scores)):
        student_ranks.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return student_ranks
        


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect_students = []
    for i in range(len(student_info)):
            if student_info[i][1] == 100:
                perfect_students.append(student_info[i][0])
                perfect_students.append(student_info[i][1])
                return perfect_students
    return perfect_students
            
