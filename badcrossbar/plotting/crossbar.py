import numpy as np
import badcrossbar.plotting.shapes as shapes
import badcrossbar.plotting.utils as utils


def word_line(context, colors, width=1, segment_length=120, first=False):
    """Draws a word line of a crossbar array.

    Parameters
    ----------
    context : cairo.Context
        Context.
    colors : list of tuple of int
        Colors of the bit line segments in RGB (max value of 255).
    width : float
        Width of the path.
    segment_length : float
        The length of each segment.
    first : bool
        If True, draws the first (from the top) word line.
    """
    for idx, color in enumerate(colors):
        if idx == 0 or first:
            shapes.line(context, segment_length)
        else:
            unit = segment_length/4
            shapes.line(context, 1.5*unit)
            shapes.semicircle(context, unit)
            shapes.line(context, 1.5*unit)

        utils.complete_path(context, rgb=color, width=width)


def bit_line(context, colors, width=1, segment_length=120):
    """Draws a bit line of a crossbar array.

    Parameters
    ----------
    context : cairo.Context
        Context.
    colors : list of tuple of int
        Colors of the bit line segments in RGB (max value of 255).
    width : float
        Width of the path.
    segment_length : float
        The length of each segment.
    """
    for idx, color in enumerate(colors):
        shapes.line(context, segment_length, angle=np.pi/2)
        utils.complete_path(context, rgb=color, width=width)
