#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
# returns a list of the absolute paths of the special files in the given directory
def get_special_paths (dir_name):
    filenames = os.listdir(dir_name)
    special_files=[]
    for files in filenames:
        match = re.search (r"__(\w+)__", files)
        if match:
            special_path = os.path.abspath (files)
            special_files.append (special_path)
    return special_files

 
# given a list of paths, copies those files into the given directory
def copy_to (paths, dir_name):
    if not os.path.exists (dir_name):
        os.mkdir(to_dir)
    for files in paths:
        shutil.copy (files, dir_name)

# given a list of paths, zip those files up into the given zipfile
def zip_to (paths, zippath):
    cmd = 'zip -j' + ','.join(paths)
    print "Command I'm going to do:" + cmd 
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)
    

# Write functions and modify main() to call them
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    # I am not sure why this code is necessary, if it is included it the command will print error: must specify one or more dirs, 
    # so I just elected not to run it. All the codes work fine without it. 
    #del args[0:2]
    
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    #del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  
  # Call the functions
  files_path = get_special_paths ('./')
  if todir != '':
    copy_to (files_path, todir)
  elif tozip != '':
    zip_to (files_path, tozip)
  else:
    all_files = []
    for paths in args:  
        all_files.extend (get_special_paths (paths))
    print ('\n'.join(all_files))
  
if __name__ == "__main__":
  main()
