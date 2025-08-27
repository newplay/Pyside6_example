import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QColorDialog,
    QFontDialog,
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont


class ColorFontDialogExample(QWidget):
    """
    一個展示 QColorDialog 和 QFontDialog 的範例。

    這個視窗包含：
    - 一個 QLabel 作為樣式展示的目標。
    - 一個按鈕用於彈出 QColorDialog 來改變 QLabel 的背景色。
    - 一個按鈕用於彈出 QFontDialog 來改變 QLabel 的字體。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog & QFontDialog 範例")
        self.setGeometry(300, 300, 450, 250)

        # 創建元件
        self.display_label = QLabel("點擊下方按鈕來改變我的樣式")
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_label.setAutoFillBackground(True)
        
        # 初始化樣式
        self.current_font = QFont("Arial", 16)
        self.display_label.setFont(self.current_font)
        
        self.change_color_button = QPushButton("選擇背景顏色...")
        self.change_font_button = QPushButton("選擇字體...")

        # 設定佈局
        layout = QVBoxLayout(self)
        layout.addWidget(self.display_label, 1)
        layout.addWidget(self.change_color_button)
        layout.addWidget(self.change_font_button)

        # 連接信號與槽
        self.change_color_button.clicked.connect(self.open_color_dialog)
        self.change_font_button.clicked.connect(self.open_font_dialog)

    def open_color_dialog(self):
        """開啟顏色選擇對話框。"""
        initial_color = self.display_label.palette().color(self.display_label.backgroundRole())
        color = QColorDialog.getColor(initial_color, self, "選擇一個顏色")

        if color.isValid():
            self.display_label.setStyleSheet(f"background-color: {color.name()};")
            print(f"顏色已選擇: {color.name()}")
        else:
            print("顏色選擇已取消。")

    def open_font_dialog(self):
        """開啟字體選擇對話框。"""
        # --- 核心修正點：使用 QFontDialog 的實例，而不是靜態方法 ---
        font_dialog = QFontDialog(self)
        font_dialog.setCurrentFont(self.current_font)
        
        # exec() 會以模態方式執行對話框
        if font_dialog.exec():
            # 如果使用者點擊 OK，則獲取選擇的字體
            self.current_font = font_dialog.selectedFont()
            self.display_label.setFont(self.current_font)
            print(f"字體已選擇: {self.current_font.family()}, 大小: {self.current_font.pointSize()}")
        else:
            print("字體選擇已取消。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorFontDialogExample()
    window.show()
    sys.exit(app.exec())