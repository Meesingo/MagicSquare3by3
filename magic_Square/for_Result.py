import value_Calc
from verbose_Print import verbose_Print
from print_Output import print_Output

# Define show_Square(success) function
def show_Square(success):
    print_Output('\nYour magic square is:')
    print_Output('(There is only one but you can (probably) rotate and/or flip it!)\n')
    for x in success:
        print_Output(str(x))
    print_Output('\nThe sum of each line is ' + str(value_Calc.target) + '\n')

def show_Time(start, end):
    verbose_Print('\nCalculating calculation time')
    t = end - start
    print_Output('Calculation time: ' + str(format(1000 * t, '.3f')) + ' milliseconds')
