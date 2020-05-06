import numpy as np

def apply(r, resistances):
    r = fill_left(r, resistances)
    r = fill_right(r, resistances)
    return r


def fill_left(r, resistances):
    (num_rows, num_columns) = resistances.shape
    devices = r[resistances.size:2*resistances.size, :resistances.size]
    horizontal = r[resistances.size:2*resistances.size, resistances.size:2*resistances.size]

    row = np.repeat(np.arange(num_rows), num_columns-1)
    column = np.tile(np.arange(num_columns-1), num_rows)
    horizontal[row*num_columns+column, row*num_columns+column] = -1
    horizontal[row*num_columns+column, row*num_columns+column+1] = 1
    devices[row*num_columns+column, row*num_columns+column] = 1

    # same branches
    horizontal[num_columns-1::num_columns, num_columns-1::num_columns] = -1
    devices[num_columns-1::num_columns, num_columns-1::num_columns] = 1

    return r