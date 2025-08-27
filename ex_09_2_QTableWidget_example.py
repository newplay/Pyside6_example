import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QHeaderView,
)
from PySide6.QtCore import Qt


class QTableWidgetExample(QWidget):
    """
    一個展示 QTableWidget 功能的範例。

    這個視窗包含：
    - 一個 QTableWidget 用於顯示結構化數據。
    - 一個 QPushButton 用於動態新增一行數據。
    - 一個 QLabel 用於顯示當前選中單元格的資訊。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget 範例")
        self.setGeometry(200, 200, 550, 400)

        # 創建元件
        self.table_widget = QTableWidget()
        self.add_row_button = QPushButton("新增一行")
        self.info_label = QLabel("點擊一個單元格以查看其資訊")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 設定表格
        self.setup_table()

        # 設定佈局
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.table_widget)
        main_layout.addWidget(self.add_row_button)
        main_layout.addWidget(self.info_label)

        # 連接信號與槽
        self.add_row_button.clicked.connect(self.add_row)
        self.table_widget.cellClicked.connect(self.on_cell_clicked)
        self.table_widget.cellChanged.connect(self.on_cell_changed)

    def setup_table(self):
        """初始化表格的結構和內容。"""
        # 1. 設定行數和列數
        self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(3)

        # 2. 設定水平和垂直標頭
        self.table_widget.setHorizontalHeaderLabels(["姓名", "語言", "貢獻值"])
        self.table_widget.setVerticalHeaderLabels(["User1", "User2", "User3", "User4"])

        # 3. 填充初始數據
        data = [
            ("Alice", "Python", "150"),
            ("Bob", "C++", "220"),
            ("Charlie", "JavaScript", "80"),
            ("David", "Rust", "300"),
        ]

        for row, (name, lang, contrib) in enumerate(data):
            name_item = QTableWidgetItem(name)
            lang_item = QTableWidgetItem(lang)
            contrib_item = QTableWidgetItem(contrib)
            
            # 讓貢獻值欄位不可編輯且靠右對齊
            contrib_item.setFlags(contrib_item.flags() & ~Qt.ItemIsEditable)
            contrib_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

            self.table_widget.setItem(row, 0, name_item)
            self.table_widget.setItem(row, 1, lang_item)
            self.table_widget.setItem(row, 2, contrib_item)

        # 4. 調整表格外觀
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setSortingEnabled(True)

    def add_row(self):
        """在表格末尾新增一個空行。"""
        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)
        
        # 可以選擇性地填充預設值
        self.table_widget.setItem(row_count, 0, QTableWidgetItem("New User"))
        self.table_widget.setItem(row_count, 1, QTableWidgetItem("Unknown"))
        self.table_widget.setItem(row_count, 2, QTableWidgetItem("0"))
        
        print(f"已在第 {row_count} 行新增。")

    def on_cell_clicked(self, row, column):
        """當單元格被點擊時觸發。"""
        item = self.table_widget.item(row, column)
        text = item.text() if item else "N/A"
        self.info_label.setText(f"你點擊了第 {row} 行, 第 {column} 列。內容: '{text}'")

    def on_cell_changed(self, row, column):
        """當單元格的內容被使用者編輯後觸發。"""
        item = self.table_widget.item(row, column)
        new_text = item.text() if item else ""
        print(f"單元格 ({row}, {column}) 的內容已變更為: '{new_text}'")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QTableWidgetExample()
    window.show()
    sys.exit(app.exec())
