import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from models import AnalysisConfig, AnalysisResult, AnalysisType, HeatmapConfig
from service import AnalysisService
from visualize import HeatmapBuilder


def main() -> None:
    parser = argparse.ArgumentParser(description="Pulisce e tokenizza file di testo.")
    parser.add_argument(
        "directory", type=Path, help="Cartella che contiene i file .txt"
    )
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error(f"La cartella non esiste: {args.directory}")

    service = AnalysisService()
    heatmap_config = HeatmapConfig()
    configs: list[AnalysisConfig] = []

    for analysis_type in AnalysisType:
        configs.append(
            AnalysisConfig(
                n=3,
                min_ngram_frequency=2,
                analysis_type=analysis_type,
            )
        )

    results: dict[AnalysisType, AnalysisResult] = service.run_analyses(
        args.directory, configs
    )
    for result in results.values():
        visualize(result, heatmap_config)
    plt.show()


def visualize(
    result: AnalysisResult, heatmap_config: HeatmapConfig
) -> Figure:
    return HeatmapBuilder.build(
        result.matrix.tolist(),
        result.labels,
        result.analysis_type.label,
        heatmap_config,
    )


if __name__ == "__main__":
    main()
