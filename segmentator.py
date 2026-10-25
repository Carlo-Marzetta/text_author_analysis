


class TextSegmentator:
    def __init__(self, tokens: list[str], boundaries: set[str]) -> None:
        self.tokens = tokens
        self.boundaries = boundaries

    def split_on_boundaries(self) -> list[list[str]]:
        segments = []
        current_segment = []

        for token in self.tokens:
            if token in self.boundaries:
                if current_segment:
                    segments.append(current_segment)
                    current_segment = []
            else:
                current_segment.append(token)

        if current_segment:
            segments.append(current_segment)

        return segments
