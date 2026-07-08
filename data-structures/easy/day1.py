import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test



def color_invert(rgb):
    return tuple(abs(255 - c) for c in rgb)



Test.assert_equals(color_invert((165, 170, 119)), (90, 85, 136))
Test.assert_equals(color_invert((165, 170, 136)), (90, 85, 119))
Test.assert_equals(color_invert((165, 170, 153)), (90, 85, 102))
Test.assert_equals(color_invert((165, 170, 170)), (90, 85, 85))
Test.assert_equals(color_invert((165, 170, 187)), (90, 85, 68))
Test.assert_equals(color_invert((165, 170, 204)), (90, 85, 51))
Test.assert_equals(color_invert((165, 170, 221)), (90, 85, 34))
Test.assert_equals(color_invert((165, 170, 238)), (90, 85, 17))
Test.assert_equals(color_invert((165, 180, 0)), (90, 75, 255))
Test.assert_equals(color_invert((165, 180, 17)), (90, 75, 238))
Test.assert_equals(color_invert((165, 180, 34)), (90, 75, 221))
Test.assert_equals(color_invert((165, 180, 51)), (90, 75, 204))
Test.assert_equals(color_invert((165, 180, 68)), (90, 75, 187))
Test.assert_equals(color_invert((165, 180, 85)), (90, 75, 170))
Test.assert_equals(color_invert((165, 180, 102)), (90, 75, 153))
Test.assert_equals(color_invert((0, 0, 0)), (255, 255, 255))
Test.assert_equals(color_invert((0, 0, 17)), (255, 255, 238))
Test.assert_equals(color_invert((0, 0, 34)), (255, 255, 221))
Test.assert_equals(color_invert((0, 0, 51)), (255, 255, 204))
Test.assert_equals(color_invert((0, 0, 68)), (255, 255, 187))
Test.assert_equals(color_invert((240, 250, 153)), (15, 5, 102))
Test.assert_equals(color_invert((240, 250, 170)), (15, 5, 85))
Test.assert_equals(color_invert((240, 250, 187)), (15, 5, 68))
Test.assert_equals(color_invert((240, 250, 204)), (15, 5, 51))
Test.assert_equals(color_invert((240, 250, 221)), (15, 5, 34))
Test.assert_equals(color_invert((240, 250, 238)), (15, 5, 17))
Test.assert_equals(color_invert((255, 255, 255)), (0, 0, 0))
Test.assert_equals(color_invert((240, 180, 136)), (15, 75, 119))
Test.assert_equals(color_invert((240, 180, 153)), (15, 75, 102))
Test.assert_equals(color_invert((240, 180, 170)), (15, 75, 85))
Test.assert_equals(color_invert((240, 180, 187)), (15, 75, 68))
Test.assert_equals(color_invert((240, 180, 204)), (15, 75, 51))
Test.assert_equals(color_invert((240, 180, 221)), (15, 75, 34))
Test.assert_equals(color_invert((240, 180, 238)), (15, 75, 17))
Test.assert_equals(color_invert((240, 190, 0)), (15, 65, 255))
Test.assert_equals(color_invert((240, 190, 17)), (15, 65, 238))
Test.assert_equals(color_invert((240, 190, 34)), (15, 65, 221))
Test.assert_equals(color_invert((240, 190, 51)), (15, 65, 204))
Test.assert_equals(color_invert((240, 190, 68)), (15, 65, 187))
Test.assert_equals(color_invert((240, 190, 85)), (15, 65, 170))
Test.assert_equals(color_invert((240, 190, 102)), (15, 65, 153))
Test.assert_equals(color_invert((240, 190, 119)), (15, 65, 136))
Test.assert_equals(color_invert((240, 190, 136)), (15, 65, 119))
Test.assert_equals(color_invert((240, 190, 153)), (15, 65, 102))
Test.assert_equals(color_invert((240, 190, 170)), (15, 65, 85))
Test.assert_equals(color_invert((240, 190, 187)), (15, 65, 68))
Test.assert_equals(color_invert((240, 190, 204)), (15, 65, 51))
Test.assert_equals(color_invert((240, 190, 221)), (15, 65, 34))
Test.assert_equals(color_invert((240, 190, 238)), (15, 65, 17))
Test.assert_equals(color_invert((240, 200, 0)), (15, 55, 255))
Test.assert_equals(color_invert((240, 200, 17)), (15, 55, 238))
Test.assert_equals(color_invert((240, 200, 34)), (15, 55, 221))
Test.assert_equals(color_invert((240, 200, 51)), (15, 55, 204))
Test.assert_equals(color_invert((240, 200, 68)), (15, 55, 187))
Test.assert_equals(color_invert((240, 200, 85)), (15, 55, 170))
Test.assert_equals(color_invert((240, 200, 102)), (15, 55, 153))
Test.assert_equals(color_invert((240, 200, 119)), (15, 55, 136))
Test.assert_equals(color_invert((240, 200, 136)), (15, 55, 119))
Test.assert_equals(color_invert((240, 200, 153)), (15, 55, 102))
Test.assert_equals(color_invert((240, 200, 170)), (15, 55, 85))


