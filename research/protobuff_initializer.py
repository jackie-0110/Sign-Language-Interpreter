import os
import sys
arguments = sys.argv
directory = arguments[1]
protocpath = arguments[2]
for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system(protocpath+" "+directory+"/"+file+" --python_out=.")