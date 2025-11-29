from pipeline.kmer_encoder import encode_kmers

encode_kmers(
    cleaned_path="data/cleanedna/test_clean.fastq",
    output_path="data/kmerdna/demo1_kmers",
    k=6
)
