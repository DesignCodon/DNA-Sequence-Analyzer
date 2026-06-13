# Functions:

# 1. fasta file reading
def fasta(filename):
    with open(filename) as file:
        lines = file.readlines()

    seq_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('>'):
            continue
        seq_lines.append(line)

    return ''.join(seq_lines).upper()


# 2.function to validate the input sequence 
def seq_validate(seq):
    valid_base = {'A', 'T', 'G', 'C'}
    for base in seq:
        if base not in valid_base:
            return False
    return True

# 3.function to count the number of individual bases
def count_base (seq):
    count = {'A':0,'T':0,'G':0, 'C':0}
    for base in seq:
        count[base] +=1
    return count

# 4. function to calculate the GC content of the input sequence
def gc_percentage(seq):
    count = count_base(seq)
    gc = (((count['G'] + count['C']) / len(seq)) * 100)
    return round(gc, 2)

# 5. function to return the complement of the input sequence
def revcomp(sequence):
    result = []
    for base in sequence:
        if base == 'A':
            result.append('T')
        elif base == 'T':
            result.append('A')
        elif base == 'G':
            result.append('C')
        elif base == 'C':
            result.append('G')

    return ''.join(result)[::-1]

# 6. function for mRNA-->Protein translation.
def translate(rna):
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG':'R',
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", 	'AGG':'R',
        "GUU": "V", "GUC": "V", "GUA": "V", 	"GUG":"V",
        "GCU": "A", 	"GCC":"A", 	"GCA":"A", 	"GCG":"A",
        "GAU": "D", 	"GAC":"D", 	"GAA":"E", 	"GAG":"E",
        "GGU": "G", 	"GGC":"G", 	"GGA":"G", 	"GGG":"G"
    }
    protein = []
    for i in range(0, len(rna)-2, 3):
        codon = rna[i:i+3]
        if codon in codon_table:
            protein.append(codon_table[codon])
    return ''.join(protein)

# 7. function for ORF finder
def find_orfs(sequence):
    start_codon = 'ATG'
    stop_codons = {'TAA', 'TAG', 'TGA'}
    orfs = []

    # Check all three reading frames
    for frame in range(3):

        for i in range(frame, len(sequence) - 2, 3):

            codon = sequence[i:i+3]

            if codon == start_codon:

                for j in range(i + 3, len(sequence) - 2, 3):

                    stop_codon = sequence[j:j+3]

                    if stop_codon in stop_codons:

                        orfs.append(sequence[i:j+3])
                        break

    return orfs