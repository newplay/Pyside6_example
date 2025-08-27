import sys
import os
import pytest
from PySide6.QtCore import Qt, QPoint

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_21_Movable_label_example import MovableLabelExample

@pytest.fixture
def widget(qtbot):
    w = MovableLabelExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_movable_label_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "可移動標籤範例"

def test_label_movement(widget, qtbot):
    label = widget.label1
    initial_pos = label.pos()
    
    # 模擬滑鼠拖曳
    start_point = label.mapToGlobal(label.rect().center())
    end_point = start_point + QPoint(50, 50)

    qtbot.mousePress(label, Qt.LeftButton, pos=label.rect().center())
    qtbot.mouseMove(label, pos=end_point)
    qtbot.mouseRelease(label, Qt.LeftButton, pos=end_point)

    # 斷言標籤的位置已改變
    # 注意：由於事件處理的複雜性，精確的最終位置可能難以預測，
    # 但我們可以斷言它不再是初始位置。
    assert label.pos() != initial_pos
