"""
Iterates over all the tar files in a directory, 
then searches each tarfile for a particular file type/name, 
then writes that to a new location. 
"""

import os, tarfile
import glob
import re

def main():

        
    reT = re.compile(r'.*?count*?.*?.txt*?')   # redundant as you dont have to filter the files searched, your iterating over all the files in the dir.

    rnaSeqIds = []
    for string in glob.glob(r'/nfs/HSM/archive/rnaseq/*.tar.gz'):
        test = int(filter(str.isdigit, string)) # grab the ints from the string
        rnaSeqIds.append(test)
    # print(rnaSeqIds)
    # print(len(rnaSeqIds))


    """
    Data contained on the API expression files mount right now:):
    """
    missing_from_expression_files_on_api = set([6060, 6105, 6219, 6691, 6538, 6519, 5010, 6525, 6728, 6547, 6460, 6054, 6650, 
    6422, 6472, 6165, 6427, 6415, 6551, 6689, 6204, 6510, 6568, 6647, 6442, 6681, 
    6352, 6192, 7156, 6312, 6159, 6744, 6595, 6539, 6840, 6616, 6330, 6709, 6215, 
    6722, 6361, 6738, 6645, 7097, 7285, 6121, 6425, 6743, 6097, 6424, 6401, 7346, 
    6759, 6259, 7255, 6031, 6800, 6985, 6243, 6535, 6217, 6437, 6241, 6640, 20170320, 
    6305, 6314, 6651, 6235, 6211, 6333, 6220, 6341, 6365, 6304, 6441, 6209, 6372, 6212, 
    6246, 6856, 6537, 6548, 6299, 7292, 6548, 6586, 6841, 6421, 6636, 6469, 6707, 7157, 
    6549, 6697, 6419, 7070, 6257, 6626, 6605, 6667, 6426, 6418, 6833, 6428, 6803, 6294, 
    6301, 6630, 6550, 6888, 7257, 6420, 6488, 6464, 6720, 6554, 6726, 6964, 6384, 6962, 
    6240, 6563, 6423, 6374, 6214, 6581, 6493, 6191, 6648, 7190, 6387, 6690, 6508, 6356, 
    6524, 6520, 6234, 6564, 6400, 7286, 6256, 6668, 6587, 6726, 6738, 6504, 5037, 7377, 
    6511, 7069, 6262, 7327, 6553, 6397, 6692, 6739, 6494, 7110])

    """
    The tar files that are in the pipe location right now 
    (and that I have already extracted the frag_count.txt files from, 
    backup location: '/mnt/various-srv-backups/expression_19052020/_tar_gz/source' :)
    """
    files_in_the_rnaseq_folder_on_pipe = set([6589, 6523, 6991, 6850, 6936, 7142, 7263, 7229, 7272, 7268, 
    7062, 7284, 7205, 7264, 7267, 7283, 6412, 6530, 7194, 7228, 6639, 7157, 7253, 
    6888, 7097, 7079, 7193, 7292, 6750, 6767, 7132, 6730, 7110, 7274, 7393, 7241, 
    6601, 7192, 7139, 7289, 7224, 7357, 7240, 7379, 7032, 7376, 7365, 7124, 7061, 
    7135, 7159, 7188, 7396, 7171, 7327, 7377, 7182, 7249, 7302, 7275, 6932, 7381, 
    6798, 7172, 7242, 6954, 7200, 7179, 7394, 7339, 6764, 7343, 6496, 6855, 6884, 
    6896, 7046, 7308, 7254, 7313, 7319, 7312, 6735, 7321, 7322, 6580, 7397, 7345, 
    7346, 7351, 6572, 7382, 6769, 7350, 6608, 6759, 7102, 7127, 7320, 7361, 7285, 
    7286, 7239, 7378, 7347, 7383, 7384, 7399, 7276, 7402, 7398, 7248, 7190, 7255, 
    7260, 6980, 7273, 7290, 6949, 7257])

    z = list(missing_expression_files - files_in_rnaseq)

    print(z)

    """
    This is the list of what is still remaining as 'missing' from the API expression files mount location
    """
    still_leftover_as_missing_from_api_after_the_pipe_rnaseq_tar_files_are_extracted_and_copied = [6667, 6668, 6159, 6165, 6681, 6689, 6690, 6691, 
    6692, 6697, 6191, 6192, 6707, 6709, 6204, 6720, 6209, 6722, 6211, 6212, 6726, 
    6215, 6728, 6217, 6219, 6220, 20170320, 6738, 6739, 6743, 6744, 6234, 
    6235, 6240, 6241, 6243, 6246, 6256, 6257, 6259, 6262, 6800, 6803, 
    6294, 6299, 6301, 6304, 6305, 6312, 6314, 6833, 6840, 
    6841, 6330, 6333, 6341, 6856, 6352, 6356, 6361, 6365, 
    6372, 6374, 6384, 6387, 6397, 6400, 6401, 6415, 6418, 6419, 6420, 6421, 6422, 
    6423, 6424, 6425, 6426, 6427, 6428, 6437, 6441, 6442, 6962, 6964, 6460, 6464, 6469, 
    6472, 6985, 6488, 6493, 6494, 6504, 6508, 6510, 6511, 6519, 6520, 6524, 6525, 6535, 
    6537, 6538, 6539, 6031, 5010, 6547, 6548, 6549, 6550, 6551, 6553, 6554, 7069, 7070, 
    6563, 6564, 6214, 6054, 6568, 6060, 5037, 6581, 6586, 6587, 6595, 6605, 6097, 6616, 
    6105, 6626, 6630, 6121, 6636, 6640, 7156, 6645, 6647, 6648, 6650, 6651]
        
    
if __name__ == "__main__":
    main()

