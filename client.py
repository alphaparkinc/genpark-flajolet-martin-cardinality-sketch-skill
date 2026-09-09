import hashlib

class FlajoletMartinSketch:
    """Flajolet-Martin Distinct Elements Estimator."""
    def estimate_cardinality(self, stream: list[str]) -> dict:
        max_zeros = 0
        for item in stream:
            h = int(hashlib.md5(str(item).encode()).hexdigest(), 16)
            zeros = (h & -h).bit_length() - 1 if h != 0 else 0
            if zeros > max_zeros:
                max_zeros = zeros

        # Constant phi = 0.77351
        est = int(2 ** max_zeros / 0.77351)
        return {
            "stream_length": len(stream),
            "max_trailing_zeros": max_zeros,
            "estimated_distinct_count": est
        }
