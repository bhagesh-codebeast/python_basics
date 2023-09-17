
from fasta_utility import fasta

def main():
	fasta_obj = fasta("/Users/bhag/Documents/Code/python_basics/data/test.fasta")
	print(f"fasta header:{fasta_obj.header}\nfasta sequence:{fasta_obj.sequence}\nfasta GC content:{fasta_obj.gc_content()}")

if __name__ == "__main__":
	main()