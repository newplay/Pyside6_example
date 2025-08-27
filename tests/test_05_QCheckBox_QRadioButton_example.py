import sys
import os
import pytest
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_05_QCheckBox_QRadioButton_example import CheckRadioExample

@pytest.fixture
def widget(qtbot):
    w = CheckRadioExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_checkradio_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QCheckBox & QRadioButton 範例"

def test_checkradio_interaction(widget, qtbot):
    assert "macOS" in widget.result_label.text()
    assert "無" in widget.result_label.text()

    widget.checkbox1.setChecked(True)
    # In a test environment, it's more reliable to call the update slot directly
    # after changing the state programmatically.
    widget.update_selection()
    assert "寫程式" in widget.result_label.text()

    widget.radio3.setChecked(True)
    widget.update_selection()
    assert "Linux" in widget.result_label.text()