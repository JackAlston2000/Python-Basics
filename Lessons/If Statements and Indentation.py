#Variables Tutorial
import sys, time, random
class lesson(object):

    def __init__(self, lessonType):
        self.lesson = lesson
        getattr(lesson,lessonType)()
    def lesson1():
        def type(sentence):
            for l in sentence:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(random.uniform(0,0.1))

        type(
"""Lesson: Loops

Sometimes you want code that can repeat itself, to make things
more efficient. Lets see if we can repeat a print function!

while True:
    print("This will repeat forever!")
""")
        print("============================")
        for x in range(200):
            print("This will repeat forever!")
        print("============================")
        type(
"""This is really useful for making things more efficient! You
won't hae to repeat the same lines of code, you could just have
one loop doing the same line over and over again!

How neat is that?
""")
