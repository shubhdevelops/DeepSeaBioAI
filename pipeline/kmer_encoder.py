import os
from Bio import SeqIO
from collections import Counter
import numpy as np

def generate_kmers(seq, k=6):
    """Generate all k-mers from a sequence."""
    return [seq[i:i+k] for i in range(len(seq)-k+1)]


def encode_kmers(cleaned_path: str, output_path: str, k: int = 6):
    """
    Encode cleaned DNA sequences into k-mer frequency vectors.
    This is the feature input for ML (CNN/DBN).
    """

    print(f"[KMER] Encoding {cleaned_path} (k={k})")

    # Detect input format
    fmt = "fastq" if cleaned_path.endswith(("fastq", ".fq")) else "fasta"

    all_counts = Counter()

    # Read cleaned sequences
    for record in SeqIO.parse(cleaned_path, fmt):
        seq = str(record.seq)
        kmers = generate_kmers(seq, k)

        # Count k-mers in this sequence
        all_counts.update(kmers)

    # Convert dictionary → sorted vector
    unique_kmers = sorted(all_counts.keys())
    vector = np.array([all_counts[kmer] for kmer in unique_kmers])

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save vector
    np.save(output_path, vector)

    print(f"[KMER] K-mer vector saved: {output_path}.npy")
    print(f"[KMER] Total unique k-mers: {len(unique_kmers)}")
