import sys
import os
import pytest
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_01_QLabel_example import QLabelExample

@pytest.fixture
def widget(qtbot):
    """Create and show the QLabelExample widget."""
    w = QLabelExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qlabel_smoke(widget):
    """Smoke test to ensure the widget loads and is visible."""
    assert widget.isVisible()
    assert widget.windowTitle() == "QLabel 範例"

def test_qlabel_interaction(widget, qtbot):
    """Test the button click and checkbox toggle."""
    initial_text = widget.label.text()
    
    # Test button click
    qtbot.mouseClick(widget.update_button, Qt.LeftButton)
    assert widget.label.text() != initial_text
    assert "已被更新 1 次" in widget.label.text()
    
    # Test checkbox
    assert not widget.label.wordWrap()
    qtbot.mouseClick(widget.word_wrap_checkbox, Qt.LeftButton)
    assert widget.label.wordWrap()
