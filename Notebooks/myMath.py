from functools import reduce

def add(x:int, y:int)->int:
    return x+y
def sub(x:int, y:int)->int:
    return x-y

class Math:
    def __init__(self, nums:list[int]) -> None:
        self.nums = nums

    def sum(self) -> int:
        add = lambda x,y: x+y 
        return reduce(add, self.nums)

var = 9

employee_name = "Mario"
age = "55"
title = "owner"

def details():
    print("Employee name is:  ", employee_name)
    print("Employee age is: ", age)
    print("Employee title is:  ", title)


def word_count(sentence):
    # Function to check number of words, Returns word count in string
    words = len(sentence.split())
    print(words)
    return words

def char_count(sentence):
    # Function to check number of characters, Returns character count in string
    chars = len(sentence)
    print(chars)
    return chars

def first_char(sentence):
    # Function to check first character using string index, Returns first character in string
    first = sentence[0]
    return first

def last_char(sentence):
    # Function to check last character using string index, Returns last character in string
    last = sentence[-1]
    return last

# inside "__main__" are executable code for this file, means codes inside "__main__" will execute when running this file
# code outside of "__main__" can be used by other program as they work as modules and can be imported in other programs by importing myMath as it is 
# name of this file, but code inside "__main__" can't be used by other programs as these codes only belong to this file
if __name__ == "__main__":
    print("this is main file")
