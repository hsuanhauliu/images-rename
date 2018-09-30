# Images Rename
A simple script created for renaming files in a directory in a consistent manner. It renames files inside of the specified directory with a new name followed by a number, which increment by one starting from 1 for every file. A random number is generated each time the script is executed, and is then being appended to the end of the filename.

## Use Case
Howard downloaded a ton of image data for training his machine learning model but too lazy to rename them one by one.

## Getting started

### Installing
```
git clone https://github.com/hsuanhauliu/images-rename.git
```

### Execution
```
python3 images-rename.py <directory> [-f filename] [-d]
```

- directory: the full path of the directory that contains the files you want to rename.
- -f: optional parameter to set a name you want to use for renaming. By default, the name "file" would be used.
- -d: disable default randomization in the naming.


### Notes
- The script will only rename unhidden files (files with no "." at the beginning of their names). It will also ignore folders and files with no extension.
- The randomization feature was added so that files won't be overwritten or deleted if one executes the program more than once in a row.

## Screenshot
![screenshot](https://github.com/hsuanhauliu/images-rename/blob/master/screenshots/demo1.jpg "demo1")
![screenshot](https://github.com/hsuanhauliu/images-rename/blob/master/screenshots/demo2.jpg "demo2")
