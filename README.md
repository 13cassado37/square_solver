# square_solver

Simple square sequence solver.
Enter coefficients (a, b, and c) and you will see the discriminant and roots of equation.

[sequanse.py]
class SquareSequence
    a - first coefficient
    b - second coefficient
    c - third coefficient
_____________________
    __init__() - initializes coefficients
    get_coefficients() - get strings of coefficients checks if its valid and returns coefficients dictionary
    check_input_validity() - in loop checks every symbol of string
    print_equation() - just prints the equation
    sequance_handler() - checks its quadratic(a ==0) or linear equation(a != 0)
    linear_x() - returns x for linear (c/-b)
    get_discriminant() - returns the discriminant
    squared_x() - returns x for squared equation

[main.py]
gets coefficients in loop while cont != 's'
