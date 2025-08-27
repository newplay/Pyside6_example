import sys
import os
import pytest
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_09_1_QListWidget_example import QListWidgetExample

@pytest.fixture
def widget(qtbot):
    w = QListWidgetExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qlistwidget_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QListWidget 範例"

def test_qlistwidget_interaction(widget, qtbot):
    assert widget.list_widget.count() == 5
    
    widget.item_input.setText("New Task")
    qtbot.mouseClick(widget.add_button, Qt.LeftButton)
    assert widget.list_widget.count() == 6
    assert widget.list_widget.item(5).text() == "New Task"

    widget.list_widget.setCurrentRow(2)
    qtbot.mouseClick(widget.delete_button, Qt.LeftButton)
    assert widget.list_widget.count() == 5
    assert "設計 UI" not in [widget.list_widget.item(i).text() for i in range(5)]
