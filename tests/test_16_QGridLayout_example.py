import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_16_QGridLayout_example import QGridLayoutExample

@pytest.fixture
def widget(qtbot):
    w = QGridLayoutExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_grid_layout_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QGridLayout (網格佈局) 範例"
    # Check if the grid has items
    assert widget.layout().count() > 10 # Should have a display + many buttons
