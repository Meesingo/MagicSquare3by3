# This program (supposedly) solves a 3-by-3 magic square
import value_Global
from verbose_Print import verbose_Print
from print_Output import print_Output
from calculation import calculation

print('This program (supposedly) solves a 3-by-3 magic square\n\nverbose\tShow more output to see how the program runs\noutput\tPrint all console outputs to a file named \'Magic_Square_v2.log.txt\'\n\t(Note that all of the data in that file, if exist, will be cleared)\nallsol\tPrint all solutions, with duplicates\n')
# Initiate necessary values
help_File = False
# Prompt user for arguments
verbose_Input = input('Do you want verbose? (\'y\' for yes and everything else for no): ')
output_Input = input('Do you want output? (\'y\' for yes and everything else for no): ')
complete_Input = input('Do you want all solutions? (\'y\' for yes and everything else for no): ')
# If there are arguments, proceed with arguments
if verbose_Input in ['y', 'Y', '\'y\'', '\'Y\'', 'yes', 'Yes']:
    value_Global.verbose = True
if output_Input in ['y', 'Y', '\'y\'', '\'Y\'', 'yes', 'Yes']:
    value_Global.output = True
    value_Global.output_File = open('Magic_Square_v2.log.txt', 'w')
if complete_Input in ['y', 'Y', '\'y\'', '\'Y\'', 'yes', 'Yes']:
    value_Global.allsol = True
verbose_Print('Calculation is initiating...\n\n')
calculation()
