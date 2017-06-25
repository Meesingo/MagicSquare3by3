# This program (supposedly) solves a 3-by-3 magic square
import time
from value_Global import output as output
from print_Output import print_Output

# Define main() function
def main():
    print('\nThis program (supposedly) solves a 3-by-3 magic square\n\nverbose\t\tShow more output to see how the program runs\noutput\t\tPrint all console outputs to a file named \'Magic_Square_v2.log.txt\'\n\t\t(Note that all of the data in that file, if exist, will be cleared)\n')
    # Globalize necessary values
    global verbose
    # Initiate necessary values
    verbose = False
    help_File = False
    # Prompt user for arguments
    verbose_Input = input('Do you want verbose? (\'y\' for yes and everything else for no): ')
    output_Input = input('Do you want output? (\'y\' for yes and everything else for no): ')
    # If there are arguments, proceed with arguments
    if verbose_Input in ['y', 'Y', '\'y\'', '\'Y\'', 'yes', 'Yes']:
        verbose = True
    if output_Input in ['y', 'Y', '\'y\'', '\'Y\'', 'yes', 'Yes']:
        value_Global.output = True
    if verbose:
        print_Output('Calculation is initiating...\n\n')
    calculation()

# Define calculation() function
def calculation():
    print_Output('')
    # Initiate necessary values
    numbers = list(range(1,10))
    assemble_Success = False
    # Ask for input using get_number(numbers) function
    numbers = get_number(numbers)
    # Start calculation
    if verbose:
        print_Output('\nCalculation starting, recording start time\n\n')
    start = time.time()
    # Sort the numbers
    if verbose:
        print_Output('Sorting numbers')
    numbers.sort()
    # Calculate the sum and average and check for the legitimacy of average using check_Average(numbers_Average)
    if verbose:
        print_Output('Calculating the target sum of each row and column')
    numbers_Average = sum(numbers) / 3
    # Integerize the average
    global target
    target = int(numbers_Average)
    # Set the central number at the center and remove it from the number list
    if verbose:
        print_Output('Determining the central number')
    global center
    center = numbers[4]
    del numbers[4]
    # Only continue if the average and the center are legit
    if verbose:
        print_Output('Checking the legitimacy of the target sum and central number\n\n')
    if check_Average(numbers_Average) and check_Center():
        if verbose:
            print_Output('Check success, continue onto iteration of first line\nThe target sum is ' + str(target) + ' and the central number is ' + str(center) + '\n')
        # Assemble the first line using assemble_Line1(numbers)
        success_Line1 = assemble_Line1(numbers)
        # Continue if there is a legit first line
        if success_Line1 == []:
            print_Output('These numbers cannot make a 3-by-3 magic square!')
            if verbose:
                print_Output('ERROR: No successful first lines!')
        else:
            if verbose:
                print_Output('Found ' + str(len(success_Line1)) + ' first lines: ' + str([x[0] for x in success_Line1]) + '\n\n')
            # Assemble the third line using assemble_Line3(success_Line1)
            success_Line3 = assemble_Line3(success_Line1)
            # Continue if there is a legit third line
            if success_Line3 == []:
                print_Output('These numbers cannot make a 3-by-3 magic square!')
                if verbose:
                    print_Output('ERROR: No successful third lines!')
            else:
                if verbose:
                    print_Output('Found ' + str(len(success_Line3)) + ' first-third-lines combinations: ' + str([x[:2] for x in success_Line3]) + '\n\n')
                # Assemble the whole square using assemble(success_Line3)
                success = assemble(success_Line3)
                # Continue if there is a legit second line
                if success == []:
                    print_Output('These numbers cannot make a 3-by-3 magic square!')
                    if verbose:
                        print_Output('ERROR: No successful second lines!')
                else:
                    assemble_Success = True
    else:
        if verbose:
            print_Output('\nCheck failed, terminating calculation\n')
    if verbose:
        print_Output('\nCalculation ending, recording end time\n')
    end = time.time()
    # If calculation successful, print the answer using show_Square(success)
    if assemble_Success:
        show_Square(success)
    if verbose:
        print_Output('\nCalculating calculation time')
    t = end - start
    print_Output('Calculation time: ' + str(format(1000 * t, '.3f')) + ' milliseconds')
    input('\n\nPress enter key to exit...')

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
            if verbose:
                print_Output('User has not chosen input. Using default value\n')
        # If the user does have an input, check if the input is legit
        else:
            # Check if the input is legit by trying to convert it into an integer
            try:
                input_Integer = int(user_Input)
            # If ValueError exception is caught, prompt the user that the value is not legit
            except ValueError:
                print_Output('This is not a legit value!')
                if verbose:
                    print_Output('ERROR: Cannot parse integer!')
                print_Output('')
            # Only proceed to next number if this one is legit
            else:
                numbers[i - 1] = input_Integer
                i += 1
                if verbose:
                    print_Output('Integer parsing successful, onto next integer\n')
    return numbers

# Define check_Sum(numbers_Sum) function
def check_Average(numbers_Average):
    # Check if the average is integer
    # If not so, prompt the user and set flag not to continue
    # Else, continue
    if not float(numbers_Average).is_integer():
        print_Output('These numbers cannot make a 3-by-3 magic square!')
        if verbose:
            print_Output('ERROR: Average not an integer!')
        return False
    else:
        return True

