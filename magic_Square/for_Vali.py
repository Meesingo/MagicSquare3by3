import value_Calc
from verbose_Print import verbose_Print
from print_Output import print_Output

# Define check_Sum(numbers_Sum) function
def check_Average(numbers_Average):
    # Check if the average is integer
    # If not so, prompt the user and set flag not to continue
    # Else, continue
    if not float(numbers_Average).is_integer():
        print_Output('These numbers cannot make a 3-by-3 magic square!')
        verbose_Print('ERROR: Average not an integer!')
        return False
    else:
        return True

# Define check_Center() function
def check_Center():
    # Check if the center is one-third of the target sum
    # If not so, prompt the user and set flag not to continue
    # Else, continue
    if not 3 * value_Calc.center == value_Calc.target:
        print_Output('These numbers cannot make a 3-by-3 magic square!')
        verbose_Print('ERROR: No proper center!')
        return False
    else:
        return True
