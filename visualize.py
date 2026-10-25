import matplotlib.pyplot as plt
import seaborn as sns
from models import HeatmapConfig


class HeatmapBuilder:

    @staticmethod
    def build(
        matrix: list[list[float]],
        labels: list[str],
        title: str,
        config: HeatmapConfig,
    ):


        fig, ax = plt.subplots(
            figsize=(
                config.figure_width,
                config.figure_height,
            )
        )

        sns.heatmap(
            matrix,
            cmap=config.cmap,
            vmin=config.vmin,
            vmax=config.vmax,
            xticklabels=labels,
            yticklabels=labels,
            annot=config.annot,
            fmt=config.fmt,
            square=config.square,
            mask=config.hide_diagonal,
            ax=ax,
        )
        ax.set_title(title)
        return fig
