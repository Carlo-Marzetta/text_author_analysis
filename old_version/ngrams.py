from collections import Counter
from text_types import NGram, Segment


class NGramCounter:
    def __init__(self, segments: list[Segment]) -> None:

        self.segments = segments

    def countNGrams(self, n: int) -> Counter[NGram]:
        chapter_counter: Counter[NGram] = Counter()

        for segment in self.segments:
            segment_counter: Counter[NGram] = Counter(
                tuple(segment[i : i + n])
                for i in range(len(segment) - n + 1)
            )
            chapter_counter.update(segment_counter)

        return chapter_counter
