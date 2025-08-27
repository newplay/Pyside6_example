import sys
import os
import pytest
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_06_QComboBox_example import QComboBoxExample

@pytest.fixture
def widget(qtbot):
    w = QComboBoxExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qcombobox_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QComboBox 範例"

def test_qcombobox_interaction(widget, qtbot):
    assert "Python" in widget.result_label.text()
    
    # Change selection
    widget.combo_box.setCurrentIndex(2) # C++
    assert "C++" in widget.result_label.text()

    # Test adding item
    assert widget.combo_box.count() == 6 # 5 items + 1 separator
    qtbot.mouseClick(widget.add_item_button, Qt.LeftButton)
    assert widget.combo_box.count() == 7
    assert widget.combo_box.itemText(6) == "Go"
