def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    integral = []
    for i in student_scores:
        integral.append(round(i))
    return integral


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    failed_students = []

    for i in student_scores:
        if i <= 40:
            failed_students.append(i)

    return len(failed_students)


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    top_scores = []

    for i in student_scores:
        if i >= threshold:
            top_scores.append(i)

    return top_scores


def letter_grades(highest):
    """ 
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    inc = int((highest - 40) / 4)

    return [score for score in range(41, highest, inc)]


def student_ranking(student_scores, student_names):
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """
    result = []

    for i in range(0, len(student_names)):

        result.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")

    return result


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for student in student_info:

        if student[1] == 100:
            return student

    return "No perfect score."
