import sys
import os
import pytest
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_08_QProgressBar_example import QProgressBarExample

@pytest.fixture
def widget(qtbot):
    w = QProgressBarExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qprogressbar_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QProgressBar 範例"

def test_qprogressbar_interaction(widget, qtbot):
    assert widget.progress_bar.value() == 0

    qtbot.mouseClick(widget.start_button, Qt.LeftButton)
    # Wait for the timer to run a few times
    qtbot.wait(550) # Wait for 5 steps
    assert widget.progress_bar.value() > 0

    qtbot.mouseClick(widget.reset_button, Qt.LeftButton)
    assert widget.progress_bar.value() == 0
