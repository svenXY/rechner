import random
from time import time
import sys
from math import sqrt
from itertools import count, islice

class Rechenspiel(object):

    def __init__(self, aufgaben):
        self.alle = 0
        self.correct = 0
        self.seconds = 0
        operations = [ Addition, Substraction, Division, Multiplication ]
        op_map = [random.choice(operations) for i in range(aufgaben)]

        for op in op_map:
            r = op()
            try:
                self.seconds += r.seconds
                self.correct += r.counter
                self.alle += 1
            except AttributeError:
                break

        self.end()

    def end(self):
        print('='*80)
        print('Aufgaben insgesamt: %d\ndavon korrekt: %d\n\nDu hast insgesamt %d Sekunden gerechnet\n' % 
              (self.alle,
               self.correct,
               self.seconds)
             )

        try:
            ratio = int(self.correct*100/self.alle)
        except:
            ratio = 0

        if self.alle == 0:
            print('Du hast keine Aufgaben gerechnet.')
        elif ratio < 50:
            print('Hmm. Weniger als die Hälfte war richtig. Bleib dran, dann wird es bald besser.')
        elif ratio < 70:
            print('Gut. Deutlich mehr als die Hälfte. Bleib dran, Du kannst Dich noch steigern.')
        elif ratio < 90:
            print('Sehr gut. Du hast die meisten Aufgaben richtig berechnet.')
        elif ratio < 99:
            print('Ahhh, fast. Beinahe hättest Du alle Aufgaben richtig gehabt.  Super!')
        else:
            print('Perfekt! Alles richtig. Anscheinend bist Du bereits ein Mathe-As.')
        sys.exit(0)

class Operation(object):

    maps = { '+' : 'ADDITION',
            '-' : 'SUBTRACTION',
            '*' : 'MULTIPLICATION',
            '/' : 'DIVISION'
           }

    def __init__(self, optype=None):
        self.opsymbol = optype
        self.operation = Operation.maps[optype]

    def isPrime(self, n):
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


    def get_number(self, first, second):
        return random.randint(first, second)

    def prompt_user(self):
        now = time()
        print('='*80)
        while True:
            ui = input('\nWieviel ist\n\n%d %s %d = ' % (self.op1, self.opsymbol, self.op2))
            if ui == '':
                return None
            try:
                ui = int(ui)
            except ValueError:
                print('Das ist keine Zahl, bitte versuche es nochmal.')
                continue
            break
        seconds = int(time() - now)
        if ui == self.result:
            print( "Sehr gut. Richtig!\n\n%d %s %d = %d\n\nDu hast %d Sekunden für die Berechnung gebraucht" %
                  (self.op1, self.opsymbol, self.op2, self.result, seconds))
            self.counter = 1
        else:
            print( "Leider falsch: \n\n%d %s %d = %d\n\nDu hast %d Sekunden benötigt." %
                  (self.op1, self.opsymbol, self.op2, self.result, seconds))
            self.counter = 0
        self.seconds = seconds



class Addition(Operation):

    def __init__(self):
        super().__init__('+')
        self.op1 = self.get_number(10, 100)
        self.op2 = self.get_number(1, 100)
        self.result = self.op1 + self.op2
        self.prompt_user()

class Substraction(Operation):

    def __init__(self):
        super().__init__('-')
        self.op1 = self.get_number(10, 100)
        while True:
            self.op2 = self.get_number(6, 100)
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
        while True:
            self.op1 = self.get_number(6, 100)
            if not self.isPrime(self.op1):
                break
        while True:
            self.op2 = self.get_number(2, 100)
            if self.op1 % self.op2 == 0:
                break
        self.result = self.op1 / self.op2
        self.prompt_user()


if __name__ == "__main__":
        print('Willkommen beim Mathe Spiel')
        try:
            aufgaben = int(input('Wie viele Aufgaben möchtest Du lösen? [10] > '))
        except:
            aufgaben = 10
        print('OK, Du möchtest %d Aufgaben lösen.' % aufgaben)
        print('Du kannst das Spiel aber jederzeit mit [RETURN] beenden.\n')
        print('Fangen wir an...')
        Rechenspiel(aufgaben)