# Define check_Center() function
def check_Center():
    # Check if the center is one-third of the target sum
    # If not so, prompt the user and set flag not to continue
    # Else, continue
    if not 3 * center == target:
        print_Output('These numbers cannot make a 3-by-3 magic square!')
        if verbose:
            print_Output('ERROR: No proper center!')
        return False
    else:
        return True

# Define assemble_Line1(numbers) function
def assemble_Line1(numbers):
    # Initiate necessary values
    row1 = []
    # Choice of first number is the first half of the set of numbers
    numbers1 = numbers[:4]
    if verbose:
        print_Output('The number pool of the first number is ' + str(numbers1))
    # Iterate through the choices for the first number
    for choice1 in numbers1:
        if verbose:
            print_Output('Selecting the first number: ' + str(choice1))
        # Reset the choice of the second number to the whole set of numbers
        numbers2 = numbers[:]
        # Remove the first number
        numbers2.remove(choice1)
        if verbose:
            print_Output('The number pool of the second number is ' + str(numbers2))
        # Iterate through the choices for the second number
        for choice2 in numbers2:
            if verbose:
                print_Output('Selecting the second number: ' + str(choice2))
            # Reset the choice of the third number to the set of numbers2
            numbers3 = numbers2[:]
            # Remove the second number
            numbers3.remove(choice2)
            if verbose:
                print_Output('The number pool of the third number is ' + str(numbers3))
            # Calculate the third number
            choice3 = target - choice1 - choice2
            if verbose:
                print_Output('But the third number has to be ' + str(choice3))
            # Check if the calculated is in the selectible pool
            # If so, append the answer to the answer pool
            # Else, continue
            if choice3 in numbers3:
                numbers3.remove(choice3)
                row1.append([[choice1, choice2, choice3], numbers3])
                if verbose:
                    print_Output('Found one legit first line ' + str([choice1, choice2, choice3]) + ', with numbers left: ' + str(numbers3) + '\n')
            else:
                if verbose:
                    print_Output(str(choice3) + ' is not in the number pool!\nJumping back into the numbers pool\n')
    return row1

# Define assemble_Line3(success_Line1) function
def assemble_Line3(success_Line1):
    # Initiate necessary values
    row3 = []
    # Iterate through the sucessful first lines
    for line1 in success_Line1:
        if verbose:
            print_Output('Selecting first line: ' + str(line1[0]))
        # Assemble third line using the first one
        line3 = list(map(lambda x: target - center - x, line1[0][::-1]))
        if verbose:
            print_Output('The corresponding third line is ' + str(line3))
        # Get the remaining numbers
        numbers_Line3 = line1[1]
        if verbose:
            print_Output('But the number pool for the third line is ' + str(numbers_Line3))
        # Initiate check variable
        check_Line3 = True
        # Check if the three values in the third line are in the numbers left
        for z in line3:
            if z in numbers_Line3:
                numbers_Line3.remove(z)
                if verbose:
                    print_Output(str(z) + ' is in the number pool! Numbers left: ' + str(numbers_Line3))
            else:
                check_Line3 = False
                if verbose:
                    print_Output(str(z) + ' is not in the number pool!')
                break
        # Record answer only if the third line is legit
        if check_Line3 == True:
            row3.append([line1[0], line3, numbers_Line3])
            if verbose:
                print_Output('Found one legit third line ' + str(line3) + ', with first line ' + str(line1[0]) + ' and numbers left: ' + str(numbers_Line3) + '\n')
        else:
            if verbose:
                print_Output('Negative legitimacy\nChecking next first line\n')
    return row3

# Define assemble(success_Line3) function
def assemble(success_Line3):
    # Initiate necessary values
    row2 = []
    # Iterate through the successful third lines
    for line3 in success_Line3:
        if verbose:
            print_Output('Selecting first line ' + str(line3[0]) + ' with third line ' + str(line3[1]))
        choice1 = target - line3[0][0] - line3[1][0]
        if verbose:
            print_Output('The corresponding first number is ' + str(choice1))
        sum_Line2 = sum(line3[2])
        if verbose:
            print_Output('But the number pool for the first number is ' + str(line3[2]))
        # Proceed if the remaining adds up for second row, first column, and third column
        if (sum_Line2 + center == target):
            if verbose:
                print_Output('The second line sums up to the target sum')
            if (choice1 in line3[2]):
                if (sum_Line2 - choice1 + line3[0][2] + line3[1][2] == target):
                    answer = [line3[0], [choice1, center, sum_Line2 - choice1], line3[1]]
                    if verbose:
                        print_Output('Found the answer: ' + str(answer) + '\n')
                    return answer
                else:
                    if verbose:
                        print_Output('The third column does not sum up to the target sum\nChecking next combination\n')
            else:
                if verbose:
                    print_Output(str(choice1) + ' is not in the number pool!\nChecking next combination\n')
        else:
            if verbose:
                print_Output('The second line does not sum up to the target sum\nChecking next combination\n')

# Define show_Square(success) function
def show_Square(success):
    print_Output('\nYour magic square is:')
    print_Output('(There is only one but you can (probably) rotate and/or flip it!)\n')
    for x in success:
        print_Output(str(x))
    print_Output('\nThe sum of each line is ' + str(target) + '\n')

# Execute the main function
main()
