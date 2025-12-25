

from dna_toolkit import *
import random

# generate random DNA and RNA sequences
rand_dna_seq = ''.join([random.choice(dna_nucleotides) for nuc in range(20)])
rand_rna_seq = ''.join([random.choice(rna_nucleotides) for nuc in range(20)])
print(f'DNA sequence: {rand_dna_seq}')
print(f'RNA sequence: {rand_rna_seq}')

# count nucleotides in DNA and RNA sequences
print(f'DNA nucleotide frequencies: {nuc_frequency(rand_dna_seq)}')
print(f'RNA nucleotide frequencies: {nuc_frequency(rand_rna_seq)}')
print(' '.join([str(val) for key, val in nuc_frequency(rand_dna_seq).items()]))






# def main():
#     if __name__ == '__main__':
