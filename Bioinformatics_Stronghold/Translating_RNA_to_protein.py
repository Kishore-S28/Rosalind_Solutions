# Translating RNA to Protein

def trans(seq):
    protein = ""

    for i in range (0, len(seq), 3):
        codon = seq[i:i+3]

        if len(codon)==3:
            protein += RNA_Codons[codon]
    return protein

seq = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print(trans(seq))
