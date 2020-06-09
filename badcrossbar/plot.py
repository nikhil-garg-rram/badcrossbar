import cairo
import numpy as np
import badcrossbar.plotting.utils as utils
import badcrossbar.plotting.crossbar as crossbar


def currents(device_currents, word_line_currents, bit_line_currents):
    WIDTH, HEIGHT = 1000, 1000
    surface = cairo.PDFSurface('crossbar_currents.pdf', WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    x_start, y_start = 50, 50
    segment_length = 120
    low, high = utils.arrays_range(
        device_currents, word_line_currents, bit_line_currents)

    bit_lines(ctx, bit_line_currents, x_start, y_start, low, high,
              segment_length=segment_length, width=3)

    word_lines(ctx, word_line_currents, x_start, y_start, low, high,
               segment_length=segment_length, width=3)

    devices(ctx, device_currents, x_start, y_start, low, high,
            segment_length=segment_length, width=3, node_color=(0, 0, 0),
            node_diameter=7)


def bit_lines(context, bit_line_currents, x_start, y_start, low, high,
              segment_length=120, width=3):
    x, y = x_start + 1.5*segment_length, y_start + 0.5*segment_length
    context.move_to(x, y)

    for bit_line in np.transpose(bit_line_currents):
        colors = utils.rgb_interpolation(bit_line, low=low, high=high)
        crossbar.bit_line(context, colors, width=width)
        x += segment_length
        context.move_to(x, y)

    context.move_to(x_start, y_start)


def word_lines(context, word_line_currents, x_start, y_start, low, high,
              segment_length=120, width=3):
    x, y = x_start, y_start
    context.move_to(x, y)

    for idx, word_line in enumerate(word_line_currents):
        colors = utils.rgb_interpolation(word_line, low=low, high=high)
        if idx == 0:
            crossbar.word_line(context, colors, width=width, first=True)
        else:
            crossbar.word_line(context, colors, width=width)
        y += segment_length
        context.move_to(x, y)

    context.move_to(x_start, y_start)


def devices(context, device_currents, x_start, y_start, low, high,
            segment_length=120, width=3, node_color=(0, 0, 0),
            node_diameter=7):
    x, y = x_start, y_start
    context.move_to(x, y)
    for device_row in device_currents:
        colors = utils.rgb_interpolation(device_row, low=low, high=high)
        crossbar.device_row(context, colors, width=width)

        colors = utils.rgb_interpolation(np.zeros(device_row.shape),
                                         low_rgb=node_color)
        context.move_to(x, y)
        crossbar.nodes(context, colors, diameter=node_diameter,
                       bit_line_nodes=True)
        context.move_to(x, y)
        crossbar.nodes(context, colors, diameter=node_diameter,
                       bit_line_nodes=False)
        y += segment_length
        context.move_to(x, y)

    context.move_to(x_start, y_start)