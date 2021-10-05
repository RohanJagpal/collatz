class Collatz:
    def __init__(self, startNum: float) -> None:
        self.startNum = startNum
    
    def __isEven(self, num: float) -> bool:
        return num%2 == 0

    def __process(self, num: float) -> int:
        if self.__isEven(num):
            return num/2
        return (3*num)+1

    def sequence(self):
        start = self.startNum
        print(f"\n\n{start}\n")
        nextNum = self.__process(start)
        counter = 1
        while nextNum != 1:
            counter +=1
            print(nextNum)
            nextNum = self.__process(nextNum)
        print(1.0)
        print(f"\n===RESULT===\nInitial number: {str(start)}\nTrials to complete: {counter}\n===FINISHED===")