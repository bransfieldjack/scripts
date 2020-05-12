"""
Extract the RNA Seq counts files from .tar archives.
"""

import os, tarfile, pandas

in_dir = "/nfs/HSM/archive/rnaseq"
out_dir = "/nfs/HSM/expression/"

def checkFiles():
    """Check microarray and rnaseq dirs to see if rna seq datasets are indeed missing from out_dir
    Results: There are 624 dataset ids in /nfs/HSM/archive/microarray and 289 dataset ids in /nfs/HSM/archive/rnaseq
    and these 5 are common: {'7127', '6412', '6309', '6197', '6186'}. We can just ignore these and extract them again.
    Between in_dir and out_dir, there are already 99 datasets from in_dir in out_dir, so we don't need to extract these.
    """
    microarray = set([item.split(".")[0] for item in os.listdir("/nfs/HSM/archive/microarray") if ".tgz" in item])
    rnaseq = set([item.split(".")[0] for item in os.listdir(in_dir)])
    outdata = set([item.split(".")[0] for item in os.listdir(out_dir)])
    print(len(microarray), len(rnaseq), len(outdata), microarray.intersection(rnaseq), len(outdata.intersection(rnaseq)))
    print(list(outdata.intersection(rnaseq))[:5])
    print('6655' in rnaseq, '6655' in outdata, '6197' in rnaseq, '6197' in outdata)

if __name__ == "__main__":
    checkFiles()


