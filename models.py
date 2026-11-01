from dataclasses import dataclass
from pathlib import Path
from collections import Counter

import numpy as np
from text_types import NGram
from enum import Enum


class AnalysisType(str, Enum):
    WEIGHTED_JACCARD = "weighted_jaccard"
    COSINE = "cosine"
    BERT = "tibert"

    @property
    def code(self) -> str:
        return self.value

    @property
    def label(self) -> str:
        return {
            AnalysisType.WEIGHTED_JACCARD: "Weighted Jaccard",
            AnalysisType.COSINE: "Cosine Similarity",
        }[self]


@dataclass
class ChapterProfile:
    path: Path
    ngram_counts: Counter[NGram]


@dataclass
class AnalysisConfig:
    n: int
    min_ngram_frequency: int
    merged_boundaries: bool = False
    remove_suffixes: bool = False
    analysis_type: AnalysisType = AnalysisType.COSINE


@dataclass(frozen=True)
class AnalysisResult:

    analysis_type: AnalysisType

    matrix: np.ndarray

    labels: list[str]


@dataclass
class HeatmapConfig:
    cmap: str = "magma"

    vmin: float = 0.0
    vmax: float = 1.0

    annot: bool = False
    fmt: str = ".2f"

    hide_diagonal: bool = False

    figure_width: int = 15
    figure_height: int = 8

    square: bool = True
