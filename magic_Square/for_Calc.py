import value_Global
import value_Calc
from verbose_Print import verbose_Print
from print_Output import print_Output

def calc(numbers):
    verbose_Print('Check success, continue onto iteration of first line\nThe target sum is ' + str(value_Calc.target) + ' and the central number is ' + str(value_Calc.center) + '\n')
    # Assemble the first line using assemble_Line1(numbers)
    success_Line1 = assemble_Line1(numbers)
    # Continue if there is a legit first line
    if success_Line1 == []:
        print_Output('These numbers cannot make a 3-by-3 magic square!')
        verbose_Print('ERROR: No successful first lines!')
        return False
    else:
        verbose_Print('Found ' + str(len(success_Line1)) + ' first lines: ' + str([x[0] for x in success_Line1]) + '\n\n')
        # Assemble the third line using assemble_Line3(success_Line1)
        success_Line3 = assemble_Line3(success_Line1)
        # Continue if there is a legit third line
        if success_Line3 == []:
            print_Output('These numbers cannot make a 3-by-3 magic square!')
            verbose_Print('ERROR: No successful third lines!')
            return False
        else:
            verbose_Print('Found ' + str(len(success_Line3)) + ' first-third-lines combinations: ' + str([x[:2] for x in success_Line3]) + '\n\n')
            # Assemble the whole square using assemble(success_Line3)
            success = assemble(success_Line3)
            # Continue if there is a legit second line
            if success == []:
                print_Output('These numbers cannot make a 3-by-3 magic square!')
                verbose_Print('ERROR: No successful second lines!')
                return False
            else:
                verbose_Print('\nCalculation successful\n')
                return success

# Define assemble_Line1(numbers) function
def assemble_Line1(numbers):
    # Initiate necessary values
    row1 = []
    # Choice of first number is the first half of the set of numbers
    if value_Global.allsol:
        numbers1 = numbers[:]
    else:
        numbers1 = numbers[:4]
    verbose_Print('The number pool of the first number is ' + str(numbers1))
    # Iterate through the choices for the first number
    for choice1 in numbers1:
        verbose_Print('Selecting the first number: ' + str(choice1))
        # Reset the choice of the second number to the whole set of numbers
        numbers2 = numbers[:]
        # Remove the first number
        numbers2.remove(choice1)
        verbose_Print('The number pool of the second number is ' + str(numbers2))
        # Iterate through the choices for the second number
        for choice2 in numbers2:
            verbose_Print('Selecting the second number: ' + str(choice2))
            # Reset the choice of the third number to the set of numbers2
            numbers3 = numbers2[:]
            # Remove the second number
            numbers3.remove(choice2)
            verbose_Print('The number pool of the third number is ' + str(numbers3))
            # Calculate the third number
            choice3 = value_Calc.target - choice1 - choice2
            verbose_Print('But the third number has to be ' + str(choice3))
            # Check if the calculated is in the selectible pool
            # If so, append the answer to the answer pool
            # Else, continue
            if choice3 in numbers3:
                numbers3.remove(choice3)
                row1.append([[choice1, choice2, choice3], numbers3])
                verbose_Print('Found one legit first line ' + str([choice1, choice2, choice3]) + ', with numbers left: ' + str(numbers3) + '\n')
            else:
                verbose_Print(str(choice3) + ' is not in the number pool!\nJumping back into the numbers pool\n')
    return row1

# Define assemble_Line3(success_Line1) function
def assemble_Line3(success_Line1):
    # Initiate necessary values
    row3 = []
    # Iterate through the sucessful first lines
    for line1 in success_Line1:
        verbose_Print('Selecting first line: ' + str(line1[0]))
        # Assemble third line using the first one
        line3 = list(map(lambda x: value_Calc.target - value_Calc.center - x, line1[0][::-1]))
        verbose_Print('The corresponding third line is ' + str(line3))
        # Get the remaining numbers
        numbers_Line3 = line1[1]
        verbose_Print('But the number pool for the third line is ' + str(numbers_Line3))
        # Initiate check variable
        check_Line3 = True
        # Check if the three values in the third line are in the numbers left
        for z in line3:
            if z in numbers_Line3:
                numbers_Line3.remove(z)
                verbose_Print(str(z) + ' is in the number pool! Numbers left: ' + str(numbers_Line3))
            else:
                check_Line3 = False
                verbose_Print(str(z) + ' is not in the number pool!')
                break
        # Record answer only if the third line is legit
        if check_Line3 == True:
            row3.append([line1[0], line3, numbers_Line3])
            verbose_Print('Found one legit third line ' + str(line3) + ', with first line ' + str(line1[0]) + ' and numbers left: ' + str(numbers_Line3) + '\n')
        else:
            verbose_Print('Negative legitimacy\nChecking next first line\n')
    return row3

# Define assemble(success_Line3) function
def assemble(success_Line3):
    # Initiate necessary values
    if value_Global.allsol:
        row2 = []
    # Iterate through the successful third lines
    for line3 in success_Line3:
        verbose_Print('Selecting first line ' + str(line3[0]) + ' with third line ' + str(line3[1]))
        choice1 = value_Calc.target - line3[0][0] - line3[1][0]
        verbose_Print('The corresponding first number is ' + str(choice1))
        sum_Line2 = sum(line3[2])
        verbose_Print('But the number pool for the first number is ' + str(line3[2]))
        # Proceed if the remaining adds up for second row, first column, and third column
        if (sum_Line2 + value_Calc.center == value_Calc.target):
            verbose_Print('The second line sums up to the target sum')
            if (choice1 in line3[2]):
                if (sum_Line2 - choice1 + line3[0][2] + line3[1][2] == value_Calc.target):
                    answer = [line3[0], [choice1, value_Calc.center, sum_Line2 - choice1], line3[1]]
                    verbose_Print('Found the answer: ' + str(answer) + '\n')
                    if value_Global.allsol:
                        row2.append(answer)
                    else:
                        return answer
                else:
                    verbose_Print('The third column does not sum up to the target sum\nChecking next combination\n')
            else:
                verbose_Print(str(choice1) + ' is not in the number pool!\nChecking next combination\n')
        else:
            verbose_Print('The second line does not sum up to the target sum\nChecking next combination\n')
    return row2
