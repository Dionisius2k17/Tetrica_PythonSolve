import collections
import re
import string

tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

def appearance(intervals):
    i = 0
    total_time = 0
    while i < 3:
        print("The duration of the lesson is ",
              tests[i].get('data').get('lesson')[1] - tests[i].get('data').get('lesson')[0], "seconds")
        if len(tests[i].get('data').get('pupil')) % 2 != 0 or len(tests[i].get('data').get('tutor')) % 2 != 0:
            print("ERROR: The number of timestamps couples in pupil and/or tutor is not even!")
            break
        time = tests[i].get('data').get('lesson')[0]
        c = 0
        while time <= tests[i].get('data').get('lesson')[1]:
            c = 0
            while c < len(tests[i].get('data').get('pupil')):
                d = 0
                while d < len(tests[i].get('data').get('tutor')):
                    time2 = 0
                    if time in range(tests[i].get('data').get('pupil')[c], tests[i].get('data').get('pupil')[c+1]) and \
                        time in range(tests[i].get('data').get('tutor')[d], tests[i].get('data').get('tutor')[d+1]):
                        time2 = time2 + 1
                    d = d + 2
                total_time = total_time + time2
                c = c + 2
            time = time + 1


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       #assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'