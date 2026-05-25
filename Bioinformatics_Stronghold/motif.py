# Finding a Protein Motif

import requests
import re

os.chdir('C:/Users/kisho/Desktop/Programming/Python/')

motif = r"N[^P][ST][^P]"
uniprot_ids = []

with open("file.txt", "r") as f:
    for line in f:
        uniprot_ids.append(line.strip())
        

for raw_id in uniprot_ids:
    uid = raw_id.split("_")[0]
    url = f"https://www.uniprot.org/uniprotkb/{uid}.fasta"
    response = requests.get(url)

    if response.status_code == 200:
        fasta = response.text.split("\n")

        seq = ""

        for line in fasta:
            if not line.startswith(">"):
                seq += line.strip()

        # collect positions
        positions = []

        for match in re.finditer(motif, seq):
            pos = match.start() + 1    
            positions.append(pos)

        # print ONLY if motif found
        if positions:
            print(raw_id)
            for p in positions:
                print(p, end=" ")
            print()

    else:
        print("Error fetching:",raw_id )
