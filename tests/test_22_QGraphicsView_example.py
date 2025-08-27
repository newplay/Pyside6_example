import sys
import os
import pytest
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsTextItem

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_22_QGraphicsView_example import QGraphicsViewExample

@pytest.fixture
def widget(qtbot):
    w = QGraphicsViewExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qgraphicsview_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "2D 圖形視圖 (QGraphicsView) 範例"

def test_scene_items(widget):
    """Test if the scene contains the correct number and types of items."""
    scene = widget.scene
    items = scene.items()
    
    # 應該有 3 個項目
    assert len(items) == 3
    
    # 檢查各類項目的數量
    rect_count = sum(1 for item in items if isinstance(item, QGraphicsRectItem))
    ellipse_count = sum(1 for item in items if isinstance(item, QGraphicsEllipseItem))
    text_count = sum(1 for item in items if isinstance(item, QGraphicsTextItem))
    
    assert rect_count == 1
    assert ellipse_count == 1
    assert text_count == 1
