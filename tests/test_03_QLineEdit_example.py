import sys
import os
import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_03_QLineEdit_example import QLineEditExample

@pytest.fixture
def widget(qtbot):
    w = QLineEditExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qlineedit_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QLineEdit 範例"

def test_qlineedit_interaction(widget, qtbot):
    qtbot.keyClicks(widget.line_edit, "Hello")
    assert widget.display_label.text() == "Hello"

    # Test echo mode change
    assert widget.line_edit.echoMode() == QLineEdit.Normal
    qtbot.keyClick(widget.echo_mode_combo, Qt.Key_Down) # Select next item (Password)
    assert widget.line_edit.echoMode() == QLineEdit.Password
() == QLineEdit.Password
