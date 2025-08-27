import sys
import os
import pytest
from PySide6.QtWidgets import QWidget

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_15_VBoxLayout_HBoxLayout_example import VBoxLayoutHBoxLayoutExample

@pytest.fixture
def widget(qtbot):
    w = VBoxLayoutHBoxLayoutExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_box_layout_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "基礎佈局 (VBox & HBox) 範例"
    # Basic check if layouts contain widgets
    assert widget.findChild(QWidget, "hbox_group").layout().count() > 0
    assert widget.findChild(QWidget, "vbox_group").layout().count() > 0
    assert widget.findChild(QWidget, "nested_group").layout().count() > 0