import pytest
from ligotools import utils
import numpy as np


def test_reqshift():
    x = np.arange(1, 20)
    output = utils.reqshift(x)
    assert len(output) == 18

def test_reqshift2():
    x = np.arange(1, 100)
    output = utils.reqshift(x)
    assert len(output) == 98