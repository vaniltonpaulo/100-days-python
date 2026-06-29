import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def find_occurrences(txt, ch):
    txt = txt.lower()
    ch = ch.lower()
    result = {}
    words = txt.split()
    for word in words:
        result[word] = word.count(ch)
    
    return result





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



def collatz(num):
    rounds = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        rounds += 1

    return rounds







Test.assert_equals(collatz(2), 1)
Test.assert_equals(collatz(3), 7)
Test.assert_equals(collatz(10), 6)
Test.assert_equals(collatz(6), 8)
Test.assert_equals(collatz(345), 125)
Test.assert_equals(collatz(72), 22)
Test.summary()


def calc(s):
    x =  "".join( str(ord(word)) for word in s)
    y = x.replace("7", "1")
    first = sum(int(i) for i in x)
    second = sum(int(i) for i in y)
    return first - second


Test.assert_equals(calc('ABCDabcd'), 12)
Test.assert_equals(calc('cdefgh'), 0)
Test.assert_equals(calc('ifkhchlhfde'), 6) 
Test.assert_equals(calc('aaaaaddddrijkl'), 36) 
Test.assert_equals(calc('abcdefghijklmnopqrstuvwxyz'), 18)
Test.assert_equals(calc('AABBCC'), 12) 
Test.assert_equals(calc('ABCDEFGH'), 24) 
Test.assert_equals(calc('anmatmudtr'), 18) 
Test.assert_equals(calc('suwvete'), 6) 
Test.assert_equals(calc('edabit'), 6) 
Test.assert_equals(calc('EDABIT'), 6) 
Test.assert_equals(calc('SLOWLLLY'), 36) 
Test.assert_equals(calc('COMEnananan'), 42) 
Test.assert_equals(calc('coupdetat'), 12) 
Test.assert_equals(calc('arsenal'), 12) 
Test.assert_equals(calc('byoaaasglrrsA'), 18) 
Test.assert_equals(calc('byoglrrsA'), 0) 
Test.assert_equals(calc('eyyyhenDDDUEN'), 6) 
Test.assert_equals(calc('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 78) 
Test.assert_equals(calc('zyxwvutsrqpon'), 6) 
Test.assert_equals(calc('ZYXWVUTSR'), 6)
Test.summary()


def rectangles(n):
    return ((n*(n+1))//2)**2



Test.assert_equals(rectangles(64), 4326400)
Test.assert_equals(rectangles(76), 8561476)
Test.assert_equals(rectangles(10), 3025)
Test.assert_equals(rectangles(79), 9985600)
Test.assert_equals(rectangles(84), 12744900)
Test.assert_equals(rectangles(0), 0)
Test.assert_equals(rectangles(60), 3348900)
Test.assert_equals(rectangles(29), 189225)
Test.assert_equals(rectangles(18), 29241)
Test.assert_equals(rectangles(74), 7700625)
Test.assert_equals(rectangles(16), 18496)
Test.assert_equals(rectangles(64), 4326400)
Test.summary()
