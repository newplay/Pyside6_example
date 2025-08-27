import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QTextEdit,
)


class QGridLayoutExample(QWidget):
    """
    一個展示 QGridLayout 功能的範例，模擬一個計算機鍵盤佈局。

    這個視窗展示了如何：
    - 將按鈕放置在網格的不同單元格中。
    - 讓一個元件（顯示屏）跨越多列。
    - 讓一個按鈕跨越多行。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout (網格佈局) 範例")
        self.setGeometry(300, 300, 300, 400)

        # 創建網格佈局實例
        grid_layout = QGridLayout(self)

        # --- 創建元件 ---
        # 顯示屏，跨越 4 列
        display = QTextEdit()
        display.setReadOnly(True)
        display.setFixedHeight(80)
        
        # 將顯示屏添加到網格的第 0 行、第 0 列，
        # 並讓它佔用 1 行和 4 列
        grid_layout.addWidget(display, 0, 0, 1, 4)

        # 按鈕名稱列表
        button_names = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]

        # 遍歷按鈕名稱，創建按鈕並添加到網格中
        positions = [(i, j) for i in range(1, 5) for j in range(4)]

        for position, name in zip(positions, button_names):
            row, col = position
            button = QPushButton(name)
            grid_layout.addWidget(button, row, col)
            
            # 將 '=' 按鈕跨越 2 行
            if name == '=':
                # addWidget(widget, fromRow, fromColumn, rowSpan, columnSpan)
                grid_layout.addWidget(button, row, col, 2, 1)
            
            # 將 '+' 按鈕移動到 '=' 按鈕的右邊
            if name == '+':
                grid_layout.addWidget(button, row, col + 1)

        # 調整行和列的拉伸因子，讓按鈕填充空間
        for i in range(1, 5):
            grid_layout.setRowStretch(i, 1)
        for j in range(4):
            grid_layout.setColumnStretch(j, 1)
            
        # 讓最後一列（給 '+' 用的）也拉伸
        grid_layout.setColumnStretch(4, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QGridLayoutExample()
    window.show()
    sys.exit(app.exec())
