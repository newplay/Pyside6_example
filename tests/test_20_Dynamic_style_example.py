import sys
import os
import pytest
from unittest.mock import patch
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QColorDialog
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_20_Dynamic_style_example import DynamicStyleExample

@pytest.fixture
def widget(qtbot):
    w = DynamicStyleExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_dynamic_style_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "動態樣式設定範例"

def test_color_change(widget, qtbot):
    # 模擬選擇紅色為字體顏色
    with patch.object(QColorDialog, 'getColor', return_value=QColor("red")):
        qtbot.mouseClick(widget.text_color_button, Qt.LeftButton)
        text_color = widget.display_label.palette().color(widget.display_label.foregroundRole())
        assert text_color.name() == "#ff0000"

    # 模擬選擇藍色為背景顏色
    with patch.object(QColorDialog, 'getColor', return_value=QColor("blue")):
        qtbot.mouseClick(widget.bg_color_button, Qt.LeftButton)
        bg_color = widget.display_label.palette().color(widget.display_label.backgroundRole())
        assert bg_color.name() == "#0000ff"
