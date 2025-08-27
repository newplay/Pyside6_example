import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QComboBox,
    QVBoxLayout,
    QFormLayout,
    QCheckBox,
    QPushButton,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon # 假設我們有圖示資源

class QComboBoxExample(QWidget):
    """
    一個展示 QComboBox 功能的範例。

    這個視窗包含：
    - 一個 QComboBox，包含多個程式語言選項，部分選項帶有圖示。
    - 一個 QLabel 用於顯示使用者的選擇。
    - 一個 QCheckBox 用於切換 ComboBox 的可編輯狀態。
    - 一個 QPushButton 用於在執行時動態新增項目。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox 範例")
        self.setGeometry(300, 300, 400, 250)

        # 建立主要元件
        self.combo_box = QComboBox(self)
        self.result_label = QLabel("你選擇的語言是: Python", self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("border: 1px solid #ccc; padding: 8px;")

        self.editable_checkbox = QCheckBox("允許使用者編輯/新增項目", self)
        self.add_item_button = QPushButton("動態新增 'Go'", self)

        # 設定佈局
        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        form_layout.addRow("選擇程式語言:", self.combo_box)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.editable_checkbox)
        main_layout.addWidget(self.add_item_button)
        main_layout.addStretch()

        # 初始化 ComboBox
        self.populate_combo_box()

        # 連接信號與槽
        self.combo_box.currentIndexChanged.connect(self.on_selection_change)
        self.combo_box.currentTextChanged.connect(self.on_text_change)
        self.editable_checkbox.stateChanged.connect(self.toggle_editable)
        self.add_item_button.clicked.connect(self.add_item)

    def populate_combo_box(self):
        """填充 ComboBox 的初始項目。"""
        # addItem 可以接受文字、圖示和使用者數據 (userData)
        # 為了範例簡潔，這裡不實際加載圖示檔案，但保留 API 展示
        # self.combo_box.addItem(QIcon("path/to/python.png"), "Python", userData="py")
        self.combo_box.addItem("Python", userData="py")
        self.combo_box.addItem("JavaScript", userData="js")
        self.combo_box.addItem("C++", userData="cpp")
        self.combo_box.addItem("Java", userData="java")
        
        # 插入一個分隔線
        self.combo_box.insertSeparator(4)
        self.combo_box.addItem("Rust", userData="rs")


    def on_selection_change(self, index):
        """當下拉清單中的選擇項索引改變時觸發。"""
        if index == -1: # 當 ComboBox 被清空時，索引為 -1
            return
            
        selected_text = self.combo_box.currentText()
        selected_data = self.combo_box.currentData()
        print(f"索引改變: 索引={index}, 文字='{selected_text}', 數據='{selected_data}'")
        # self.result_label.setText(f"你選擇的語言是: {selected_text}")

    def on_text_change(self, text):
        """當 ComboBox 的當前文字改變時觸發 (包括選擇和編輯)。"""
        print(f"文字改變: '{text}'")
        self.result_label.setText(f"當前顯示的是: {text}")

    def toggle_editable(self, state):
        """切換 ComboBox 的可編輯狀態。"""
        is_editable = (state == Qt.Checked.value)
        self.combo_box.setEditable(is_editable)
        print(f"可編輯狀態: {is_editable}")

    def add_item(self):
        """動態地向 ComboBox 新增一個項目。"""
        # 檢查項目是否已存在
        if self.combo_box.findText("Go") == -1:
            self.combo_box.addItem("Go", userData="go")
            print("已新增項目 'Go'")
            self.add_item_button.setEnabled(False)
            self.add_item_button.setText("'Go' 已新增")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QComboBoxExample()
    window.show()
    sys.exit(app.exec())
