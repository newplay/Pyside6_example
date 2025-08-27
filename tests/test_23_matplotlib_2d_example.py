import sys
import pytest
import numpy as np
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from pytestqt.qtbot import QtBot

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from examples.ex_23_matplotlib_2d_example import Matplotlib2DExample

@pytest.fixture
def widget(qtbot: QtBot):
    """創建並返回 Matplotlib2DExample 元件。"""
    # 確保 QApplication 實例存在
    QApplication.instance() or QApplication([])
    
    test_widget = Matplotlib2DExample()
    qtbot.addWidget(test_widget)
    # 不調用 show() 以避免在無頭 (headless) 測試環境中出現渲染問題
    return test_widget


def test_widget_creation_and_initial_state(widget: Matplotlib2DExample):
    """測試元件創建時的初始狀態是否正確。"""
    # 1. 驗證視窗和圖表標題
    assert widget.windowTitle() == "Matplotlib 2D 範例 - 網格精度與隨機數據"
    assert "隨機數據熱圖" in widget.canvas.ax.get_title()

    # 2. 驗證 UI 控制項的初始值
    assert widget.precision_slider.value() == 100
    assert widget.precision_label.text() == "網格精度: 100x100"

    # 3. 驗證 Matplotlib 圖表的初始狀態
    # 熱圖會創建一個 AxesImage 對象
    assert len(widget.canvas.ax.images) == 1
    
    # 獲取圖像數據並驗證其維度
    initial_data = widget.canvas.ax.images[0].get_array()
    assert initial_data.shape == (100, 100)


def test_refresh_button_changes_data(widget: Matplotlib2DExample, qtbot: QtBot):
    """測試刷新按鈕是否能改變圖表數據，但保持維度不變。"""
    # 獲取初始圖表的數據陣列副本
    initial_data = widget.canvas.ax.images[0].get_array().copy()

    # 模擬點擊刷新按鈕
    qtbot.mouseClick(widget.refresh_button, Qt.LeftButton)

    # 獲取新圖表的數據
    new_data = widget.canvas.ax.images[0].get_array()

    # 斷言數據維度保持不變
    assert new_data.shape == initial_data.shape

    # 斷言數據內容已改變 (由於是隨機數據，幾乎不可能相同)
    assert not np.array_equal(initial_data, new_data)


def test_slider_changes_grid_and_label(widget: Matplotlib2DExample):
    """測試滑桿是否能正確更新標籤和圖表的網格精度。"""
    new_grid_size = 25

    # 程式化設定滑桿的值，這會觸發 valueChanged 信號
    widget.precision_slider.setValue(new_grid_size)

    # 1. 斷言標籤文本已更新
    assert widget.precision_label.text() == f"網格精度: {new_grid_size}x{new_grid_size}"

    # 2. 斷言圖表數據的維度已更新
    # 確認圖表上仍然只有一個 image
    assert len(widget.canvas.ax.images) == 1
    updated_data = widget.canvas.ax.images[0].get_array()
    assert updated_data.shape == (new_grid_size, new_grid_size)