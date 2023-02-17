class SquareSequence:
    def __init__(self):
        self.a, self.b, self.c = self.get_coefficients().values()
        self.d = self.get_discriminant()

    # !!! FOR TESTING ONLY !!!
    # def __init__(self, a, b, c):
    #     self.a = a
    #     self.b = b
    #     self.c = c
    #     self.d = self.get_discriminant()

    def get_coefficients(self):
        is_valid_numbers = False
        while not is_valid_numbers:
            a = input('a: ')
            b = input('b: ')
            c = input('c: ')

            is_valid_numbers = self.check_input_validity(a, b, c)

        return {'a': float(a), 'b': float(b), 'c': float(c)}

    def check_input_validity(self, a, b, c):
        is_valid_numbers = False

        for s in [a, b, c]:
            for i in range(len(s)):
                if s[i].isdigit() or (s[i] == '.' and s.count('.') == 1) or (s[i] == '-' and s.count('-') == 1) or (s[i] == 'e' and s.count('e') == 1):
                    is_valid_numbers = True
                else:
                    is_valid_numbers = False
                    return is_valid_numbers

        return is_valid_numbers

    def print_equation(self):
        equation = ''
        eq1 = f'{self.a}x² ' if self.a > 0 else f'{self.a}x² '
        eq2 = f'+ {self.b}x ' if self.b >= 0 else f'- {-self.b}x '
        eq3 = f'+ {self.c} ' if self.c > 0 else f'- {-self.c} '
        equation = eq1 + eq2 + eq3 + '= 0'

        print(equation)

    def sequance_handler(self):
        x = self.linear_x() if self.a == 0 else self.squared_x()
        return x

    def linear_x(self):
        if self.b != 0:
            return {'x': self.c / -self.b}
        else:
            return '[!] - ZeroDivision'

    def get_discriminant(self):
        return self.b**2 - 4 * self.a * self.c

    def squared_x(self):
        print('D =', self.d)
        if self.d < 0:
            print('[no roots]')
            return {'x1': None, 'x2': None}

        elif self.d == 0:
            print('[single root]')
            print('root_d = 0')
            x1 = -self.b / (2 * self.a)
            x2 = -self.b / (2 * self.a)
            return {'x1': x1, 'x2': x2}

        elif self.d > 0:
            print('[two roots]')
            root_d = self.d ** 0.5
            print(f'{round(root_d, 2) = }')

            x1 = (-self.b + root_d) / 2 * self.a
            x2 = (-self.b - root_d) / 2 * self.a

            return {'x1': x1, 'x2': x2}
