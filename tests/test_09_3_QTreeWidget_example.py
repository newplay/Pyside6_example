import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_09_3_QTreeWidget_example import QTreeWidgetExample

@pytest.fixture
def widget(qtbot):
    w = QTreeWidgetExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qtreewidget_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QTreeWidget 範例"

def test_qtreewidget_interaction(widget, qtbot):
    root = widget.tree_widget.topLevelItem(0)
    assert root is not None
    assert root.childCount() == 3

    # Select an item and check the label
    target_item = root.child(1).child(1) # Pictures -> cat.jpg
    widget.tree_widget.setCurrentItem(target_item)
    assert "cat.jpg" in widget.info_label.text()
    assert "/home/user/Pictures/cat.jpg" in widget.info_label.text()
