import os
import useful_functions as f

os.chdir(os.path.dirname(os.path.realpath(__file__)))

f.clear_console()

print(f.color_change("red","This should be red"))

