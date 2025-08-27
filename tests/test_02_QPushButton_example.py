import sys
import os
import pytest
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_02_QPushButton_example import QPushButtonExample

@pytest.fixture
def widget(qtbot):
    w = QPushButtonExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qpushbutton_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QPushButton 範例"

def test_qpushbutton_interaction(widget, qtbot):
    assert widget.count_label.text() == "點擊次數: 0"
    qtbot.mouseClick(widget.main_button, Qt.LeftButton)
    assert widget.count_label.text() == "點擊次數: 1"

    # Test checkable
    assert not widget.main_button.isCheckable()
    qtbot.mouseClick(widget.checkable_checkbox, Qt.LeftButton)
    assert widget.main_button.isCheckable()
    assert "未被勾選" in widget.checkable_status_label.text()
    qtbot.mouseClick(widget.main_button, Qt.LeftButton)
    assert widget.main_button.isChecked()
    assert "已勾選" in widget.checkable_status_label.text()
