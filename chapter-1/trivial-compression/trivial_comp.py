class CompressedGene:
    def _init_(self, gene:str) -> None:
        self._compress(gene)

def _compress(self, gene:str) -> None:
    self.bit_string: int = 1 # starts with a sentinel
    for nucleotide in gene.upper():
        self.bit_string <<= 2 # move 2 bits left
        if nucleotide == "A": # change last 2 bits for 00
            self.bit_string |= 0b00
        elif nucleotide == "C": # change last 2 bits for 01
            self.bit_string |= 0b01
        elif nucleotide == "G": # change last 2 bits for 10
            self.bit_string |= 0b10
        elif nucleotide == "T": # change last 2 bits for 11
            self.bit_string |= 0b11
        else:
            raise ValueError("Invalid Nucleotide:{}".format(nucleotide))