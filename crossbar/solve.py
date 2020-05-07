from scipy.sparse import linalg
from crossbar import display


def i(r, v):
    """Solves matrix equation ri = v.

    :param r: r matrix.
    :param v: v matrix.
    :return: Currents in each branch of the crossbar.
    """
    display.message('Started solving for i.')
    i_matrix = linalg.spsolve(r.tocsc(), v)  # converts lil_matrix to csc_matrix before solving
    display.message('Solved for i.')
    return i_matrix
