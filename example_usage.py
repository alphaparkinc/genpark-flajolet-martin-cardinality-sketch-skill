from client import FlajoletMartinSketch

def main():
    print("=== Flajolet-Martin Cardinality Sketch ===")
    sketch = FlajoletMartinSketch()
    # 50 unique items repeated 10 times
    items = [f"item_{i % 50}" for i in range(500)]
    res = sketch.estimate_cardinality(items)
    print("FM Estimate Result:", res)
    assert res["estimated_distinct_count"] > 15

    print("Flajolet-Martin Sketch verified successfully!")

if __name__ == "__main__":
    main()
