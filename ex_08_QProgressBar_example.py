import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
)
from PySide6.QtCore import QTimer, Qt


class QProgressBarExample(QWidget):
    """
    一個展示 QProgressBar 功能的範例。

    這個視窗包含：
    - 一個 QProgressBar。
    - 一個 QPushButton 用於開始一個模擬的耗時任務。
    - 一個 QPushButton 用於重置。
    - 一個 QPushButton 用於切換到不確定模式。
    - 使用 QTimer 來模擬進度的推進。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar 範例")
        self.setGeometry(300, 300, 400, 200)

        # 創建元件
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        self.start_button = QPushButton("開始任務", self)
        self.reset_button = QPushButton("重置", self)
        self.indeterminate_button = QPushButton("切換到不確定模式", self)

        # 設定佈局
        layout = QVBoxLayout(self)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.indeterminate_button)

        # 計時器用於模擬進度
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.advance_progress)
        self.step = 0

        # 連接信號與槽
        self.start_button.clicked.connect(self.start_task)
        self.reset_button.clicked.connect(self.reset_task)
        self.indeterminate_button.clicked.connect(self.toggle_indeterminate)

    def start_task(self):
        """開始模擬任務。"""
        if self.timer.isActive():
            return
            
        # 確保是確定模式
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.step = 0
        
        self.timer.start(100) # 每 100 毫秒觸發一次
        self.start_button.setEnabled(False)
        self.indeterminate_button.setEnabled(False)
        print("任務開始...")

    def advance_progress(self):
        """推進進度。"""
        self.step += 1
        self.progress_bar.setValue(self.step)

        if self.step >= 100:
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.indeterminate_button.setEnabled(True)
            print("任務完成！")

    def reset_task(self):
        """重置進度條和任務狀態。"""
        self.timer.stop()
        # 確保切換回確定模式再重置
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.step = 0
        self.start_button.setEnabled(True)
        self.indeterminate_button.setEnabled(True)
        self.progress_bar.setTextVisible(True)
        print("任務已重置。")

    def toggle_indeterminate(self):
        """切換進度條的確定/不確定模式。"""
        current_min = self.progress_bar.minimum()
        current_max = self.progress_bar.maximum()

        if current_min == 0 and current_max == 0:
            # 當前是不確定模式，切換回確定模式
            self.progress_bar.setRange(0, 100)
            self.progress_bar.setTextVisible(True)
            self.indeterminate_button.setText("切換到不確定模式")
            print("切換到確定模式")
        else:
            # 當前是確定模式，切換到不確定模式
            self.progress_bar.setRange(0, 0)
            self.indeterminate_button.setText("切換到確定模式")
            print("切換到不確定模式")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QProgressBarExample()
    window.show()
    sys.exit(app.exec())
