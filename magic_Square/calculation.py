import time
import value_Global
import value_Calc
import for_Input
import for_Vali
import for_Calc
import for_Result
from verbose_Print import verbose_Print
from print_Output import print_Output

# Define calculation() function
def calculation():
    print_Output('')
    # Initiate necessary values
    numbers = list(range(1,10))
    # Ask for input using get_number(numbers) function
    numbers = for_Input.get_number(numbers)
    # Start calculation
    verbose_Print('\nCalculation starting, recording start time\n\n')
    start = time.time()
    # Sort the numbers
    verbose_Print('Sorting numbers')
    numbers.sort()
    # Calculate the average, integerize it, and check for the legitimacy of average using check_Average(numbers_Average)
    verbose_Print('Calculating the target sum of each row and column')
    numbers_Average = sum(numbers) / 3
    value_Calc.target = int(numbers_Average)
    # Set the central number at the center and remove it from the number list
    verbose_Print('Determining the central number')
    value_Calc.center = numbers[4]
    del numbers[4]
    # Only continue if the average and the center are legit
    verbose_Print('Checking the legitimacy of the target sum and central number\n\n')
    if for_Vali.check_Average(numbers_Average) and for_Vali.check_Center():
        success = for_Calc.calc(numbers)
    else:
        verbose_Print('\nCheck failed, terminating calculation\n')
    verbose_Print('\nCalculation ending, recording end time\n')
    end = time.time()
    # If calculation successful, print the answer using show_Square(success)
    if success != False:
        for_Result.show_Square(success)
    for_Result.show_Time(start, end)
    input('\n\nPress enter key to exit...')
