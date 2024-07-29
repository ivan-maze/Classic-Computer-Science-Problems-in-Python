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

def decompress(self) -> str:
    gene: str = ""
    for i in range(0, self.bit_string.bit_lenght()-1, 2): # -1 to exclude sentinel
        bits: int = self.bit_string >> i & 0b11 # get just 2 relevant bits
        if bits == 0b00: # A
            gene += "A"
        elif bits == 0b01: # C
            gene += "C"
        elif bits == 0b10: # G
            gene += "G"
        elif bits == 0b11: # T
            gene += "T"
        else:
            raise ValueError("Invalid bits:{}".format(bits))
    return gene[::-1] # invert string

def _str_(self) -> str: # string representation
    return self.decompress()
