import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTabWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFormLayout,
    QLineEdit,
)
from PySide6.QtCore import Qt


class GeneralTab(QWidget):
    """一個通用的標籤頁面，只包含一個標籤。"""
    def __init__(self, text, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

class FormTab(QWidget):
    """一個包含表單的標籤頁面。"""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QFormLayout(self)
        layout.addRow("姓名:", QLineEdit())
        layout.addRow("電子郵件:", QLineEdit())
        layout.addRow("地址:", QLineEdit())
        self.setLayout(layout)


class QTabWidgetExample(QWidget):
    """
    一個展示 QTabWidget 功能的範例。

    這個視窗包含：
    - 一個 QTabWidget，內含幾個不同的標籤頁。
    - 一個 QLabel 用於顯示當前切換事件的資訊。
    - 一組 QPushButton 用於動態新增和移除標籤頁。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget 範例")
        self.setGeometry(300, 300, 500, 300)

        # 創建元件
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True) # 讓標籤頁可以被關閉
        self.tab_widget.setMovable(True)      # 讓標籤頁可以被拖動排序

        self.info_label = QLabel("歡迎使用 QTabWidget")
        self.add_tab_button = QPushButton("新增標籤頁")
        self.remove_tab_button = QPushButton("移除當前頁")

        # 設定佈局
        main_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()
        
        button_layout.addWidget(self.add_tab_button)
        button_layout.addWidget(self.remove_tab_button)
        button_layout.addStretch()

        main_layout.addWidget(self.tab_widget)
        main_layout.addWidget(self.info_label)
        main_layout.addLayout(button_layout)

        # 填充初始標籤頁
        self.setup_tabs()

        # 連接信號與槽
        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        self.tab_widget.tabCloseRequested.connect(self.on_tab_close)
        self.add_tab_button.clicked.connect(self.add_tab)
        self.remove_tab_button.clicked.connect(self.remove_current_tab)
        
        self.new_tab_count = 0

    def setup_tabs(self):
        """初始化標籤頁。"""
        tab1 = GeneralTab("這是第一個標籤頁的內容。")
        tab2 = FormTab()
        tab3 = GeneralTab("這是第三個標籤頁，展示了不同的內容。")

        self.tab_widget.addTab(tab1, "總覽")
        self.tab_widget.addTab(tab2, "使用者資料")
        self.tab_widget.addTab(tab3, "說明")
        
        # 為某個標籤頁設置提示文字
        self.tab_widget.setTabToolTip(0, "這是關於總覽的提示")

    def on_tab_changed(self, index):
        """當標籤頁切換時觸發。"""
        tab_text = self.tab_widget.tabText(index)
        self.info_label.setText(f"已切換到索引為 {index} 的標籤頁: '{tab_text}'")
        print(f"Tab changed to index {index}")

    def on_tab_close(self, index):
        """當使用者點擊標籤頁上的關閉按鈕時觸發。"""
        tab_text = self.tab_widget.tabText(index)
        self.tab_widget.removeTab(index)
        print(f"已關閉標籤頁: '{tab_text}' (原索引 {index})")

    def add_tab(self):
        """動態新增一個標籤頁。"""
        self.new_tab_count += 1
        new_tab_title = f"新標籤頁 {self.new_tab_count}"
        new_tab_content = GeneralTab(f"這是動態新增的第 {self.new_tab_count} 個標籤頁。")
        
        index = self.tab_widget.addTab(new_tab_content, new_tab_title)
        self.tab_widget.setCurrentIndex(index) # 切換到新創建的頁面
        print(f"已新增標籤頁 '{new_tab_title}' 在索引 {index}")

    def remove_current_tab(self):
        """移除當前可見的標籤頁。"""
        current_index = self.tab_widget.currentIndex()
        if current_index != -1:
            self.on_tab_close(current_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QTabWidgetExample()
    window.show()
    sys.exit(app.exec())
