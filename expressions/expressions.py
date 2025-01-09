from numbers import Number as Num


class Expression:


    def __init__(self, *operands):
        self.operands = operands
    
    def __add__(self, other):
        if isinstance(other, Expression):
            return Add(self, other)
        elif isinstance(other, Num):
            return self + Number(other)

    def __radd__(self, other):
        if isinstance(self, Expression):
            return Add(other, self)
        elif isinstance(self, Num):
            return Number(self) + other
    
    def __sub__(self, other):
        if isinstance(other, Expression):
            return Sub(self, other)
        elif isinstance(other, Num):
            return self - Number(other)
    
    def __rsub__(self, other):
        if isinstance(self, Expression):
            return Sub(other, self)
        elif isinstance(self, Num):
            return Number(self) - other
    
    def __mul__(self, other):
        if isinstance(other, Expression):
            return Mul(self, other)
        elif isinstance(other, Num):
            return self * Number(other)
    
    def __rmul__(self, other):
        if isinstance(self, Expression):
            return Mul(other, self)
        elif isinstance(self, Num):
            return Number(self) * other
    
    def __truediv__(self, other):
        if isinstance(other, Expression):
            return Div(self, other)
        elif isinstance(other, Num):
            return self / Number(other)
    
    def __rtruediv__(self, other):
        if isinstance(self, Expression):
            return Div(other, self)
        elif isinstance(self, Num):
            return Number(self) / other
    
    def __pow__(self, other):
        if isinstance(other, Expression):
            return Pow(self, other)
        elif isinstance(other, Num):
            return self ** Number(other)

    def __rpow__(self, other):
        if isinstance(self, Expression):
            return Pow(self, other)
        elif isinstance(self, Num):
            return Number(self) ** other

class Operator(Expression):

    def __repr__(self):
        return type(self).__name__ + repr(self.operands)
    
    def __str__(self):
        strlist = []
        for operand in self.operands:
            if isinstance(operand, Operator) and \
              operand.precedence < self.precedence:
                strlist.append(f"({str(operand)})")
                print(strlist)
            else:
                strlist.append(str(operand))
                print(strlist)
        return f" {self.symbol} ".join(strlist)

class Add(Operator):

    symbol = "+"
    precedence = 1

class Mul(Operator):

    symbol = "*"
    precedence = 2

class Sub(Operator):

    symbol = "-"
    precedence = 1

class Div(Operator):

    symbol = "/"
    precedence = 2

class Pow(Operator):

    symbol = "^"
    precedence = 3

class Terminal(Expression):

    def __init__(self, value, operands=()):
        self.precedence = 4
        self.value = value
        super().__init__(operands)
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return repr(self.value)


class Number(Terminal):

    def __init__(self, value, operands=()):
        super().__init__(value, operands)
        if not isinstance(value, Num):
            return NotImplemented

class Symbol(Terminal):

    def __init__(self, value, operands=()):
        super().__init__(value, operands)
        if not isinstance(value, str):
            return NotImplemented