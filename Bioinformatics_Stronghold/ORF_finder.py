# Finding Open Reading Frames in DNA sequences

codon_table = {
    "ATA":"I","ATC":"I","ATT":"I","ATG":"M",
    "ACA":"T","ACC":"T","ACG":"T","ACT":"T",
    "AAC":"N","AAT":"N","AAA":"K","AAG":"K",
    "AGC":"S","AGT":"S","AGA":"R","AGG":"R",
    "CTA":"L","CTC":"L","CTG":"L","CTT":"L",
    "CCA":"P","CCC":"P","CCG":"P","CCT":"P",
    "CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
    "CGA":"R","CGC":"R","CGG":"R","CGT":"R",
    "GTA":"V","GTC":"V","GTG":"V","GTT":"V",
    "GCA":"A","GCC":"A","GCG":"A","GCT":"A",
    "GAC":"D","GAT":"D","GAA":"E","GAG":"E",
    "GGA":"G","GGC":"G","GGG":"G","GGT":"G",
    "TCA":"S","TCC":"S","TCG":"S","TCT":"S",
    "TTC":"F","TTT":"F","TTA":"L","TTG":"L",
    "TAC":"Y","TAT":"Y","TAA":"_","TAG":"_",
    "TGC":"C","TGT":"C","TGA":"_","TGG":"W"
}

# Read FASTA sequence
sequence = ""

with open("motif.txt", "r") as f:
    for line in f:
        if not line.startswith(">"):
            sequence += line.strip()

# Generate reverse complement
def reverse_complement(seq):
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    return ''.join(complement[base] for base in reversed(seq))

# Translate DNA sequence into protein
def translate(seq):
    protein = ""
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]

        # Ignore incomplete codons
        if len(codon) < 3:
            break

        amino_acid = codon_table.get(codon, "")

        # Stop translation at stop codon
        if amino_acid == "_":
            break

        protein += amino_acid
    return protein


# Find ORFs in a reading frame
def find_orfs(seq):
    proteins = set()
    for i in range(len(seq) - 2):

        # Look for start codon
        if seq[i:i+3] == "ATG":
            for j in range(i, len(seq), 3):
                codon = seq[j:j+3]

                # Stop codons
                if codon in ["TAA", "TAG", "TGA"]:
                    protein = translate(seq[i:j+3])

                    if protein:
                        proteins.add(protein)
                    break
    return proteins

# Store all proteins
all_proteins = set()

# Forward reading frames
for frame in range(3):
    all_proteins.update(find_orfs(sequence[frame:]))

# Reverse reading frames
reverse_seq = reverse_complement(sequence)

for frame in range(3):
    all_proteins.update(find_orfs(reverse_seq[frame:]))

# Print proteins
for protein in all_proteins:
    print(protein)
