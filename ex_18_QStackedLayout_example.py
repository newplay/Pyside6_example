import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QStackedLayout,
    QListWidget,
    QLabel,
    QHBoxLayout,
    QFormLayout,
    QLineEdit,
)
from PySide6.QtCore import Qt


class Page(QWidget):
    """一個簡單的頁面，只顯示傳入的文字。"""
    def __init__(self, text):
        super().__init__()
        layout = QHBoxLayout(self)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px;")
        layout.addWidget(label)


class QStackedLayoutExample(QWidget):
    """
    一個展示 QStackedLayout 功能的範例。

    這個視窗左側是一個 QListWidget 作為導航，右側是一個 QStackedLayout
    用於顯示不同的頁面。點擊左側的列表項會切換右側顯示的頁面。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout (堆疊佈局) 範例")
        self.setGeometry(300, 300, 500, 300)

        # --- 創建左側的導航列表 ---
        self.nav_list = QListWidget()
        self.nav_list.setFixedWidth(120)
        self.nav_list.insertItem(0, "主頁")
        self.nav_list.insertItem(1, "個人資料")
        self.nav_list.insertItem(2, "設定")

        # --- 創建右側的堆疊佈局和頁面 ---
        self.page1 = Page("歡迎來到主頁")
        
        # 第二頁是一個表單
        self.page2 = QWidget()
        form_layout = QFormLayout(self.page2)
        form_layout.addRow("姓名:", QLineEdit())
        form_layout.addRow("地址:", QLineEdit())
        
        self.page3 = Page("這裡是設定頁面")

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.page1)
        self.stacked_layout.addWidget(self.page2)
        self.stacked_layout.addWidget(self.page3)

        # --- 創建主佈局 ---
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.nav_list)
        main_layout.addLayout(self.stacked_layout)

        # --- 連接信號與槽 ---
        self.nav_list.currentRowChanged.connect(self.stacked_layout.setCurrentIndex)
        
        # 初始化
        self.nav_list.setCurrentRow(0)

    def add_page_example(self):
        """一個展示 addWidget 和 insertWidget 的輔助說明 (未在主介面使用)"""
        # addWidget 會將頁面添加到末尾並返回其索引
        new_page = Page("這是一個新頁面")
        index = self.stacked_layout.addWidget(new_page)
        print(f"新頁面已添加在索引 {index}")
        
        # insertWidget 可以在指定位置插入頁面
        another_page = Page("這是插入的頁面")
        self.stacked_layout.insertWidget(1, another_page)
        print("一個頁面已插入到索引 1")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QStackedLayoutExample()
    window.show()
    sys.exit(app.exec())