def get_student_names(students):
    return sorted(students.values())


Test.assert_equals(get_student_names({
	"Student 1":"Steve",
	"Student 2":"Becky",
	"Student 3":"John"
}), ["Becky", "John", "Steve"])

Test.assert_equals(get_student_names({
	"Student 1":"Jacek",
	"Student 2":"Ewa",
	"Student 3":"Zygmunt",
	"Student 4":"Tomek"
}), ["Ewa", "Jacek", "Tomek", "Zygmunt"])


def integer_boolean(n):
    return [i == "1" for i in n]



Test.assert_equals(integer_boolean("100101"), [True, False, False, True, False, True])
Test.assert_equals(integer_boolean("10"), [True, False])
Test.assert_equals(integer_boolean("001"), [False, False, True])
Test.assert_equals(integer_boolean(""), [])
Test.assert_equals(integer_boolean("111"), [True, True, True])
Test.assert_equals(integer_boolean("000"), [False, False, False])
Test.assert_equals(integer_boolean("10010110"), [True, False, False, True, False, True, True, False])

def find_bob(names):
    if "Bob"  not in names:
        return -1
    return names.index("Bob")

Test.assert_equals(find_bob(["Jimmy", "Layla", "Mandy"]), -1)
Test.assert_equals(find_bob(["Bob", "Nathan", "Hayden"]), 0)
Test.assert_equals(find_bob(["Paul", "Layla", "Bob"]), 2)
Test.assert_equals(find_bob(["Garry", "Maria", "Bethany", "Bob", "Pauline"]), 3)


def count_all(txt):
    return {'LETTERS': sum (1 for i in txt if i.isalpha()), 'DIGITS': sum (1 for i in txt if i.isdigit())}


Test.assert_equals(count_all("Hello"), { "LETTERS": 5, "DIGITS": 0 })
Test.assert_equals(count_all("137"), { "LETTERS": 0, "DIGITS": 3 })
Test.assert_equals(count_all("H3LL0"), { "LETTERS": 3, "DIGITS": 2 })
Test.assert_equals(count_all("149990"), { "LETTERS": 0, "DIGITS": 6 })
Test.assert_equals(count_all("edabit 2018"), { "LETTERS": 6, "DIGITS": 4 }, "Spaces are not letters.")
Test.assert_equals(count_all("    "), { "LETTERS": 0, "DIGITS": 0 })


def matrix(x, y, z):
    return [[z] * y for _ in range(x) ] 



