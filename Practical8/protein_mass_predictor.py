def protein_mass(sequence):
    mass_table = {
        'A': 71.04,
        'C': 103.01,
        'D': 115.03,
        'E': 129.04,
        'F': 147.07,
        'G': 57.02,
        'H': 137.06,
        'I': 113.08,
        'K': 128.09,
        'L': 113.08,
        'M': 131.04,
        'N': 114.04,
        'P': 97.05,
        'Q': 128.06,
        'R': 156.10,
        'S': 87.03,
        'T': 101.05,
        'V': 99.07,
        'W': 186.08,
        'Y': 163.06
    }
    total_mass = 0.0
    aa = sequence.split()
    for aa in sequence:
        if aa not in mass_table:
            print(f"Error: Invalid amino acid '{aa}' in the sequence.")
            exit(1)
        else:
            total_mass = sum(mass_table[aa] for aa in sequence)
            return total_mass

#Example usage
if __name__ == "__main__":
    sequence = "AGPC"
    mass = protein_mass(sequence)
    print(f"The total mass of the protein is: {mass:.2f} Da")