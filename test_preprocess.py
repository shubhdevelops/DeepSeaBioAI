from pipeline.preprocess import preprocess_sample

preprocess_sample(
    input_path="data/rawdna/test.fastq",
    output_path="data/cleanedna/test_clean.fastq",
    min_length=10
)
