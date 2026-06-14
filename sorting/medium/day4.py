import sys
from unittest import result
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test

def sort_by_last(txt):
    return ' '.join(sorted(txt.split(), key = lambda x: x[-1]))



Test.assert_equals(sort_by_last("herb camera dynamic"), "camera herb dynamic")
Test.assert_equals(sort_by_last("stab traction artist approach"), "stab approach traction artist")
Test.assert_equals(sort_by_last("sample partner autonomy swallow trend"), "trend sample partner swallow autonomy")
Test.assert_equals(sort_by_last("dividend platform pupil conclusion silence breakfast"), "dividend silence pupil platform conclusion breakfast")
Test.assert_equals(sort_by_last("harm"), "harm")
Test.assert_equals(sort_by_last("card warrant opinion medium illustrate"), "card illustrate medium opinion warrant")
Test.assert_equals(sort_by_last("cause fine virtue"), "cause fine virtue")
Test.assert_equals(sort_by_last("introduce fashionable cause sacrifice reality"), "introduce fashionable cause sacrifice reality")
Test.assert_equals(sort_by_last("brick moral institution loud talk resign worth"), "loud worth brick talk moral institution resign")
Test.summary()

def sort_it(lst):
    return sorted(lst, key = lambda x: x if isinstance(x, int) else x[0])



Test.assert_equals(sort_it([4, 1, 3]), [1, 3, 4])
Test.assert_equals(sort_it([[4], [1], [3]]), [[1], [3], [4]])
Test.assert_equals(sort_it([4, [1], 3]), [[1], 3, 4])
Test.assert_equals(sort_it([[4], 1, [3]]), [1, [3], [4]])
Test.assert_equals(sort_it([[3], 4, [2], [5], 1, 6]), [1, [2], [3], 4, [5], 6])
Test.assert_equals(sort_it([[3], 7, [9], [5], 1, 6]), [1, [3], [5], 6, 7, [9]])
Test.assert_equals(sort_it([[3], 7, [9], [5], 1, 6, [0]]), [[0], 1, [3], [5], 6, 7, [9]])

Test.summary()

def correct_sentences(s):
    words = s.split()
    sentences = []
    current = []

    for word in words:
        if word[0].isupper() and current:
            sentences.append(" ".join(current))
            current = [word]
        else:
            current.append(word)

    sentences.append(" ".join(current))

    return ". ".join(sentence[0].upper() + sentence[1:] for sentence in sentences) + "."
Test.assert_equals(correct_sentences("  mubashir loves  edabit  Matt  loves  edabit  "), "Mubashir loves edabit. Matt loves edabit.")
Test.assert_equals(correct_sentences("  he is an engineer He sleeps a lot"), "He is an engineer. He sleeps a lot.")
Test.assert_equals(correct_sentences(" his english is not good Help him     Thank you"), "His english is not good. Help him. Thank you.")
Test.assert_equals(correct_sentences(" he is ready to join   airforce  Waiting for the  final approval"), "He is ready to join airforce. Waiting for the final approval.")
Test.summary()
