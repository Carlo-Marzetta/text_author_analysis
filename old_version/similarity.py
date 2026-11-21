from collections import Counter
from models import AnalysisConfig, AnalysisType, ChapterProfile
from math import sqrt

from collections import Counter


class AnalysisRunner:

    def __init__(
        self,
        config: AnalysisConfig
    ) -> None:

        self.config = config

    def process_profile(
        self,
        profile: ChapterProfile
    ) -> ChapterProfile:

        filtered_counter = Counter({
            ngram: count
            for ngram, count
            in profile.ngram_counts.items()
            if count >= self.config.min_ngram_frequency
        })

        return ChapterProfile(
            path=profile.path,
            ngram_counts=filtered_counter
        )

    def process_profiles(
        self,
        profiles: list[ChapterProfile]
    ) -> list[ChapterProfile]:

        return [
            self.process_profile(profile)
            for profile in profiles
        ]

    def run(
        self,
        profiles: list[ChapterProfile]
    ) -> list[list[float]]:

        filtered_profiles = self.process_profiles(
            profiles
        )

        match self.config.analysis_type:

            case AnalysisType.WEIGHTED_JACCARD:
                return WeightedJaccard.matrix(
                    filtered_profiles
                )

            case AnalysisType.COSINE:
                return CosineSimilarity.matrix(
                    filtered_profiles
                )

            case _:
                raise ValueError(
                    f"Unsupported analysis: "
                    f"{self.config.analysis_type}"
                )

class WeightedJaccard:

    @staticmethod
    def similarity(counter_a: Counter, counter_b: Counter) -> float:

        intersection = sum((counter_a & counter_b).values())

        union = sum((counter_a | counter_b).values())

        if union == 0:
            return 0.0

        return intersection / union

    @staticmethod
    def matrix(chaptersProfiles: list[ChapterProfile]) -> list[list[float]]:

        matrix = []

        for chapter_a in chaptersProfiles:

            row = []

            for chapter_b in chaptersProfiles:

                row.append(
                    WeightedJaccard.similarity(
                        chapter_a.ngram_counts, chapter_b.ngram_counts
                    )
                )

            matrix.append(row)

        return matrix


class CosineSimilarity:

    @staticmethod
    def similarity(profile_a: ChapterProfile, profile_b: ChapterProfile) -> float:

        counter_a = profile_a.ngram_counts
        counter_b = profile_b.ngram_counts

        # prodotto scalare
        dot_product = 0

        for ngram, count_a in counter_a.items():

            count_b = counter_b.get(ngram, 0)

            dot_product += count_a * count_b

        # norma del vettore A
        norm_a = sqrt(sum(count * count for count in counter_a.values()))

        # norma del vettore B
        norm_b = sqrt(sum(count * count for count in counter_b.values()))

        if norm_a == 0 or norm_b == 0:
            return 0.0

        return dot_product / (norm_a * norm_b)

    @staticmethod
    def matrix(chapter_profiles: list[ChapterProfile]) -> list[list[float]]:

        matrix = []

        for profile_a in chapter_profiles:

            row = []

            for profile_b in chapter_profiles:

                row.append(CosineSimilarity.similarity(profile_a, profile_b))

            matrix.append(row)

        return matrix
