import sys
import pytest
import numpy as np
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from pytestqt.qtbot import QtBot
from unittest.mock import patch

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from examples.ex_24_matplotlib_3d_example import Matplotlib3DExample

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

    # 斷言基礎數據 Z_base 本身沒有被修改
    assert np.array_equal(widget.Z_base, z_base_copy), "基礎數據不應被噪聲函式修改"
    
    # 從圖形集合中獲取實際繪製的頂點數據
    # ax.collections[0] 是 Poly3DCollection
    collection = widget.canvas.ax.collections[0]
    
    # get_verts() 返回一個列表，每個元素是面(一個四邊形)的頂點
    # 每個頂點是 [x, y, z]。我們提取每個面第一個頂點的 z 值作為代表
    # 這足以驗證數據是否被修改
        # 使用 patch 監聽 canvas.plot 方法的調用
    with patch.object(widget.canvas, 'plot') as mock_plot:
        # 點擊刷新按鈕
        qtbot.mouseClick(widget.refresh_button, Qt.LeftButton)

        # 斷言 canvas.plot 被調用
        mock_plot.assert_called_once()

        # 獲取傳遞給 plot 方法的 Z 數據
        # plot 方法的簽名是 plot(self, X, Y, Z)
        # 所以 Z 數據是第三個位置參數 (索引為 2)
        _, _, plotted_z_coords = mock_plot.call_args[0]

        # 斷言基礎數據 Z_base 本身沒有被修改
        assert np.array_equal(widget.Z_base, z_base_copy), "基礎數據不應被噪聲函式修改"

        # 斷言繪製出的 Z 座標與原始基礎數據不相等，證明噪聲已應用
        assert not np.array_equal(plotted_z_coords, z_base_copy), "繪製的 Z 座標應與原始數據不同"

    # 獲取與繪製的面對應的原始 Z 數據
    # plot_surface 使用 Z[:-1, :-1] 來決定面的顏色和位置
    base_z_coords = z_base_copy

    # 斷言繪製出的 Z 座標與原始基礎數據不相等，證明噪聲已應用
    assert not np.array_equal(plotted_z_coords, base_z_coords), "繪製的 Z 座標應與原始數據不同"
