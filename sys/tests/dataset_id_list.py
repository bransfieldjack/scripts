"""
This script will return a list of all the dataset_ids prepending the expression files, filenames in '' on the api server. 
"""

import os, tarfile, pandas
import smtplib
import glob
import re

def main():

    for item in glob.glob(r'/expression-files-volume/*.raw.tsv'):
        print(len(re.findall('\d+', item )))
    
if __name__ == "__main__":
    main()
