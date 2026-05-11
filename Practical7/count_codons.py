import re
from collections import Counter
import matplotlib.pyplot as plt


def extract_gene_name(header):
    gene_match = re.search(r'gene:([^\s]+)', header)
    if gene_match:
        return gene_match.group(1)
    return header.split()[0]

def find_longest_orf_codons(sequence, target_stop):
    seq = sequence.upper()
    stop_codons = ['TAA', 'TAG', 'TGA']
    longest_orf_codons = []

    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            codons = []
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon == target_stop:
                    if len(codons) > len(longest_orf_codons):
                        longest_orf_codons = codons.copy()
                    break
                elif codon in stop_codons:
                    break
                else:
                    codons.append(codon)

    return longest_orf_codons

def get_user_stop_codon():
    valid_stops = ['TAA', 'TAG', 'TGA']
    while True:
        user_input = input("Enter a stop codon (TAA, TAG, or TGA): ").strip().upper()
        if user_input in valid_stops:
            return user_input
        print("Invalid input. Please enter TAA, TAG, or TGA.")


def main():
    target_stop = get_user_stop_codon()
    print(f"\nAnalyzing codon usage upstream of {target_stop}...")

    input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

    all_codon_counts = Counter()
    genes_with_target_stop = 0

    with open(input_file, 'r') as in_fh:
        current_seq_lines = []

        for line in in_fh:
            line = line.strip()

            if line.startswith('>'):
                if current_seq_lines:
                    sequence = ''.join(current_seq_lines)
                    codons = find_longest_orf_codons(sequence, target_stop)
                    if codons:
                        genes_with_target_stop += 1
                        all_codon_counts.update(codons)
                    current_seq_lines = []
            else:
                current_seq_lines.append(line)

        if current_seq_lines:
            sequence = ''.join(current_seq_lines)
            codons = find_longest_orf_codons(sequence, target_stop)
            if codons:
                genes_with_target_stop += 1
                all_codon_counts.update(codons)

    print(f"Genes containing {target_stop}: {genes_with_target_stop}")
    print(f"Total codons counted: {sum(all_codon_counts.values())}")
    print(f"Unique codons: {len(all_codon_counts)}")

    if not all_codon_counts:
        print(f"No genes found with in-frame {target_stop} stop codon.")
        return

    print("\nTop 10 most frequent codons:")
    for codon, count in all_codon_counts.most_common(10):
        percentage = (count / sum(all_codon_counts.values())) * 100
        print(f"  {codon}: {count} ({percentage:.2f}%)")

    print("\nGenerating pie chart...")

    top_n = 15
    most_common = all_codon_counts.most_common(top_n)

    if len(all_codon_counts) > top_n:
        top_codons = [item[0] for item in most_common]
        top_counts = [item[1] for item in most_common]
        others_count = sum(all_codon_counts.values()) - sum(top_counts)
        labels = top_codons + ['Others']
        sizes = top_counts + [others_count]
    else:
        labels = [item[0] for item in most_common]
        sizes = [item[1] for item in most_common]

    plt.figure(figsize=(14, 10))
    colors = plt.cm.Set3(range(len(labels)))

    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': 10}
    )

    for autotext in autotexts:
        autotext.set_fontweight('bold')

    plt.title(
        f'Distribution of In-Frame Codons Upstream of {target_stop}\n'
        f'Across {genes_with_target_stop} Genes in S. cerevisiae',
        fontsize=14,
        fontweight='bold'
    )

    plt.axis('equal')
    plt.tight_layout()

    output_chart = f'codon_frequency_{target_stop}.png'
    plt.savefig(output_chart, dpi=300, bbox_inches='tight')
    print(f"Pie chart saved to: {output_chart}")

    output_text = f'codon_counts_{target_stop}.fa'
    with open(output_text, 'w') as f:
        f.write(f"Codon usage upstream of {target_stop}\n")
        f.write(f"Genes analyzed: {genes_with_target_stop}\n")
        f.write(f"Total codons: {sum(all_codon_counts.values())}\n")
        f.write("Codon\tCount\tPercentage\n")
        for codon, count in all_codon_counts.most_common():
            percentage = (count / sum(all_codon_counts.values())) * 100
            f.write(f"{codon}\t{count}\t{percentage:.2f}%\n")
    print(f"Codon counts saved to: {output_text}")

if __name__ == '__main__':
    main()