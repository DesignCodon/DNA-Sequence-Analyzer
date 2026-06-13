from analyze import fasta, seq_validate, count_base, gc_percentage, revcomp, translate, find_orfs

#----- Main program-----#   

print("DNA Sequence Analysis")
print("*"*23)

file_name = input("Enter the name of the FASTA file (including extension): ")

try:
    sequence = fasta(file_name)
except FileNotFoundError:
    print("File not found.")
    exit()

if(seq_validate(sequence)==False):
    print("Invalid sequence")
else:
    print(f'\nLength of the input sequence: {len(sequence)}')
    count = count_base(sequence)
    print("\nNumber of Bases:")
    print(f"A: {count['A']}")
    print(f"T: {count['T']}")
    print(f"G: {count['G']}")
    print(f"C: {count['C']}")

    print(f'\nGC content: {gc_percentage(sequence)}%')
  
    print(f"\nReverse Complement: {revcomp(sequence)}")

    # replacing T with U to get the RNA sequence (Transcription)
    RNA = sequence.replace('T','U')
    print(f"\nThe RNA sequence (transcription) is: {RNA}") 

    print(f"\nThe complete translated sequence is: {translate(RNA)}")
    print("(if * in translated sequence, means present of stop codon in RNA sequence.)")

    orfs = find_orfs(sequence)
    print(f"\nThe ORFs found in the sequence is: {orfs}")
    orf_proteins = [translate(orf.replace('T', 'U')) for orf in orfs]
    print(f"\nThe protein sequences translated from the ORFs is/are: {orf_proteins}")
    