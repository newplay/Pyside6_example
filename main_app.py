import sys
import os
import importlib
import inspect
import traceback
import tempfile
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QStackedWidget,
    QListWidgetItem,
    QTextEdit,
    QSplitter,
    QPushButton,
    QMessageBox,
)
import platform # + 新增導入
from PySide6.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat, QColor,QFontDatabase
from PySide6.QtCore import Qt

# {{ modifications, a C-style code block }}
# + --- Pygments 語法高亮 ---
# + 導入 Pygments 相關模塊
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token, Comment, Keyword, Name, String, Number, Operator

class PythonSyntaxHighlighter(QSyntaxHighlighter):
    """
    一個使用 Pygments 實現的 Python 語法高亮器。
    採用了更豐富的 token 類型和優化的顏色主題，以提高可讀性。
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.lexer = PythonLexer()

        # 基於 Solarized Light 主題的顏色，針對白色背景進行了調整，確保對比度
        self.formats = {
            Comment: self.create_format(QColor("#839496"), italic=True),          # 灰色註解
            Keyword: self.create_format(QColor("#859900")),                     # 綠色關鍵字
            Keyword.Constant: self.create_format(QColor("#b58900")),            # 橙色常量 (True, False, None)
            Keyword.Namespace: self.create_format(QColor("#cb4b16"), bold=True), # 粗體橙色 (import, from)

            Name.Builtin: self.create_format(QColor("#b58900")),                 # 橙色內建函數
            Name.Function: self.create_format(QColor("#268bd2")),                # 藍色函數名
            Name.Class: self.create_format(QColor("#268bd2"), bold=True),        # 粗體藍色類名
            Name.Decorator: self.create_format(QColor("#2aa198"), italic=True),  # 青色斜體裝飾器
            Name.Exception: self.create_format(QColor("#cb4b16")),               # 橙色異常

            Operator: self.create_format(QColor("#6c71c4")),                    # 紫色運算符

            Number: self.create_format(QColor("#d33682")),                      # 洋紅色數字

            String: self.create_format(QColor("#2aa198")),                      # 青色字符串
            String.Doc: self.create_format(QColor("#839496"), italic=True),      # 灰色斜體文檔字符串
        }

        # 預設格式 (用於普通變數名等)
        self.default_format = self.create_format(QColor("#000000")) # 黑色

    def create_format(self, color, bold=False, italic=False):
        """創建一個 QTextCharFormat。"""
        fmt = QTextCharFormat()
        fmt.setForeground(color)
        if bold:
            fmt.setFontWeight(QFont.Bold)
        if italic:
            fmt.setFontItalic(italic)
        return fmt

    def highlightBlock(self, text):
        """
        在文本塊上應用高亮。
        此方法通過遍歷 token 的父類型來查找最匹配的格式，
        從而支持更精確的高亮顯示。
        """
        # 使用 Pygments 進行詞法分析
        tokens = self.lexer.get_tokens_unprocessed(text)
        
        for index, token_type, token_text in tokens:
            # 遍歷 token 類型繼承鏈，找到最匹配的格式
            current_token_type = token_type
            fmt = None
            while current_token_type is not Token:
                fmt = self.formats.get(current_token_type)
                if fmt:
                    break
                current_token_type = current_token_type.parent
            
            if not fmt:
                fmt = self.default_format
            
            self.setFormat(index, len(token_text), fmt)

class MainAppWindow(QMainWindow):
    """主應用程式視窗，用於瀏覽所有 PySide6 範例。"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 範例瀏覽器")
        self.setGeometry(100, 100, 1400, 800) # 擴大視窗以容納更多內容
        self._initial_show = True

        self.nav_list = QListWidget()
        self.nav_list.setFixedWidth(250) # 稍微加寬
        
        self.stacked_widget = QStackedWidget()

# {{ modifications, a C-style code block }}
# - self.source_viewer = QTextEdit()
# - self.source_viewer.setReadOnly(True)
# - self.source_viewer.setFont(QFont("Courier New", 11))
# - self.source_viewer.setLineWrapMode(QTextEdit.NoWrap)
# + 創建可編輯的程式碼編輯器和執行按鈕
        self.source_viewer = QTextEdit()

        font_name = self._find_best_font()
        self.source_viewer.setFont(QFont(font_name, 11))
        self.source_viewer.setLineWrapMode(QTextEdit.NoWrap)
        
        # 應用語法高亮
        self.highlighter = PythonSyntaxHighlighter(self.source_viewer.document())

        self.run_button = QPushButton("執行修改 (Ctrl+R)")
        self.run_button.setShortcut("Ctrl+R")
        
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.source_viewer)
        right_layout.addWidget(self.run_button)
        
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
# {{ end modifications }}
        
        main_splitter = QSplitter(Qt.Horizontal)
        main_splitter.addWidget(self.nav_list)
        main_splitter.addWidget(self.stacked_widget)
# {{ modifications, a C-style code block }}
# - main_splitter.addWidget(self.source_viewer)
# + 將包含編輯器和按鈕的 widget 加入分割器
        main_splitter.addWidget(right_widget)
# {{ end modifications }}
        main_splitter.setStretchFactor(1, 1)
        main_splitter.setStretchFactor(2, 1)

        self.setCentralWidget(main_splitter)

        self.source_codes = []
        self.load_examples()

        self.nav_list.currentRowChanged.connect(self.stacked_widget.setCurrentIndex)
        self.nav_list.currentRowChanged.connect(self.display_source_code)
