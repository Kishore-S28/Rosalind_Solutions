# Reverse Complementing a strand of DNA

def reverse_comp(seq):
    DNA_comp = {"A": "T", "C": "G", "G": "C", "T": "A"}
    rev_comp = ''.join([DNA_comp[nuc] for nuc in seq])[::-1]
    return rev_comp

seq = "AGCACAGTATTGTCTTCCAA"
print(reverse_comp(seq))
