import sys
import os
import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_19_QLineEdit_validation_example import QLineEditValidationExample

@pytest.fixture
def widget(qtbot):
    w = QLineEditValidationExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_validation_smoke(widget):
    """Smoke test to ensure the widget loads."""
    assert widget.isVisible()
    assert widget.windowTitle() == "QLineEdit 進階驗證範例"

def test_max_length(widget, qtbot):
    """Test the setMaxLength functionality."""
    line_edit = widget.findChild(QLineEdit) # 找到第一個 QLineEdit
    qtbot.keyClicks(line_edit, "1234567890123")
    assert line_edit.text() == "1234567890"

def test_int_validator(widget, qtbot):
    """Test the QIntValidator functionality."""
    # 找到第二個 QLineEdit
    line_edits = widget.findChildren(QLineEdit)
    int_edit = line_edits[1]
    
    qtbot.keyClicks(int_edit, "123a456")
    assert int_edit.text() == "123" # 'a' and subsequent chars should be rejected
    
    int_edit.setText("") # Clear
    qtbot.keyClicks(int_edit, "1500")
    assert int_edit.text() == "150" # '0' should be rejected as it's out of range (0-999)

def test_input_mask(widget, qtbot):
    """Test the setInputMask functionality."""
    line_edits = widget.findChildren(QLineEdit)
    mask_edit = line_edits[2]
    
    qtbot.keyClicks(mask_edit, "12AB34CD56EF")
    assert mask_edit.text() == "12:AB:34:CD:56:EF"
