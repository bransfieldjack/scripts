"""
Iterates over all the tar files in a directory, 
then searches each tarfile for a particular file type/name, 
then writes that to a new location. 
"""

import os, tarfile, pandas
import smtplib
import glob
import re

def main():

    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'admin@stemformatics.org'
    smtp_password = '######'
    body = "Expression transfer script has finished running. "
    email_text = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % ("admin@stemformatics.org", "bransfieldjack@gmail.com", "Transfer script", body)
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.ehlo()
    s.starttls()
    s.ehlo
    s.login(smtp_username, smtp_password)

    # reT = re.compile(r'.*?count*?.*?.txt*?')
    reT = re.compile(r'count(.+?).txt')
    

    for tar_filename in glob.glob(r'data/*.tar.gz'):
        try:
            t = tarfile.open(tar_filename, 'r')
        except IOError as e:
            print (e)
        else:
            print([m for m in t.getmembers() if reT.search(m.name)])
            s.sendmail("admin@stemformatics.org", "bransfieldjack@gmail.com", email_text)
            s.quit()

            #t.extractall('out', members=[m for m in t.getmembers() if reT.search(m.name)])

if __name__ == "__main__":
    main()


