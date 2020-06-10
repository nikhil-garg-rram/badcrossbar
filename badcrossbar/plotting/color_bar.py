import cairo
import numpy as np
from badcrossbar import plotting as plotting


def draw(ctx, color_bar_dims, low, high):
    ctx.rectangle(*color_bar_dims)
    pattern = cairo.LinearGradient(color_bar_dims[0], color_bar_dims[1],
                                   color_bar_dims[0] + color_bar_dims[2],
                                   color_bar_dims[1] + color_bar_dims[3])

    top_rgb = plotting.utils.rgb_interpolation(
        np.array([high]), low=low, high=high)[0]
    if low != high:
        middle_rgb = plotting.utils.rgb_interpolation(
            np.array([0]), low=low, high=high)[0]
    else:
        middle_rgb = plotting.utils.rgb_interpolation(
            np.array([0]), low=-1, high=1)[0]
    bottom_rgb = plotting.utils.rgb_interpolation(
        np.array([low]), low=low, high=high)[0]

    ctx.set_source_rgb(0, 0, 0)
    font_size = color_bar_dims[2]/2.5
    ctx.set_font_size(font_size)

    if low < 0 < high:
        pattern.add_color_stop_rgb(0, *top_rgb)
        pattern.add_color_stop_rgb(0.5, *middle_rgb)
        pattern.add_color_stop_rgb(1, *bottom_rgb)

        x = color_bar_dims[0] + color_bar_dims[2]*1.2
        y = color_bar_dims[1] + 0.5*font_size
        ctx.move_to(x, y)
        ctx.show_text(str(high))

        x = color_bar_dims[0] + color_bar_dims[2]*1.2
        y = color_bar_dims[1] + 0.5*color_bar_dims[3] + 0.5*font_size
        ctx.move_to(x, y)
        ctx.show_text(str(0))

        x = color_bar_dims[0] + color_bar_dims[2]*1.2
        y = color_bar_dims[1] + color_bar_dims[3] + 0.5*font_size
        ctx.move_to(x, y)
        ctx.show_text(str(low))
    else:
        if high > 0:
            pattern.add_color_stop_rgb(0, *top_rgb)
            pattern.add_color_stop_rgb(1, *middle_rgb)

            x = color_bar_dims[0] + color_bar_dims[2]*1.2
            y = color_bar_dims[1] + 0.5*font_size
            ctx.move_to(x, y)
            ctx.show_text(str(high))

            x = color_bar_dims[0] + color_bar_dims[2]*1.2
            y = color_bar_dims[1] + color_bar_dims[3] + 0.5*font_size
            ctx.move_to(x, y)
            ctx.show_text(str(0))
        else:
            pattern.add_color_stop_rgb(0, *middle_rgb)
            pattern.add_color_stop_rgb(1, *bottom_rgb)

            x = color_bar_dims[0] + color_bar_dims[2]*1.2
            y = color_bar_dims[1] + 0.5*font_size
            ctx.move_to(x, y)
            ctx.show_text(str(0))

            x = color_bar_dims[0] + color_bar_dims[2]*1.2
            y = color_bar_dims[1] + color_bar_dims[3] + 0.5*font_size
            ctx.move_to(x, y)
            ctx.show_text(str(low))

    ctx.set_source(pattern)
    ctx.fill()

    font_size *= 1.5
    ctx.set_font_size(font_size)
    ctx.set_source_rgb(0, 0, 0)
    angle = np.pi/2

    _, _, width, height, _, _ = ctx.text_extents('Current (A)')
    x = color_bar_dims[0] + 2*color_bar_dims[2] + height
    y = color_bar_dims[1] + 0.5*color_bar_dims[3] + 0.5*width
    ctx.move_to(x, y)

    ctx.rotate(-angle)
    ctx.show_text('Current (A)')
    ctx.rotate(angle)


def dimensions(surface_dims, color_bar_fraction, border_fraction):
    height = np.max(surface_dims) * color_bar_fraction[0]
    width = np.max(surface_dims) * color_bar_fraction[1] / 4
    x_start = surface_dims[0] * (1 - border_fraction) - 3 * width
    y_start = surface_dims[1] * 0.5 - height / 2
    color_bar_dims = (x_start, y_start, width, height)
    return color_bar_dims