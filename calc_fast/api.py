import random
import time

# create random number
def get_random_number(start=1, end=10):
    """Create random number between start and end range."""
    return random.randint(start, end)


# calculate operation
def calculate(expresion):
    """Return calculation result of expresion
    If any exception occured return None."""
    try:
        return eval(expresion)
    except Exception:
        return None


def compare(response, result):
    return response == result


# calculate current time
def current_time():
    return time.time()


# get time difference
def get_time_diff(start_time, end_time):
    return end_time - start_time


def get_socres():
    scores = None
    with open("scoreboard.txt", "r") as score_file:
        scores = score_file.readlines()
    scores = [score.strip() for score in scores]
    return scores


def save_score(scores):
    with open("scoreboard.txt", "w") as score_file:
        for score in scores:
            score_file.write(f"{score}\n")


def compare_scores(score, scores):
    for item in scores[:]:
        if score < float(item):
            index = scores.index(item)
            scores[index] = score
            break
    return scores  # modified scores


if __name__ == "__main__":
    pass
