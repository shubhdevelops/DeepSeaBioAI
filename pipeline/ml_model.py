import numpy as np

def ml_predict(kmer_vector_path: str):
    """
    Placeholder ML model.
    Reads k-mer vector and returns a dummy classification.
    Used for pipeline connectivity before real CNN model.
    """

    print(f"[ML] Loading vector: {kmer_vector_path}")

    vector = np.load(kmer_vector_path + ".npy")

    # Simple fake logic (just for prototype)
    if vector.sum() < 100:
        return "Unknown organism"
    else:
        return "Bacteria (placeholder prediction)"
