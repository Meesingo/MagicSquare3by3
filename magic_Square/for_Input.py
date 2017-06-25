import value_Global
import value_Calc
from verbose_Print import verbose_Print
from print_Output import print_Output

# Define get_number(numbers) function
def get_number(numbers):
    # Initiate iteration variable
    i = 1
    # Run the following 9 times
    while i < 10:
        # Prompt for and collect input
        x = 'Input your integer ' + str(i) + ' (Leave blank for ' + str(i) + '): '
        print(x, end = '')
        user_Input = input('')
        if value_Global.output:
            value_Global.output_File.write(x + user_Input + '\n')
        # See if user has input
        # If not, use the defalut and ask for the next input
        if user_Input == '':
            i += 1
            verbose_Print('User has not chosen input. Using default value\n')
        # If the user does have an input, check if the input is legit
        else:
            # Check if the input is legit by trying to convert it into an integer
            try:
                input_Integer = int(user_Input)
            # If ValueError exception is caught, prompt the user that the value is not legit
            except ValueError:
                print_Output('This is not a legit value!')
                verbose_Print('ERROR: Cannot parse integer!')
                print_Output('')
            # Only proceed to next number if this one is legit
            else:
                numbers[i - 1] = input_Integer
                i += 1
                verbose_Print('Integer parsing successful, onto next integer\n')
    return numbers
