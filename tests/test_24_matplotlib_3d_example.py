import sys
import pytest
import numpy as np
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from pytestqt.qtbot import QtBot

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ex_24_matplotlib_3d_example import Matplotlib3DExample

@pytest.fixture
def widget(qtbot: QtBot):
    """創建並返回 Matplotlib3DExample 元件。"""
    app = QApplication.instance() or QApplication(sys.argv)
    widget = Matplotlib3DExample()
    qtbot.addWidget(widget)
    # 不調用 show() 以避免在無頭環境中出現渲染問題
    return widget

def test_ex24_widget_creation(widget: Matplotlib3DExample):
    """測試元件及其子元件是否能被成功創建和配置。"""
    assert widget is not None
    assert widget.windowTitle() == "Matplotlib 3D 範例"
    assert widget.canvas is not None
    assert widget.resolution_slider is not None
    assert widget.refresh_button is not None
    assert widget.canvas.ax.name == '3d'

def test_ex24_slider_changes_resolution(widget: Matplotlib3DExample, qtbot: QtBot):
    """測試滑桿是否能改變圖形解析度。"""
    # 獲取初始的 Z 數據點數量
    initial_points = widget.Z_base.size

    # 移動滑桿到一個新位置
    with qtbot.waitSignal(widget.resolution_slider.valueChanged, raising=True):
        widget.resolution_slider.setValue(50)

    # 獲取新的 Z 數據點數量
    new_points = widget.Z_base.size

    assert new_points != initial_points

def test_ex24_refresh_button_adds_noise(widget: Matplotlib3DExample, qtbot: QtBot):
    """測試刷新按鈕是否為圖形添加了噪聲。"""
    # 獲取初始的 Z 數據 (無噪聲)
    z_base_copy = np.copy(widget.Z_base)
    
    # 點擊刷新按鈕
    qtbot.mouseClick(widget.refresh_button, Qt.LeftButton)

    # 獲取圖形上當前的 Z 數據 (應該是帶有噪聲的)
    # 我們需要從 canvas 的 collections 中獲取數據
    current_z_data = widget.canvas.ax.collections[0].get_array()

    # 斷言基礎數據 Z_base 沒有被修改
    assert np.array_equal(widget.Z_base, z_base_copy)
    
    # 斷言當前繪製的數據與基礎數據不相等 (因為添加了噪聲)
    # 由於數據是一維數組，需要將 z_base_copy 攤平進行比較
    assert not np.array_equal(current_z_data, z_base_copy.ravel())
