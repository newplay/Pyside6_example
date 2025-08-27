import sys
import os
import pytest
from unittest.mock import patch
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_12_QFileDialog_example import QFileDialogExample

@pytest.fixture
def widget(qtbot):
    w = QFileDialogExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qfiledialog_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QFileDialog 範例"

# Patch the dialog methods to avoid GUI interaction in tests

def test_qfiledialog_interaction(widget, qtbot):
    test_path = '/tmp/test_file.txt'
    with patch.object(QFileDialog, 'getOpenFileName', return_value=(test_path, 'All Files (*)')):
        qtbot.mouseClick(widget.open_file_button, Qt.LeftButton)
        assert test_path in widget.result_display.toPlainText()

    with patch.object(QFileDialog, 'getSaveFileName', return_value=(test_path, 'All Files (*)')):
        qtbot.mouseClick(widget.save_file_button, Qt.LeftButton)
        assert test_path in widget.result_display.toPlainText()
