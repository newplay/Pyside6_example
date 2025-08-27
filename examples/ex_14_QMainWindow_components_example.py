import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QMessageBox,
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt


class MainWindowComponentsExample(QMainWindow):
    """
    一個展示 QMenuBar, QToolBar, QStatusBar 的範例。

    這個視窗是一個 QMainWindow，它包含：
    - 一個中央元件 QTextEdit。
    - 一個菜單欄，包含 "檔案" 和 "編輯" 選單。
    - 一個工具欄，包含常用動作的圖示按鈕。
    - 一個狀態欄，用於顯示提示訊息。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("主視窗元件範例")
        self.setGeometry(200, 200, 600, 400)

        # 設置中央元件
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # 創建狀態欄
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("準備就緒", 3000) # 顯示訊息 3 秒

        # 創建動作 (QAction)
        self.create_actions()

        # 創建菜單欄
        self.create_menu_bar()

        # 創建工具欄
        self.create_tool_bar()

    def create_actions(self):
        """創建所有 QAction。"""
        # 為了範例簡潔，我們不實際加載圖示，但保留 API 展示
        # new_icon = QIcon.fromTheme("document-new", QIcon("path/to/new.png"))
        # self.new_action = QAction(new_icon, "&新增", self)
        
        self.new_action = QAction("&新增 (New)", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.setStatusTip("建立一個新檔案")
        self.new_action.triggered.connect(self.new_file)

        self.save_action = QAction("&儲存 (Save)", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setStatusTip("儲存目前檔案")
        self.save_action.triggered.connect(self.save_file)

        self.exit_action = QAction("&離開 (Exit)", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setStatusTip("離開應用程式")
        self.exit_action.triggered.connect(self.close) # close 是 QWidget 的內建槽

        self.copy_action = QAction("&複製 (Copy)", self)
        self.copy_action.setShortcut("Ctrl+C")
        self.copy_action.setStatusTip("複製選取內容")
        self.copy_action.triggered.connect(self.text_edit.copy) # 連接到 QTextEdit 的內建槽

        self.paste_action = QAction("&貼上 (Paste)", self)
        self.paste_action.setShortcut("Ctrl+V")
        self.paste_action.setStatusTip("貼上剪貼簿內容")
        self.paste_action.triggered.connect(self.text_edit.paste)

    def create_menu_bar(self):
        """創建菜單欄並添加選單和動作。"""
        menu_bar = self.menuBar()

        # 檔案選單
        file_menu = menu_bar.addMenu("&檔案")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator() # 添加分隔線
        file_menu.addAction(self.exit_action)

        # 編輯選單
        edit_menu = menu_bar.addMenu("&編輯")
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)

    def create_tool_bar(self):
        """創建工具欄並添加動作。"""
        tool_bar = self.addToolBar("主要工具列")
        tool_bar.setMovable(True)
        tool_bar.addAction(self.new_action)
        tool_bar.addAction(self.save_action)
        tool_bar.addSeparator()
        tool_bar.addAction(self.copy_action)
        tool_bar.addAction(self.paste_action)

    # --- 槽函數 ---
    def new_file(self):
        self.text_edit.clear()
        self.status_bar.showMessage("已建立新檔案", 3000)

    def save_file(self):
        # 這裡僅作演示
        content = self.text_edit.toPlainText()
        self.status_bar.showMessage("檔案已儲存 (模擬)", 3000)
        print("--- 檔案內容 ---")
        print(content)
        QMessageBox.information(self, "儲存", "檔案已成功儲存 (模擬操作)。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowComponentsExample()
    window.show()
    sys.exit(app.exec())
