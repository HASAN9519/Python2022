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

# inside "__main__" are executable code for this file, means codes inside "__main__" will execute when running this file
# code outside of "__main__" can be used by other program as they work as modules and can be imported in other programs by importing myMath as it is 
# name of this file, but code inside "__main__" can't be used by other programs as these codes only belong to this file
if __name__ == "__main__":
    print("this is main file")
