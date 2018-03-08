import os
import sys
import re
import argparse

parser = argparse.ArgumentParser(description='Replace spaces in file names')
parser.add_argument('-p', '--path', type=str, help='Specify the path to the directory housing the files to be renamed')
parser.add_argument('-d', '--directories', action='store_true', default=False, help='Replace spaces in directory names as well as file names')
parser.add_argument('-r', '--recursive', action='store_true', default=False, help='Recursively replace spaces in file names (and directory names if the -d flag is used)')
parser.add_argument('-rc', '--replacecharacter', type=str, default='.', help='Specify what character should replace the space in file or directory names (default is .)')
parser.add_argument('-cr', '--charactertoreplace', type=str, default=' ', help='Specify which character should be replaced (default is space)')
args = parser.parse_args()

d = args.directories
r = args.recursive
rc = args.replacecharacter
cr = args.charactertoreplace

if args.path == None:
    path = input("Enter path to directory: ")
else:
    path = args.path

if path[-1] != "/": path += "/"

if args.recursive:
    for folder, subdir, files in os.walk(path):
        if os.path.isdir(folder):
            print('This is a directory {}'.format(folder))
        for file in files:
            if os.path.isfile(os.path.join(folder + file)):
                print('This is a file {}'.format(folder + file))

else:
    if args.directories:
        for file in os.listdir(path):
            if args.charactertoreplace in file:
                new_name = re.sub(args.charactertoreplace, args.replacecharacter, file)
                print('File to rename: {}'.format(path + file))
                try:
                    os.rename(path + file, path + new_name)
                    print('File renamed to: {}'.format(path + new_name))
                except:
                    print('Couldn\'t rename file: {}'.format(path + file))
    else:
        for file in os.listdir(path):
            if args.charactertoreplace in file and os.path.isfile(os.path.join(path, file)):
                new_name = re.sub(args.charactertoreplace, args.replacecharacter, file)
                print('File to rename: {}'.format(path + file))
                try:
                    os.rename(path + file, path + new_name)
                    print('File renamed to: {}'.format(path + new_name))
                except:
                    print('Couldn\'t rename file')
                    pass
