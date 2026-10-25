from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import streamlit as st
from models import AnalysisConfig, AnalysisType, HeatmapConfig
from service import AnalysisService
from visualize import HeatmapBuilder


@dataclass(frozen=True)
class AnalysisRequest:

    input_directory: Path
    analysis_type: AnalysisType
    ngram_size: int
    min_ngram_frequency: int
    show_values: bool
    colormap: str
    figure_size: int

    def build_analysis_config(self) -> AnalysisConfig:

        return AnalysisConfig(
            analysis_type=self.analysis_type,
            n=self.ngram_size,
            min_ngram_frequency=self.min_ngram_frequency,
        )

    def build_heatmap_config(self) -> HeatmapConfig:

        return HeatmapConfig(
            annot=self.show_values,
            cmap=self.colormap,
            hide_diagonal=False,
            figure_width=self.figure_size,
            figure_height=self.figure_size,
        )


def main() -> None:
    st.title("Analisi stilistica")

    directory = st.text_input("Cartella contenente i file .txt")
    analysis_type = st.selectbox(
        "Tipo di analisi",
        options=list(AnalysisType),
        format_func=lambda item: item.label,
    )
    ngram_size = st.number_input("Dimensione n-grammi", min_value=1, value=3)
    min_frequency = st.number_input("Frequenza minima", min_value=1, value=2)
    show_values = st.checkbox("Mostra i valori", value=False)
    colormap = st.text_input("Colormap", value="magma")
    figure_size = st.number_input("Dimensione figura", min_value=1, value=8)

    if st.button("Avvia analisi"):
        if not directory.strip():
            st.error("Inserisci il percorso di una cartella.")
            return

        request = AnalysisRequest(
            input_directory=Path(directory),
            analysis_type=analysis_type,
            ngram_size=ngram_size,
            min_ngram_frequency=min_frequency,
            show_values=show_values,
            colormap=colormap,
            figure_size=figure_size,
        )

        try:
            result = AnalysisService().run_analysis(
                request.input_directory,
                request.build_analysis_config(),
            )
        except (ValueError, OSError) as exc:
            st.error(str(exc))
            return

        fig = HeatmapBuilder.build(
            result.matrix.tolist(),
            result.labels,
            result.analysis_type.label,
            request.build_heatmap_config(),
        )
        st.pyplot(fig)
        plt.close(fig)


main()