Test.assert_equals(matrix(3, 4, 0), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
Test.assert_equals(matrix(2, 3, "#"), [["#", "#", "#"], ["#", "#", "#"]])
Test.assert_equals(matrix(2, 3, -4), [[-4, -4, -4], [-4, -4, -4]])
Test.assert_equals(matrix(1, 2, 0), [[0, 0]])


Test.summary()


def find_occurrences(txt, ch):
    return {i.lower(): i.lower().count(ch.lower()) for i in txt.split()}



Test.assert_equals(find_occurrences("Hello World", "o"), {
	"hello" : 1,
	"world" : 1
})


Test.assert_equals(find_occurrences("Create a nice JUICY function", "c"),  {
	"create" : 1,
	"a" : 0,
	"nice" : 1,
	"juicy" : 1,
	"function" : 1
})


Test.assert_equals(find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "a"), {
	"an" : 1,
	"apple" : 1,
	"a" : 1,
	"day" : 1,
	"keeps" : 0,
	"archeologist" : 1,
	"away..." : 2
})

Test.assert_equals(find_occurrences("hello people of the planet Earth", "g"), {"hello": 0, "people": 0, "of": 0, "the": 0, "planet": 0, "earth": 0})
Test.assert_equals(find_occurrences("Reference site about Lorem Ipsum, giving information on its origins, as well as a random Lipsum generator.", "R"), {"reference": 2, "site": 0, "about": 0, "lorem": 1, "ipsum,": 0, "giving": 0, "information": 1, "on": 0, "its": 0, "origins,": 1, "as": 0, "well": 0, "a": 0, "random": 1, "lipsum": 0, "generator.": 2})
Test.assert_equals(find_occurrences("Lift your spirits with funny jokes, trending memes, entertaining gifs, inspiring stories,", "l"), {"lift": 1, "your": 0, "spirits": 0, "with": 0, "funny": 0, "jokes,": 0, "trending": 0, "memes,": 0, "entertaining": 0, "gifs,": 0, "inspiring": 0, "stories,": 0})
Test.assert_equals(find_occurrences("Thats not a camel, thats my wife.", "a"), {"thats": 1, "not": 0, "a": 1, "camel,": 1, "my": 0, "wife.": 0})
Test.assert_equals(find_occurrences("hippopotomonstrosesquippedaliophobia is the fear of long words", "p"), {"hippopotomonstrosesquippedaliophobia": 6, "is": 0, "the": 0, "fear": 0, "of": 0, "long": 0, "words": 0})
Test.assert_equals(find_occurrences("Some writers believe longs sentences are simply made by coupling clauses with the word and. This is called polysyndeton, and yes, it is one of twelve literary devices you can use to take charge of your boring writing. But its a cheap way to get a long sentence.", "s"), {"some": 1, "writers": 1, "believe": 0, "longs": 1, "sentences": 2, "are": 0, "simply": 1, "made": 0, "by": 0, "coupling": 0, "clauses": 2, "with": 0, "the": 0, "word": 0, "and.": 0, "this": 1, "is": 1, "called": 0, "polysyndeton,": 1, "and": 0, "yes,": 1, "it": 0, "one": 0, "of": 0, "twelve": 0, "literary": 0, "devices": 1, "you": 0, "can": 0, "use": 1, "to": 0, "take": 0, "charge": 0, "your": 0, "boring": 0, "writing.": 0, "but": 0, "its": 1, "a": 0, "cheap": 0, "way": 0, "get": 0, "long": 0, "sentence.": 1})
Test.assert_equals(find_occurrences("i wrote code to give me these long long long long long sentences", "l"), {"i": 0, "wrote": 0, "code": 0, "to": 0, "give": 0, "me": 0, "these": 0, "long": 1, "sentences": 0})
Test.assert_equals(find_occurrences("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa a spider", "a"), {"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": 133, "a": 1, "spider": 0})
Test.assert_equals(find_occurrences("she sell sea shells on the sea shore", "s"), {"she": 1, "sell": 1, "sea": 1, "shells": 2, "on": 0, "the": 0, "shore": 1})
Test.assert_equals(find_occurrences("Woah, I just realised, that I could, use this, to find, punctuation also.", ","), {"woah,": 1, "i": 0, "just": 0, "realised,": 1, "that": 0, "could,": 1, "use": 0, "this,": 1, "to": 0, "find,": 1, "punctuation": 0, "also.": 0})

Test.summary()