import random
from time import time
import sys

class Operation(object):

    maps = { '+' : 'ADDITION',
            '-' : 'SUBTRACTION',
            '*' : 'MULTIPLICATION',
            '/' : 'DIVISION'
           }

    def __init__(self, optype=None):
        self.opsymbol = optype
        self.operation = Operation.maps[optype]
        

    def get_number(self, first, second):
        return random.randint(first, second)

    def prompt_user(self):
        now = time()
        print('='*80)
        print('Berechne %d %s %d' % (self.op1, self.opsymbol, self.op2))
        ui = input('Dein Ergebnis (oder Return zum Beenden): ')
        if ui:
            ui = int(ui)
        else:
            return None
        seconds = int(time() - now)
        if ui == self.result:
            print( "Richtig!\n\n %d %s %d = %d\n\nDas dauerte %d Sekunden" %
                  (self.op1, self.opsymbol, self.op2, self.result, seconds))
            self.counter = 1
        else:
            print( "Leider falsch: \n\n %d %s %d = %d\n\nDas dauerte %d Sekunden" %
                  (self.op1, self.opsymbol, self.op2, self.result, seconds))
            self.counter = 0
        self.seconds = seconds



class Addition(Operation):

    def __init__(self):
        super().__init__('+')
        self.op1 = self.get_number(0, 100)
        self.op2 = self.get_number(0, 100)
        self.result = self.op1 + self.op2
        self.prompt_user()

class Substraction(Operation):

    def __init__(self):
        super().__init__('-')
        self.op1 = self.get_number(1, 100)
        while True:
            self.op2 = self.get_number(0, 100)
            if self.op2 < self.op1:
                break
        self.result = self.op1 - self.op2
        self.prompt_user()

class Multiplication(Operation):

    def __init__(self):
        super().__init__('*')
        self.op1 = self.get_number(1, 10)
        self.op2 = self.get_number(1, 10)
        self.result = self.op1 * self.op2
        self.prompt_user()

class Division(Operation):

    def __init__(self):
        super().__init__('/')
        self.op1 = self.get_number(1, 100)
        while True:
            self.op2 = self.get_number(1, 100)
            if self.op1 % self.op2 == 0:
                break
        self.result = self.op1 / self.op2
        self.prompt_user()

def end(alle, correct, seconds):
    print('Aufgaben: %d, davon korrekt: %d in %d Sekunden' % (alle,
                                                         correct,
                                                          seconds))
    sys.exit(0)

if __name__ == "__main__":
    alle = 0
    correct = 0
    seconds = 0
    op_map = [ Addition, Substraction, Division, Multiplication ]
    while True:
        rand_item = op_map[random.randrange(len(op_map))]
        r = rand_item()
        try:
            seconds += r.seconds
            correct += r.counter
            alle += 1
        except AttributeError:
            end(alle, correct, seconds)




