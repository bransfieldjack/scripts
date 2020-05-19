"""
Iterates over all the tar files in a directory, 
then searches each tarfile for a particular file type/name, 
then writes that to a new location. 
"""

import os, tarfile, pandas
import glob
import re

def main():

        
    reT = re.compile(r'.*?count*?.*?.txt*?')

    for tar_filename in glob.glob(r'data/*.tar.gz'):
        try:
            t = tarfile.open(tar_filename, 'r')
        except IOError as e:
            print (e)
        else:
            # print([m for m in t.getmembers() if reT.search(m.name)])
            t.extractall('out', members=[m for m in t.getmembers() if reT.search(m.name)])

if __name__ == "__main__":
    main()

