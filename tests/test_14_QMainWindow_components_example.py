import sys
import os
import pytest
from unittest.mock import patch
from PySide6.QtWidgets import QMessageBox

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_14_QMainWindow_components_example import MainWindowComponentsExample

@pytest.fixture
def widget(qtbot):
    w = MainWindowComponentsExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qmainwindow_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "主視窗元件範例"

def test_qmainwindow_actions(widget, qtbot):
    # Test new action
    widget.text_edit.setText("some text")
    widget.new_action.trigger()
    assert widget.text_edit.toPlainText() == ""

    # Test save action (mocking the dialog)
    with patch.object(QMessageBox, 'information') as mock_info:
        widget.text_edit.setText("Hello")
        widget.save_action.trigger()
        assert "檔案已儲存" in widget.status_bar.currentMessage()
        mock_info.assert_called_once()
