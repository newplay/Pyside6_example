import sys
import os
import pytest
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_09_2_QTableWidget_example import QTableWidgetExample

@pytest.fixture
def widget(qtbot):
    w = QTableWidgetExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qtablewidget_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QTableWidget 範例"

def test_qtablewidget_interaction(widget, qtbot):
    assert widget.table_widget.rowCount() == 4
    qtbot.mouseClick(widget.add_row_button, Qt.LeftButton)
    assert widget.table_widget.rowCount() == 5
    assert widget.table_widget.item(4, 0).text() == "New User"

    widget.table_widget.cellClicked.emit(1, 1) # Bob, C++
    assert "Bob" in widget.info_label.text() or "C++" in widget.info_label.text()
