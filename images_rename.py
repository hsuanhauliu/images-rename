import argparse
import random
from os import listdir, rename, chdir
from os.path import isfile, isdir, join

def main():
    args = parse_inputs()
    dir_name = args.dir_path
    randomization = True
    filename = args.filename

    if args.disable == True:
        print(">>> Randomization disabled")
        randomization = False
    elif args.disable == False:
        print(">>> Randomization enabled")

    if not_a_directory(dir_name):
        print(">>> Error: not a directory")
        raise ValueError

    # change directory
    chdir(dir_name)

    # return a list of file names in the currect directory
    myFiles = grab_files()

    # start renaming files
    rename_files(myFiles, filename, randomization)

    return

def rename_files(file_list, new_name, randomize):
    """
    file_list: list of filenames
    name: name of the files that we will use for renaming
    randomize: a flag indicating whether to add randomized number to prevent overwriting
    """

    counter = 0
    randomized_name = ""

    if randomize:
        randomized_name = "_" + str(random.randint(0, 1000))

    for filename in file_list:
        counter += 1
        extension = get_extension(filename)
        new_filename = new_name + str(counter) + randomized_name + extension
        rename(filename, new_filename)
    print(">>> Renamed", counter, "files")


def get_extension(file_name):
    """
    Return the extension of the file_name.
    """
    return "." + file_name.split(".")[-1]

def grab_files():
    """
    Return a list of unhidden files with extensions.
    """
    return [f for f in listdir(".") if isfile(f) and f[0] != "." and len(f.split(".")) > 1]

def not_a_directory(dir_name):
    """
    Check if it is a directory.
    """
    return not isdir(dir_name)

def parse_inputs():
    """
    Parse user inputs.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dir_path", type=str, help="enter directory path")
    parser.add_argument("-d", "--disable", action='store_true',
            help="disable adding randomized name in file names")
    parser.add_argument("-f", "--filename", type=str, default="file",
            help="input a file name that will be used for the files")

    return parser.parse_args()

if __name__ == "__main__":
    main()
