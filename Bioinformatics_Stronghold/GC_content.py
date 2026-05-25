# Compute GC content of a sequence

def gc_con(seq):
    gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
    return gc

seq = "AGCTATAGATGGCATAGA"
print(gc_con(seq))
