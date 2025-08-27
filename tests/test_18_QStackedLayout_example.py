import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_18_QStackedLayout_example import QStackedLayoutExample

@pytest.fixture
def widget(qtbot):
    w = QStackedLayoutExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_stacked_layout_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QStackedLayout (堆疊佈局) 範例"

def test_stacked_layout_interaction(widget, qtbot):
    assert widget.stacked_layout.currentIndex() == 0

    # Switch to page 2
    widget.nav_list.setCurrentRow(1)
    assert widget.stacked_layout.currentIndex() == 1
    assert widget.stacked_layout.widget(1) is widget.page2

    # Switch to page 3
    widget.nav_list.setCurrentRow(2)
    assert widget.stacked_layout.currentIndex() == 2
    assert widget.stacked_layout.widget(2) is widget.page3
