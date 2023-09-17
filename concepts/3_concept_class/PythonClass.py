class fasta:
	def __init__(self, fasta_file):
		self.fasta_file = fasta_file
		self.header = self.get_header()
		self.sequence = self.get_sequence()
	# Get Sequence Header
	def get_header(self):
		with open(self.fasta_file, "r") as fasta_file:
			header = [line.strip()[1:] for line in fasta_file if line.startswith(">")]
		return header
	# Get Sequence
	def get_sequence(self):
		with open(self.fasta_file, "r") as fasta_file:
			sequences = "".join(line.strip() for line in fasta_file if not line.startswith(">")).split(">")
			sequences = [sequence.replace("\n", "") for sequence in sequences if sequence]
		return sequences
	# Get Sequence Length
	def sequence_length(self):
		return len(self.sequence)
	# Get GC Content
	def gc_content(self):
		for sequence in self.sequence:
			total_bases = len(str(sequence))
			gc_content = (sequence.count("G") + sequence.count("C")) / total_bases * 100
			return gc_content


# fasta = fasta("/Users/bhag/Documents/Code/automation/python_utility_scripts/data/test.fasta")
# print(fasta.gc_content())