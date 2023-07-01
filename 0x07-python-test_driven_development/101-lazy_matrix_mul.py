#!/usr/bin/python3

import numpy as np

"""
mul matrix using numpy
"""


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices

    Args:
        m_a: 1st matrix
        m_b: 2nd matrix
    """
    try:
        m_a = np.array(m_a)
        m_b = np.array(m_b)

        result = np.matmul(m_a, m_b)
        return result
    except Exception:
        raise TypeError("Failed multiplies 2 matrices")
