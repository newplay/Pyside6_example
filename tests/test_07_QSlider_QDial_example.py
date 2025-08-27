import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.ex_07_QSlider_QDial_example import SliderDialExample

@pytest.fixture
def widget(qtbot):
    w = SliderDialExample()
    qtbot.addWidget(w)
    w.show()
    return w

def test_qslider_qdial_smoke(widget):
    assert widget.isVisible()
    assert widget.windowTitle() == "QSlider & QDial 範例"

def test_qslider_qdial_interaction(widget, qtbot):
    assert "25" in widget.value_label.text()

    widget.slider.setValue(80)
    assert "80" in widget.value_label.text()
    assert widget.dial.value() == 80
    assert widget.progress_bar.value() == 80

    widget.dial.setValue(10)
    assert "10" in widget.value_label.text()
    assert widget.slider.value() == 10
