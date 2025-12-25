#!"D:\Anaconda\python.exe" -u

'''
functions for the main program:
1. dna_check, rna_check
2. nuc_frequency
3. 
'''

import collections

dna_nucleotides = ['A', 'C', 'G', 'T']
rna_nucleotides = ['A', 'C', 'G', 'U']

#1. check the sequence to make sure it is a DNA or RNA string
def dna_check(dna_seq: str) -> str:
    tmp_dna_seq = dna_seq.upper()
    for nuc in tmp_dna_seq:
        if nuc not in dna_nucleotides:
            raise ValueError(f"invalid nucleotide [{nuc}] in DNA sequence")
    return tmp_dna_seq

def rna_check(rna_seq: str) -> str:
    tmp_rna_seq = rna_seq.upper()
    for nuc in tmp_rna_seq:
        if nuc not in rna_nucleotides:
            raise ValueError(f"invalid nucleotide [{nuc}] in RNA sequence")
    return tmp_rna_seq

#2. count the frequency of each nucleotide in the sequence
def nuc_frequency(seq: str) -> dict:
    return dict(collections.Counter(seq))

#3. 

