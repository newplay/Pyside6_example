import sys
import os
import pytest
from PySide6.QtWidgets import QApplication

# 將專案根目錄添加到 Python 路徑中，以便 pytest 可以找到 main_app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main_app import MainAppWindow

# --- 動態計算預期範例數量 ---
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
EXPECTED_COUNT = len([f for f in os.listdir(project_root) if f.startswith('ex_') and f.endswith('_example.py')])

@pytest.fixture
def app(qtbot):
    """創建一個應用程式實例，並在測試結束時關閉它。"""
    test_app = MainAppWindow()
    qtbot.addWidget(test_app)
    yield test_app
    test_app.close()

def test_main_app_loading(app):
    """測試主應用程式是否能成功載入所有範例。"""
    print(f"\n動態檢測到 {EXPECTED_COUNT} 個範例檔案。 সন")
    assert app.nav_list.count() == EXPECTED_COUNT
    assert app.stacked_widget.count() == EXPECTED_COUNT
    assert len(app.source_codes) == EXPECTED_COUNT
    print(f"測試通過：所有 {EXPECTED_COUNT} 個範例已成功載入。 সন")

def test_main_app_navigation(app, qtbot):
    """測試點擊導覽列表是否能正確切換內容。"""
    if EXPECTED_COUNT == 0:
        pytest.skip("No examples found to test navigation.")

    print("\n開始導覽測試...")
    
    target_index = min(5, EXPECTED_COUNT - 1)
    print(f"  - 切換到索引 {target_index}...")
    app.nav_list.setCurrentRow(target_index)
    
    assert app.stacked_widget.currentIndex() == target_index
    source_code_for_item = app.source_codes[target_index]
    assert app.source_viewer.toPlainText() == source_code_for_item
    print(f"  - 索引 {target_index} 切換成功。 সন")

    last_index = app.nav_list.count() - 1
    print(f"  - 切換到最後一個索引 {last_index}...")
    app.nav_list.setCurrentRow(last_index)
    
    assert app.stacked_widget.currentIndex() == last_index
    source_code_for_last_item = app.source_codes[last_index]
    assert app.source_viewer.toPlainText() == source_code_for_last_item
    print(f"  - 索引 {last_index} 切換成功。 সন")
    
    print("  - 切換回索引 0...")
    app.nav_list.setCurrentRow(0)
    
    assert app.stacked_widget.currentIndex() == 0
    source_code_for_first_item = app.source_codes[0]
    assert app.source_viewer.toPlainText() == source_code_for_first_item
    print("  - 索引 0 切換成功。 সন")
    
    print("導覽測試通過。 সন")
