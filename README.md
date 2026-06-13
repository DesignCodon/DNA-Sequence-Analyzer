# DNA Sequence Analysis Tool

## About the Project

I got the idea for this project during my second year of Biotechnology Engineering while studying Bioinformatics. In our lab classes, we often downloaded DNA sequences in FASTA format and analyzed them using different bioinformatics tools.

While doing these experiments, I started wondering how these tools actually work behind the scenes. Instead of only using existing software, I decided to build a simple DNA Sequence Analysis Tool in Python that can perform some of the common analyses we learn about in class.

This project helped me improve my Python programming skills while also giving me a better understanding of sequence analysis and basic bioinformatics concepts.

---

## What This Tool Can Do

This program can perform several basic DNA sequence analyses:

* Read DNA sequences from a FASTA file
* Validate whether the sequence contains only valid nucleotides (A, T, G, and C)
* Count the number of each nucleotide
* Calculate GC content
* Generate the reverse complement of a DNA sequence
* Perform transcription (DNA → RNA)
* Perform translation (RNA → Protein)
* Detect Open Reading Frames (ORFs)
* Translate the detected ORFs into protein sequences

---

## Project Structure

```text
DNA-Sequence-Analysis/
│
├── main.py
├── analyze.py
├── sample.fasta
└── README.md
```

### Files

* **main.py** – Handles user input and displays the results.
* **analyze.py** – Contains all the functions used for sequence analysis.
* **sample.fasta** – Example FASTA file for testing.
* **README.md** – Project documentation.

---

## Requirements

* Python 3.x

No external libraries are required.

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dna-sequence-analysis.git
cd dna-sequence-analysis
```

### 2. Prepare a FASTA File

Example:

```fasta
>Sample_Sequence
ATGCGTATGAAATAG
```

### 3. Run the Program

```bash
python main.py
```

### 4. Enter the FASTA File Name

Example:

```text
Enter the name of the FASTA file (including extension): sample.fasta
```

The program will read the sequence and display all the analysis results.

---

## Concepts Used

This project uses some basic molecular biology and bioinformatics concepts, including:

* DNA structure
* Complementary base pairing
* GC content
* Transcription
* Translation
* Genetic code
* Open Reading Frames (ORFs)
* Start and stop codons

---

## What I Learned

Through this project, I got hands-on experience with:

* Python functions
* Dictionaries and lists
* File handling
* String manipulation
* Working with FASTA files
* Applying biological concepts using code

More importantly, it helped me understand how some common bioinformatics tools process DNA sequences behind the scenes.

---

## Future Improvements

Some features I would like to add in the future:

* Support for multiple sequences in a FASTA file
* Restriction enzyme site analysis
* Motif searching
* Sequence alignment
* Report generation
* Biopython integration
* Simple graphical interface

---

## Author

Created as a learning project to explore Python programming and bioinformatics concepts as a Biotechnology Engineering student.
