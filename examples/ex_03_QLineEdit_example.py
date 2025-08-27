import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QFormLayout,
    QComboBox,
)
from PySide6.QtCore import Qt


class QLineEditExample(QWidget):
    """
    一個展示 QLineEdit 功能的範例。

    這個視窗包含：
    - 一個 QLineEdit 用於使用者輸入。
    - 一個 QLabel 用於即時顯示 QLineEdit 中的內容。
    - 一個 QComboBox 用於動態改變 QLineEdit 的回顯模式 (Echo Mode)。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit 範例")
        self.setGeometry(300, 300, 400, 200)

        # 建立主要元件
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("請在此輸入文字...") # 設置提示文字

        self.display_label = QLabel("輸入的內容將顯示在這裡", self)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_label.setStyleSheet("border: 1px solid #ccc; padding: 8px;")

        self.echo_mode_combo = QComboBox(self)
        self.echo_mode_combo.addItem("正常 (Normal)", QLineEdit.EchoMode.Normal)
        self.echo_mode_combo.addItem("密碼 (Password)", QLineEdit.EchoMode.Password)
        self.echo_mode_combo.addItem("輸入時隱藏 (PasswordEchoOnEdit)", QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.echo_mode_combo.addItem("無回顯 (NoEcho)", QLineEdit.EchoMode.NoEcho)

        # 設定佈局
        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        form_layout.addRow("輸入框:", self.line_edit)
        form_layout.addRow("回顯模式:", self.echo_mode_combo)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.display_label)
        main_layout.addStretch()

        # 連接信號與槽
        self.line_edit.textChanged.connect(self.update_label)
        self.echo_mode_combo.currentIndexChanged.connect(self.change_echo_mode)

    def update_label(self, text):
        """當 QLineEdit 內容改變時，更新 QLabel。"""
        if text:
            self.display_label.setText(text)
        else:
            self.display_label.setText("輸入的內容將顯示在這裡")

    def change_echo_mode(self, index):
        """根據 QComboBox 的選擇，改變 QLineEdit 的回顯模式。"""
        # 從 ComboBox 的項目數據中獲取對應的 EchoMode
        mode = self.echo_mode_combo.itemData(index)
        self.line_edit.setEchoMode(mode)
        print(f"回顯模式已更改為: {self.echo_mode_combo.itemText(index)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QLineEditExample()
    window.show()
    sys.exit(app.exec())
