# Transcribe DNA into RNA

def tr(seq):
    return seq.replace("T", "U")

dna = "GATGGAACTTGACTACGTAAATT"
rna = tr(dna)

print(rna)
