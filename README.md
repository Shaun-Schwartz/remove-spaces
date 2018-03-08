Simple script to replaces spaces in file names with '.'

copy remove_spaces.py, run with python3, and enter the path to the directory housing the files to be renamed

##### Flags:
```
-h,--help for help
-p, --path to specify the path to the directory housing the files to be renamed
-d, --directories to replace spaces in directory names as well as file names (default does not rename directories)
TODO -r, --recursive to recursively replace spaces in file names (and directory names if the -d flag is used)
-rc, --replacecharacter to specify what character should replace the space in file or directory names (default is .)
-cr, --charactertoreplace to specify which character should be replaced (default is space)
```

TODO: add recursive functionality
