from pathlib import Path

import numpy as np

from models import AnalysisConfig, AnalysisResult, AnalysisType, ChapterProfile
from ngrams import NGramCounter
from segmentator import TextSegmentator
from similarity import AnalysisRunner
from text_processing import TextFileProcessor

BOUNDARIES = {
    "<end>",
    "<gap_01>",
    "<gap_02>",
    "<gap_03>",
    "<gap_04>",
    "<gap_05>",
    "<gap_06>",
    "<gap_07>",
    "<gap_08>",
    "<gap_09>",
    "<gap_10>",
    "<gap_11>",
    "<gap_?>",
    "<formula>",
}


class AnalysisService:
    def run_analysis(
        self,
        directory: Path,
        analysis_config: AnalysisConfig,
    ) -> AnalysisResult:
        return self.run_analyses(directory, [analysis_config])[
            analysis_config.analysis_type
        ]

    def run_analyses(
        self,
        directory: Path,
        analysis_configs: list[AnalysisConfig],
    ) -> dict[AnalysisType, AnalysisResult]:
        if not analysis_configs:
            raise ValueError("È necessaria almeno una configurazione di analisi.")
        if not directory.is_dir():
            raise ValueError(f"La cartella non esiste: {directory}")

        tokens_by_file = TextFileProcessor(directory).process()
        if not tokens_by_file:
            raise ValueError(f"Nessun file .txt trovato in: {directory}")

        profiles_by_ngram_size: dict[int, list[ChapterProfile]] = {}
        results: dict[AnalysisType, AnalysisResult] = {}
        for analysis_config in analysis_configs:
            if analysis_config.n not in profiles_by_ngram_size:
                chapter_profiles: list[ChapterProfile] = []
                for file_path, tokens in tokens_by_file.items():
                    segments = TextSegmentator(
                        tokens, boundaries=BOUNDARIES
                    ).split_on_boundaries()
                    ngram_counts = NGramCounter(segments).countNGrams(
                        n=analysis_config.n
                    )
                    chapter_profiles.append(
                        ChapterProfile(path=file_path, ngram_counts=ngram_counts)
                    )
                profiles_by_ngram_size[analysis_config.n] = chapter_profiles

            chapter_profiles = profiles_by_ngram_size[analysis_config.n]
            matrix = AnalysisRunner(analysis_config).run(chapter_profiles)
            results[analysis_config.analysis_type] = AnalysisResult(
                analysis_type=analysis_config.analysis_type,
                matrix=np.asarray(matrix, dtype=float),
                labels=[profile.path.stem for profile in chapter_profiles],
            )

        return results
