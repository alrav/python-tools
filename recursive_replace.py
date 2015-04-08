#!/usr/bin/env python
"""
    RecursiveReplace
    ~~~~~~~~~~~~~~~~
    Performs a recursive directory replace for a simple string
"""

import os
import sys

def main():
    if len(sys.argv) < 4:
        sys.exit('Insufficient command line arguments')
    
    find = sys.argv[1]
    replace = sys.argv[2]
    extension = sys.argv[3]

    recursiveReplace = RecursiveReplace()
    count = recursiveReplace.replace(find, replace, os.getcwd(), extension)
    
    print str(count) + " occurences replaced"


class RecursiveReplace():

    ignoredDirectories = ['vendor']
    
    def replace(self, find, replace, rootDirectory, extension):
        totalReplacements = 0

        for directory, directories, files in os.walk(rootDirectory):

            """ Ignore any directories in the ignoredDirectories variable """
            if any(ignoredDirectory not in directory for ignoredDirectory in self.ignoredDirectories):
                for fileName in files:
                    if fileName.endswith('.' + extension):
                        filePath = os.path.join(directory, fileName)
                        
                        with open(filePath) as f:
                            s = f.read()
                        
                        matches = s.count(find)
                        if matches > 0:
                            print str(matches) +" occurences found in " + filePath
                            s = s.replace(find, replace)
                            totalReplacements += matches 
                        
                        with open(filePath, "w") as f:
                            f.write(s)

        return totalReplacements

# Execute script
if __name__ == '__main__':
  main()

