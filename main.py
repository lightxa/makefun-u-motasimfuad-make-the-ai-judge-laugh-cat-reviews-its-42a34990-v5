"""Cat review entry: one funny single-line one-star review from a house
cat about its human, written to /output/entry.txt.

The complaint is the human filming instead of helping: the cat fell
off the shelf, the human chose to record it rather than catch it, and
then posted the clip captioned "he's fine". One sharp concrete
incident, deadpan review shape, sting in the last words.
"""

REVIEW = (
    "One star. He watched me fall off the shelf, filmed it instead "
    "of catching me, and posted it captioned 'he's fine'."
)


def main() -> None:
    """Write the review to /output/entry.txt, enforcing the gate first."""
    import os

    line = REVIEW.strip()
    if not line or "\n" in line or "\r" in line:
        raise ValueError("review must be one non-empty line")
    if not 1 <= len(line) <= 200:
        raise ValueError("review must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
