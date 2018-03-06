import os
import sys
import re

path = input("Enter path to directory: ")
if path[-1] != "/":
    path += "/"

for file in os.listdir(path):
    if " " in file:
        new_name = re.sub(" ", ".", file)
        os.rename(path + file, path + new_name)
