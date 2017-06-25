import value_Global

def print_Output(x):
    print(x)
    if value_Global.output:
        value_Global.output_File.write(x + '\n')
