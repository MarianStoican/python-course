
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return '%s/%s' % (self.numerator, self.denominator)

    @staticmethod
    def cmd(number1, number2):
        while number1 != number2:
            if number1 > number2:
                number1 -= number2
            else:
                number2 -= number1
        return number1

    @staticmethod
    def lcd(number1, number2):
        return (number1 * number2) / Fraction.cmd(number1, number2)

    def __add__(self, other):
        if self.denominator != other.denominator:
            numerator1 = self.numerator * other.denominator
            numerator2 = other.numerator * self.denominator
            new_numerator = numerator1 + numerator2
            new_denominator = self.denominator * other.denominator
        else:
            new_numerator = self.numerator + other.numerato
            new_denominator = self.denominator

        return Fraction(new_numerator, new_denominator)


f1 = Fraction(3, 6)
f2 = Fraction(2, 3)

f3 = f1 + f2

print(f3)
