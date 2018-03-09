Command-line script to rename files. Default behaviour is to replace spaces in file names with a dot. The rc and cr flags (all flags below) allow for customization of this behaviour. Additional default behaviour: directories are not renamed, and files/ directories are not renamed recursively.

copy remove_spaces.py, run with python3, and enter the path to the directory housing the files to be renamed

#### Caution:
If replacing or substituting in special characters do not use the -rc or -cr flags. Rather edit default_characters.py. The reason for this is many special characters are reserved Unix characters which may (likely) cause unexpected behaviour.

##### Flags:
```
-h, --help for help
-p, --path to specify the path to the directory housing the files to be renamed
-d, --directories to replace spaces in directory names as well as file names (default does not rename directories)
-r, --recursive to recursively replace spaces in file names (and directory names if the -d flag is used)
-rc, --replacecharacter to specify what character should replace the space in file or directory names (default is .)
-cr, --charactertoreplace to specify which character should be replaced (default is space)
```
