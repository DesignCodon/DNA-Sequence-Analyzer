from analyze import fasta, seq_validate, count_base, gc_percenage, comp, translate, find_orfs

#----- Main program-----#   

print("DNA Sequence Analysis")
print("*"*23)

file_name = input("Enter the name of the FASTA file (including extension): ")
sequence = fasta(file_name)

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

    print(f'\nGC content: {gc_percenage(sequence)}%')
  
    print(f"\nReverse Complement: {comp(sequence)}")

    # replacing T with U to get the mRNA sequence (Transcription)
    mRNA = comp(sequence).replace('T', 'U')
    print(f"\nThe mRNA sequence (transcription) is: {mRNA}") 

    print(f"\nThe translated protein sequence is: {translate(mRNA)}")
    print("(* represents the translation termination point.)")

    orfs = find_orfs(sequence)
    print(f"\nThe ORFs found in the sequence is/are: {orfs}")
    orf_proteins = [translate(comp(orf).replace('T', 'U')) for orf in orfs]
    print(f"\nThe protein sequences translated from the ORFs is/are: {orf_proteins}")
    
