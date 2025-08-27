import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
)
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtCore import Qt


class QTextEditExample(QWidget):
    """
    一個展示 QTextEdit 功能的範例。

    這個視窗包含：
    - 一個 QTextEdit 用於使用者輸入多行和富文本。
    - 兩個 QPushButton，一個用於獲取純文字，另一個用於獲取 HTML 內容。
    - 一個 QLabel 用於顯示獲取到的內容。
    - 一個 QCheckBox 用於切換 QTextEdit 的唯讀狀態。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit 範例")
        self.setGeometry(300, 300, 500, 400)

        # 建立主要元件
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("請在此輸入文字，可使用 Ctrl+B 加粗，Ctrl+I 設為斜體...")
        
        # --- 核心修正點：設定一個支援 Unicode 的等寬字體 ---
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setPointSize(11)
        self.text_edit.setFont(font)

        # 預先填入一些富文本內容
        self.text_edit.setHtml(
            "<h1>歡迎使用 QTextEdit</h1>"
            "<p>這是一個功能強大的<b>富文本</b>編輯器。</p>"
            "<ul><li>項目一</li><li>項目二</li></ul>"
        )

        self.display_label = QLabel("點擊按鈕以顯示 QTextEdit 的內容", self)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_label.setStyleSheet("border: 1px solid #ccc; padding: 8px; background-color: #f0f0f0;")
        self.display_label.setWordWrap(True)

        self.get_plain_text_button = QPushButton("獲取純文字 (toPlainText)", self)
        self.get_html_button = QPushButton("獲取 HTML (toHtml)", self)
        self.readonly_checkbox = QCheckBox("設為唯讀 (ReadOnly)", self)

        # 設定佈局
        main_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()

        button_layout.addWidget(self.get_plain_text_button)
        button_layout.addWidget(self.get_html_button)

        main_layout.addWidget(self.text_edit, 1)
        main_layout.addWidget(self.readonly_checkbox)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.display_label, 1)

        # 連接信號與槽
        self.get_plain_text_button.clicked.connect(self.get_plain_text)
        self.get_html_button.clicked.connect(self.get_html_content)
        self.readonly_checkbox.stateChanged.connect(self.toggle_readonly)
        self.text_edit.textChanged.connect(lambda: print("內容已變更..."))

    def get_plain_text(self):
        """獲取 QTextEdit 中的純文字內容並顯示。"""
        plain_text = self.text_edit.toPlainText()
        print("--- 純文字內容 ---\
", plain_text)
        self.display_label.setText(plain_text)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

    def get_html_content(self):
        """獲取 QTextEdit 中的 HTML 內容並顯示。"""
        html_content = self.text_edit.toHtml()
        print("--- HTML 內容 ---\
", html_content)
        self.display_label.setText(html_content)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

    def toggle_readonly(self, state):
        """根據 checkbox 狀態切換 QTextEdit 的唯讀模式。"""
        is_readonly = (state == Qt.Checked.value)
        self.text_edit.setReadOnly(is_readonly)
        print(f"唯讀狀態: {is_readonly}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QTextEditExample()
    window.show()
    sys.exit(app.exec())