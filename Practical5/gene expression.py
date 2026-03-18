gene_expression = {"TP53":12.4, "EGFR":15.1, "BRCA1":8.2, "PTEN":5.3, "ESR1":10.7}
gene_expression["MYC"] = 11.6

import numpy as np
import matplotlib.pyplot as plt

genes = list(gene_expression.keys()) 
expression_levels = list(gene_expression.values())
plt.bar(genes, expression_levels, color='skyblue')
plt.xlabel('Genes')
plt.ylabel('Expression Levels')
plt.title('Gene Expression Levels')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

gene_of_interest = input("Enter the gene you want to check: ")
if gene_of_interest in gene_expression:
    print(f"{gene_of_interest} expression level: {gene_expression[gene_of_interest]}")  
else:
    print(f"{gene_of_interest} not found in the gene expression data.")

total_expression = sum(expression_levels)
average_expression = total_expression / len(gene_expression)
print(f"Average Expression: {average_expression}")