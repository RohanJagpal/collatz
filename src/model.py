class Collatts:
    def __init__(self, startNum: int) -> None:
        self.startNum = startNum
    
    def __isEven(self, num: int) -> bool:
        return num%2 == 0

    def __process(self, num: int) -> int:
        if self.__isEven(num):
            return num/2
        return (3*num)+1

    def play(self):
        start = self.startNum
        print(f"\n\n{start}")
        nextNum = self.__process(start)
        while nextNum != 1:
            print(nextNum)
            nextNum = self.__process(nextNum)
        print(1)

game = Collatts(float(eval(input())))
game.play()
