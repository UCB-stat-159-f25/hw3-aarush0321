import pytest
from ligotools import readligo
import numpy as np

def test_dq_channel_to_seglist():
    channel = np.array([0, 1, 0, 1, 1, 0, 1, 0])
    segs = readligo.dq_channel_to_seglist(channel)
    assert len(segs) == 3


def test_dq_channel_to_seglist_invalid():
    channel_dict = {
        "DAT": [1, 2, 3, 4], 
    }

    with pytest.raises((KeyError, ValueError, AttributeError, TypeError)):
        readligo.dq_channel_to_seglist(channel_dict)