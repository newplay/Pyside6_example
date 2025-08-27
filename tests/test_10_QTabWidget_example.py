import sys
import os
import pytest
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_10_QTabWidget_example import QTabWidgetExample

@pytest.fixture
def widget(qtbot):
    w = QTabWidgetExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qtabwidget_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QTabWidget 範例"

def test_qtabwidget_interaction(widget, qtbot):
    assert widget.tab_widget.count() == 3
    assert widget.tab_widget.currentIndex() == 0

    qtbot.mouseClick(widget.add_tab_button, Qt.LeftButton)
    assert widget.tab_widget.count() == 4
    assert widget.tab_widget.currentIndex() == 3 # Should switch to new tab

    widget.tab_widget.setCurrentIndex(1)
    assert "使用者資料" in widget.info_label.text()

    qtbot.mouseClick(widget.remove_tab_button, Qt.LeftButton)
    assert widget.tab_widget.count() == 3
