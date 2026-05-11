import re

stop_codons = ['TAA', 'TAG', 'TGA']
start_codon = 'ATG'


def extract_gene_name(header):
    gene_match = re.search(r'gene:([^\s]+)', header)
    if gene_match:
        return gene_match.group(1)
    return header.split()[0]


def find_inframe_stop_codons(sequence): 
    found_stops = set()
    seq = sequence.upper()

    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    break  

    return found_stops


def main():
    input_file = 'Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = 'Practical7\stop_genes.fa'

    total_genes = 0
    genes_with_stops = 0

    with open(output_file, 'w') as out_fh:
        with open(input_file, 'r') as in_fh:
            current_header = None
            current_seq_lines = []

            for line in in_fh:
                line = line.strip()

                if line.startswith('>'):
                    if current_header is not None:
                        total_genes += 1
                        sequence = ''.join(current_seq_lines)
                        stops = find_inframe_stop_codons(sequence)

                        if stops:
                            genes_with_stops += 1
                            gene_name = extract_gene_name(current_header)
                            stop_list = ' '.join(sorted(stops))
                            out_fh.write(f">{gene_name} {stop_list}\n")
                            for i in range(0, len(sequence), 60):
                                out_fh.write(sequence[i:i+60] + '\n')

                    current_header = line[1:]  
                    current_seq_lines = []
                else:
                    current_seq_lines.append(line)

            if current_header is not None:
                total_genes += 1
                sequence = ''.join(current_seq_lines)
                stops = find_inframe_stop_codons(sequence)

                if stops:
                    genes_with_stops += 1
                    gene_name = extract_gene_name(current_header)
                    stop_list = ' '.join(sorted(stops))
                    out_fh.write(f">{gene_name} {stop_list}\n")
                    for i in range(0, len(sequence), 60):
                        out_fh.write(sequence[i:i+60] + '\n')

    print(f"Total genes processed: {total_genes}")
    print(f"Genes with in-frame stop codons: {genes_with_stops}")
    print(f"Output written to: {output_file}")

if __name__ == '__main__':
    main()