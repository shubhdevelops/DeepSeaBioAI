import subprocess
import os

def run_blast(query_fastq, db_path, output_path):
    """
    Placeholder function.
    Actual BLAST runs inside GitHub Actions using system-installed BLAST+.
    Here we just define the interface.
    """

    print("[BLAST] Running BLASTn...")

    cmd = [
        "blastn",
        "-query", query_fastq,
        "-db", db_path,
        "-out", output_path,
        "-outfmt", "6 qseqid sseqid pident length evalue bitscore staxids sscinames"
    ]

    # In GitHub Actions, this will execute BLAST
    subprocess.run(cmd, check=True)

    print("[BLAST] Output saved:", output_path)
