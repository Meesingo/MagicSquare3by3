import value_Calc
from print_Output import print_Output

# Define show_Square(success) function
def show_Square(success):
    print_Output('\nYour magic square is:')
    print_Output('(There is only one but you can (probably) rotate and/or flip it!)\n')
    for x in success:
        print_Output(str(x))
    print_Output('\nThe sum of each line is ' + str(target) + '\n')

def show_Time():
    verbose_Print('\nCalculating calculation time')
    t = calc_Time(start, end)
    print_Output('Calculation time: ' + str(format(1000 * t, '.3f')) + ' milliseconds')

def calc_Time(start, end):
    return end - start
