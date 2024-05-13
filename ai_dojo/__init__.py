import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # tensorflow should stop it with the useless warnings

from . import (
    datasets,
    mlp,
    mlts,
    show,
    plot,
)

import seaborn
import jupyterthemes
import html
from pathlib import Path



colors = [
    "#6CA0A3",  # soft teal/blue shade from glass and walls
    "#D0C1A5",  # warm beige for walls
    "#2F3E46",  # deep blue/gray from shadows and corners
    "#403931",  # muted dark brown from wooden floor and frames
    "#E3584D",  # vibrant red-orange from robot's eye
    "#F0F0F0",  # light, almost white, for bright spots on walls
    "#7A7D80",  # mid-tone gray from shadows and robot's body
    "#F2B66D",  # accent color from robot's headlight illumination
]
palette = seaborn.color_palette(colors)

def setup_plot_style(dark=False):
    if dark:
        theme = "monokai"
    else:
        theme = None # TODO: select favorite light theme
    seaborn.set_style("ticks")
    jupyterthemes.jtplot.style(theme=theme, grid=True, figsize=(20, 8))
    seaborn.set_palette(palette)


def setup_slide_style(theme="night"):
    from traitlets.config.manager import BaseJSONConfigManager
    path = Path.home() / ".jupyter" / "nbconfig"
    cm = BaseJSONConfigManager(config_dir=str(path))
    cm.update(
        "rise",
        {
            "theme": theme,
            "transition": "fade",
            "start_slideshow_at": "selected",
         }
    )