# {{ modifications, a C-style code block }}
# + 連接執行按鈕的信號
        self.run_button.clicked.connect(self.execute_edited_code)
# {{ end modifications }}
    def _find_best_font(self):
        """
        檢測操作系統並從優先級列表中返回第一個可用的、支持中文的字體。
        優先選擇支持繁體中文的字體。
        """
        
        os_system = platform.system()

        if os_system == "Windows":
            # 微軟正黑體 (繁體) > 微軟雅黑 (簡體) > 黑體 (簡體)
            font_preferences = ["Microsoft JhengHei", "Microsoft YaHei", "SimHei"]
        elif os_system == "Darwin": # macOS
            # 蘋方-繁 > 黑體-繁
            font_preferences = ["PingFang TC", "Heiti TC"]
        else: # Linux
            # Noto (Google) > 文泉驛
            font_preferences = ["Noto Sans CJK TC", "WenQuanYi Zen Hei", "WenQuanYi Micro Hei"]
        
        for font_name in font_preferences:
            if font_name in QFontDatabase.families():
                print(f"字體查找：找到並使用 '{font_name}'")
                return font_name
        
        # 如果上面都找不到，返回一個通用名稱，讓系統自己決定
        print("字體查找：未找到任何偏好字體，使用通用 'sans-serif'。")
        return "sans-serif"
    def showEvent(self, event):
        super().showEvent(event)
        if self._initial_show and self.nav_list.count() > 0:
            self.nav_list.setCurrentRow(0)
            self._initial_show = False

    def load_examples(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        examples_dir = os.path.join(current_dir, 'examples')
        if not os.path.isdir(examples_dir):
            return
        example_files = sorted([f for f in os.listdir(examples_dir) if f.startswith('ex_') and f.endswith('_example.py')])

        for file_name in example_files:
            module_name = file_name[:-3]
            file_path = os.path.join(examples_dir, file_name)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    source_code = f.read()
                self.source_codes.append(source_code)

                module = importlib.import_module(f"examples.{module_name}")
                
                target_class = None
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if (issubclass(obj, QWidget) and obj is not QWidget and obj.__module__ == module.__name__):
                        target_class = obj
                
                if target_class:
                    widget_instance = target_class()
                    self.stacked_widget.addWidget(widget_instance)
                    
                    title = module_name.replace('_example', '').replace('_', ' ').replace('Q', ' Q').strip()
                    # ... (省略了一些不影響功能的 title 格式化代碼)
                    
# {{ modifications, a C-style code block }}
# - self.nav_list.addItem(QListWidgetItem(title))
# + 創建 QListWidgetItem 並綁定模組名
                    item = QListWidgetItem(title)
                    item.setData(Qt.UserRole, module_name) # 綁定原始模組名
                    self.nav_list.addItem(item)
# {{ end modifications }}
                else:
                    self.source_codes.pop()
                    print(f"警告: 在 {module_name} 中未找到自訂的 QWidget 子類。")

            except Exception as e:
                print(f"錯誤: 處理檔案 {file_name} 時發生問題。原因: {e}")

    def display_source_code(self, index):
        if 0 <= index < len(self.source_codes):
            self.source_viewer.setText(self.source_codes[index])

# {{ modifications, a C-style code block }}
# + 新增執行編輯後程式碼的方法
    def execute_edited_code(self):
        """
        將編輯器中的程式碼寫入臨時文件，動態加載並替換當前的範例元件。
        """
        current_row = self.nav_list.currentRow()
        if current_row < 0:
            return

        edited_code = self.source_viewer.toPlainText()
        
        # 獲取原始模組名，用於從 sys.modules 中清理
        original_module_name = self.nav_list.item(current_row).data(Qt.UserRole)

        temp_dir = None
        try:
            # 使用 TemporaryDirectory 確保目錄和文件在結束後被清理
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_file_path = os.path.join(temp_dir, "temp_module.py")
                with open(temp_file_path, 'w', encoding='utf-8') as f:
                    f.write(edited_code)

                # 將臨時目錄加入 sys.path
                if temp_dir not in sys.path:
                    sys.path.insert(0, temp_dir)

                # 清理舊模組的快取，以確保能加載新程式碼
                if original_module_name in sys.modules:
                    del sys.modules[original_module_name]
                if "temp_module" in sys.modules:
                    del sys.modules["temp_module"]

                # 動態導入臨時模組
                module = importlib.import_module("temp_module")

                # 在新模組中查找 QWidget 子類
                target_class = None
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, QWidget) and obj is not QWidget and obj.__module__ == module.__name__:
                        target_class = obj
                        break
                
                if not target_class:
                    raise RuntimeError("在編輯後的程式碼中未找到有效的 QWidget 子類。")

                # --- 替換元件 ---
                old_widget = self.stacked_widget.widget(current_row)
                self.stacked_widget.removeWidget(old_widget)
                old_widget.deleteLater() # 安全銷毀

                new_widget = target_class()
                self.stacked_widget.insertWidget(current_row, new_widget)
                self.stacked_widget.setCurrentIndex(current_row)

        except Exception:
            error_message = traceback.format_exc()
            QMessageBox.critical(self, "執行錯誤", 
                "執行編輯後的程式碼時發生錯誤：\n\n"
                "請檢查程式碼的語法和邏輯。\n\n"
                f"詳細資訊：\n{error_message}")
        finally:
            # 清理 sys.path
            if temp_dir and temp_dir in sys.path:
                sys.path.remove(temp_dir)
# {{ end modifications }}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainAppWindow()
    window.show()
    sys.exit(app.exec())