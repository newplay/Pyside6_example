import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt


class QListWidgetExample(QWidget):
    """
    一個展示 QListWidget 功能的範例。

    這個視窗包含：
    - 一個 QListWidget 用於顯示項目列表。
    - 一個 QLineEdit 和一個 QPushButton 用於向列表中新增項目。
    - 一個 QPushButton 用於刪除當前選中的項目。
    - 一個 QLabel 用於顯示當前選中的項目資訊。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget 範例")
        self.setGeometry(300, 300, 400, 350)

        # 創建元件
        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True) # 啟用交替行顏色

        self.item_input = QLineEdit()
        self.item_input.setPlaceholderText("輸入新項目名稱...")

        self.add_button = QPushButton("新增項目")
        self.delete_button = QPushButton("刪除選中項")
        
        self.info_label = QLabel("請從列表中選擇一個項目")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 預填充一些項目
        self.populate_list()

        # 設定佈局
        main_layout = QVBoxLayout(self)
        input_layout = QHBoxLayout()

        input_layout.addWidget(self.item_input)
        input_layout.addWidget(self.add_button)

        main_layout.addWidget(self.list_widget)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.delete_button)
        main_layout.addWidget(self.info_label)

        # 連接信號與槽
        self.add_button.clicked.connect(self.add_item)
        self.item_input.returnPressed.connect(self.add_item) # 按 Enter 也能新增
        self.delete_button.clicked.connect(self.delete_item)
        self.list_widget.currentItemChanged.connect(self.on_item_changed)

    def populate_list(self):
        """填充初始列表項目。"""
        tasks = ["學習 PySide6", "撰寫文件", "設計 UI", "測試應用程式", "發布版本"]
        for task in tasks:
            item = QListWidgetItem(task)
            self.list_widget.addItem(item)

    def add_item(self):
        """從輸入框獲取文字並新增一個項目到列表中。"""
        text = self.item_input.text().strip()
        if text:
            self.list_widget.addItem(text)
            self.item_input.clear()
            print(f"已新增項目: '{text}'")
        else:
            print("輸入為空，不新增。")

    def delete_item(self):
        """刪除當前選中的項目。"""
        current_item = self.list_widget.currentItem()
        if current_item:
            # takeItem 會從列表中移除項目並返回它，需要手動刪除
            row = self.list_widget.row(current_item)
            item = self.list_widget.takeItem(row)
            del item
            print(f"已刪除項目，行號: {row}")
            if self.list_widget.count() == 0:
                self.info_label.setText("列表已空")
        else:
            print("沒有選中任何項目。")

    def on_item_changed(self, current, previous):
        """當選中的項目改變時，更新標籤。"""
        if current:
            self.info_label.setText(f"當前選中: '{current.text()}' (在第 {self.list_widget.row(current)} 行)")
        else:
            # 如果列表被清空，current 會是 None
            self.info_label.setText("沒有項目被選中")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QListWidgetExample()
    window.show()
    sys.exit(app.exec())
