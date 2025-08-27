import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QCheckBox,
)
from PySide6.QtCore import Qt


class QLabelExample(QWidget):
    """
    一個展示 QLabel 功能的範例。

    這個視窗包含一個 QLabel、一個 QPushButton 和一個 QCheckBox。
    - QPushButton 用於改變 QLabel 顯示的文字。
    - QCheckBox 用於控制 QLabel 是否啟用自動換行 (Word Wrap)。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel 範例")
        self.setGeometry(300, 300, 300, 200)

        # 建立主要元件
        self.label = QLabel(
            "這是一個 QLabel。\n點擊下面的按鈕來更新我。", self
        )
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("border: 1px solid black; padding: 5px;")

        self.update_button = QPushButton("更新文字", self)
        self.word_wrap_checkbox = QCheckBox("啟用自動換行 (Word Wrap)", self)

        # 設定佈局
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.word_wrap_checkbox)
        layout.addWidget(self.update_button)

        # 連接信號與槽
        self.update_button.clicked.connect(self.update_label_text)
        self.word_wrap_checkbox.stateChanged.connect(self.toggle_word_wrap)

        # 初始化文字更新計數器
        self.click_count = 0

    def update_label_text(self):
        """點擊按鈕時，更新 QLabel 的文字。"""
        self.click_count += 1
        self.label.setText(f"文字已被更新 {self.click_count} 次！\n"
                           "這是一段非常非常非常非常非常非常長的文字，"
                           "用來測試自動換行功能是否生效。")

    def toggle_word_wrap(self, state):
        """根據 QCheckBox 的狀態，啟用或禁用 QLabel 的自動換行。"""
        # Qt.Checked 的值是 2，Qt.Unchecked 的值是 0
        if state == Qt.Checked.value:
            self.label.setWordWrap(True)
            print("自動換行已啟用")
        else:
            self.label.setWordWrap(False)
            print("自動換行已禁用")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QLabelExample()
    window.show()
    sys.exit(app.exec())
