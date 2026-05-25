# Rosalind Problem
# Count the number of each nucleotide in a DNA string

def count_nt_freq(dna):
    counts = {
        "A": dna.count("A"),
        "C": dna.count("C"),
        "G": dna.count("G"),
        "T": dna.count("T")
    }
    return counts

DNA_string = "GCCCCAATGCTCTGT"

result = count_nt_freq(DNA_string)

print(result)
print(' '.join([str(val) for val in result.values()]))
