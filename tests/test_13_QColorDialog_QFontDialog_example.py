import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QColorDialog, QFontDialog
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex_13_QColorDialog_QFontDialog_example import ColorFontDialogExample

@pytest.fixture
def widget(qtbot):
    w = ColorFontDialogExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_colordialog_fontdialog_smoke(widget):
    assert widget.isVisible()

def test_dialog_interaction(widget, qtbot):
    # Test color dialog
    test_color = QColor("#ff0000")
    with patch.object(QColorDialog, 'getColor', return_value=test_color):
        qtbot.mouseClick(widget.change_color_button, Qt.LeftButton)
        assert "ff0000" in widget.display_label.styleSheet()

    # Test font dialog by patching the instance methods
    test_font = QFont("Comic Sans MS", 24)
    with patch('ex_13_QColorDialog_QFontDialog_example.QFontDialog') as mock_dialog_class:
        # Configure the mock instance that will be created
        mock_instance = MagicMock()
        mock_instance.exec.return_value = True
        mock_instance.selectedFont.return_value = test_font
        mock_dialog_class.return_value = mock_instance

        qtbot.mouseClick(widget.change_font_button, Qt.LeftButton)
        
        assert widget.display_label.font().family() == "Comic Sans MS"
        assert widget.display_label.font().pointSize() == 24