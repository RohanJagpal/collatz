class Collatz:
    def __init__(self, startNum: int) -> None:
        self.startNum = startNum

    def __process(self, num: int) -> int:
        return num/2 if num%2==0 else (3*num)+1

    def sequence(self):
        nextNum = self.__process(self.startNum)
        counter = 1
        while nextNum != 1:
            counter +=1
            nextNum = self.__process(nextNum)
        return (self.startNum, counter)