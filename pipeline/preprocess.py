from Bio import SeqIO
import os

def preprocess_sample(input_path: str, output_path: str, min_length: int = 100):
    """
    Basic FASTQ/FASTA preprocessing:
    - Removes sequences shorter than min_length.
    - Removes sequences containing too many N's.
    """

    print(f"[PREPROCESS] Reading: {input_path}")

    records = []
    count_in = 0
    count_out = 0

    # Detect format
    fmt = "fastq" if input_path.endswith(("fastq", ".fq")) else "fasta"

    for record in SeqIO.parse(input_path, fmt):
        count_in += 1
        seq = str(record.seq)

        # Skip sequence if too short
        if len(seq) < min_length:
            continue

        # Skip if too many Ns
        if seq.count("N") > 5:
            continue

        records.append(record)
        count_out += 1

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write cleaned sequences
    SeqIO.write(records, output_path, fmt)

    print(f"[PREPROCESS] Completed.")
    print(f"   Input reads: {count_in}")
    print(f"   Output reads: {count_out}")
    print(f"   Saved cleaned file at: {output_path}")
