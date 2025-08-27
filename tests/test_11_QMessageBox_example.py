import sys
import os
import pytest
from unittest.mock import patch
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_11_QMessageBox_example import QMessageBoxExample

@pytest.fixture
def widget(qtbot):
    w = QMessageBoxExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qmessagebox_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QMessageBox 範例"

# We need to 'patch' the QMessageBox static methods so they don't block the test runner

def test_qmessagebox_interaction(widget, qtbot):
    with patch.object(QMessageBox, 'question', return_value=QMessageBox.Yes) as mock_question:
        qtbot.mouseClick(widget.question_button, Qt.LeftButton)
        mock_question.assert_called_once()
        assert "Yes" in widget.result_label.text()

    with patch.object(QMessageBox, 'information') as mock_info:
        qtbot.mouseClick(widget.info_button, Qt.LeftButton)
        mock_info.assert_called_once()
        assert "資訊框已顯示" in widget.result_label.text()
