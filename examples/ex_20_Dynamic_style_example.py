import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QColorDialog,
)
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtCore import Qt


class DynamicStyleExample(QWidget):
    """
    一個展示如何動態改變元件樣式的範例。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("動態樣式設定範例")
        self.setGeometry(300, 300, 400, 200)

        # 創建元件
        self.display_label = QLabel("觀察我的顏色變化")
        self.display_label.setAlignment(Qt.AlignCenter)
        self.display_label.setFont(QFont("Arial", 20))
        self.display_label.setAutoFillBackground(True) # 必須設定此項才能讓背景色生效

        self.text_color_button = QPushButton("改變字體顏色")
        self.bg_color_button = QPushButton("改變背景顏色")

        # 設定佈局
        main_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.text_color_button)
        button_layout.addWidget(self.bg_color_button)
        
        main_layout.addWidget(self.display_label, 1)
        main_layout.addLayout(button_layout)

        # 連接信號
        self.text_color_button.clicked.connect(self.change_text_color)
        self.bg_color_button.clicked.connect(self.change_bg_color)

    def change_text_color(self):
        """使用 QColorDialog 改變字體顏色。"""
        current_color = self.display_label.palette().color(QPalette.WindowText)
        color = QColorDialog.getColor(current_color, self, "選擇字體顏色")

        if color.isValid():
            # 使用 QPalette 來設定顏色是更底層、更推薦的方式
            palette = self.display_label.palette()
            palette.setColor(QPalette.WindowText, color)
            self.display_label.setPalette(palette)

    def change_bg_color(self):
        """使用 QColorDialog 改變背景顏色。"""
        current_color = self.display_label.palette().color(QPalette.Window)
        color = QColorDialog.getColor(current_color, self, "選擇背景顏色")

        if color.isValid():
            palette = self.display_label.palette()
            palette.setColor(QPalette.Window, color)
            self.display_label.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DynamicStyleExample()
    window.show()
    sys.exit(app.exec())
