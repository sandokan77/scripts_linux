# Author: Chris Miklos
# 
# What can I be useful for?:
# FreeBSD in Linux compatibility mode is capable to run Linux applications given the 
# dependency libraries are copied from a matching architecture running a Linux.
# In order to collect these libraries one can use Linux command ldd in order to generate a
# the dependency list. Files present in the list need to be collected in a subfolder then
# copied to FreeBSD retaining their original full path. I could not find a native solution
# in Linux that was capable to copy files retaining AND creating their full path and a one 
# of functionality I could fully understand.
#
#
# TODO: an extension to parse the output of ldd would be good : DONE 
# TODO: give files root owner and group : TO_BE_CONSIDERED


import os
import sys

BINARY_FILE = '~/Projects/vscode/code' 
DEST_DIR = '~/Projects/vscode/unix'
COMMAND = "ldd " + BINARY_FILE + " | awk \'BEGIN{ORS=\" \"}$1~/^\//{print $1}$3~/^\//{print $3}\' | sed \'s/,$/" + r"\n" + r"/'"            


FILE_LIST = None

def generate_dependency_list():
    global FILE_LIST
    FILE_LIST = os.popen(COMMAND).readlines()[0].split(" ")
    
    if (FILE_LIST[-1]==''):
        FILE_LIST.pop()

def makedir(src_path_with_filename):
    print ("makedir: SOURCE_PATHWITHFILE:",src_path_with_filename)
    print("makedir DEST_DIR:",DEST_DIR)
    print("makedir amalgamated:",DEST_DIR + src_path_with_filename)

    #os.makedirs(os.path.dirname(DEST_DIR + src_path_with_filename), exist_ok=True)
    os.system('mkdir --parent '+ os.path.dirname(DEST_DIR + src_path_with_filename))

def copy_file(srcfile):
    os.system('cp ' + srcfile + ' ' + DEST_DIR + srcfile)

def copy_all_files():
    global FILE_LIST, DEST_DIR
    for f in FILE_LIST:
        print("copy_all_files processing file:",f)
        makedir(f)
        copy_file(f)

generate_dependency_list()
copy_all_files() 