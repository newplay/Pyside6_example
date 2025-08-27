import sys
import os
import pytest
from PySide6.QtWidgets import QWidget

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_17_QFormLayout_example import QFormLayoutExample

@pytest.fixture
def widget(qtbot):
    w = QFormLayoutExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_form_layout_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QFormLayout (表單佈局) 範例"
    # Check if the form has rows
    assert widget.findChild(QWidget, "group_box").layout().rowCount() > 0
