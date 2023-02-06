from day10.tools import Animal


class Dog(Animal):

    def eat(self):
        super().eat()
        print("吃完骨头瑶瑶头...")


aaa = Dog('小明')
aaa.eat()
