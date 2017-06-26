# This program (supposedly) solves a 3-by-3 magic square
import sys
import value_Global
from verbose_Print import verbose_Print
from print_Output import print_Output
from calculation import calculation

print()
# Try defining arguments
# If there is no argument, prompt the user that s/he can input one, and continue
actions = sys.argv[1:]
# Initiate necessary values
no_Help = True
valid_Argument = True
# If there are arguments, proceed with arguments
if actions == []:
    print('You can specify arguments on this little program!')
    print('Use \'python', sys.argv[0], '-h\' to see more!\n')
else:
    if ('-h' in actions) or ('--help' in actions):
        no_Help = False
        print_Output('This program (supposedly) solves a 3-by-3 magic square\n\n-h OR --help\tShow this help section\n-v OR --verbose\tShow more output to see how the program runs\n-o OR --output\tPrint all console outputs to a file named \'Magic_Square_v2.log.txt\'\n\t\t(Note that all of the data in that file, if exist, will be cleared)\n')
    else:
        if ('-v' in actions) or ('--verbose' in actions):
            value_Global.verbose = True
            actions = [x for x in actions if x not in ['-v', '--verbose']]
        if ('-o' in actions) or ('--output' in actions):
            value_Global.output = True
            value_Global.output_File = open('Magic_Square_v2.log.txt', 'w')
            actions = [x for x in actions if x not in ['-o', '--output']]
        if actions != []:
            print('Arguments invalid!')
            valid_Argument = False
            print('Use \'python', sys.argv[0], '-h\' to see more!\n')
verbose_Print('Calculation is initiating...\n\n')
if no_Help and valid_Argument:
    calculation()
