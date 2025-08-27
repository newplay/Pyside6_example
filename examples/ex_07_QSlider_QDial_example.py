import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QSlider,
    QDial,
    QProgressBar,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
)
from PySide6.QtCore import Qt


class SliderDialExample(QWidget):
    """
    一個展示 QSlider 和 QDial 功能的範例。

    這個視窗包含：
    - 一個水平 QSlider 和一個 QDial，它們的值是同步的。
    - 一個 QProgressBar，其進度由 Slider 和 Dial 控制。
    - 一個 QLabel，用於精確顯示當前的數值。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider & QDial 範例")
        self.setGeometry(300, 300, 500, 350)

        # --- 創建元件 ---
        # 數值範圍設定
        min_val, max_val = 0, 100

        # 水平滑桿
        slider_group = QGroupBox("QSlider (水平滑桿)")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        slider_layout = QVBoxLayout()
        slider_layout.addWidget(self.slider)
        slider_group.setLayout(slider_layout)

        # 旋鈕
        dial_group = QGroupBox("QDial (旋鈕)")
        self.dial = QDial()
        self.dial.setNotchesVisible(True) # 顯示刻度
        dial_layout = QHBoxLayout()
        dial_layout.addStretch()
        dial_layout.addWidget(self.dial)
        dial_layout.addStretch()
        dial_group.setLayout(dial_layout)

        # 進度條和數值標籤
        feedback_group = QGroupBox("回饋元件")
        self.progress_bar = QProgressBar()
        self.value_label = QLabel(f"當前數值: {min_val}")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        feedback_layout = QVBoxLayout()
        feedback_layout.addWidget(self.value_label)
        feedback_layout.addWidget(self.progress_bar)
        feedback_group.setLayout(feedback_layout)

        # --- 設定元件屬性 ---
        for widget in [self.slider, self.dial, self.progress_bar]:
            widget.setRange(min_val, max_val)

        # --- 主佈局 ---
        main_layout = QVBoxLayout(self)
        controls_layout = QHBoxLayout()
        controls_layout.addWidget(slider_group, 1)
        controls_layout.addWidget(dial_group, 1)
        main_layout.addLayout(controls_layout)
        main_layout.addWidget(feedback_group)

        # --- 連接信號與槽 ---
        self.slider.valueChanged.connect(self.sync_values)
        self.dial.valueChanged.connect(self.sync_values)

        # 初始化數值
        self.slider.setValue(25)

    def sync_values(self, value):
        """
        當一個元件的值改變時，同步更新所有其他相關元件。
        使用 self.sender() 來識別是哪個元件觸發了信號。
        """
        sender = self.sender()
        
        # 為了避免信號循環觸發 (A->B, B->A)，我們可以檢查值是否真的改變了
        # 但更簡單的方法是，在設置值之前先斷開連接
        
        # 斷開所有連接
        self.slider.valueChanged.disconnect(self.sync_values)
        self.dial.valueChanged.disconnect(self.sync_values)

        # 設置新值
        self.slider.setValue(value)
        self.dial.setValue(value)
        self.progress_bar.setValue(value)
        self.value_label.setText(f"當前數值: {value}")
        
        if sender is self.slider:
            print(f"Slider 觸發, value={value}")
        else:
            print(f"Dial 觸發, value={value}")

        # 重新連接
        self.slider.valueChanged.connect(self.sync_values)
        self.dial.valueChanged.connect(self.sync_values)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderDialExample()
    window.show()
    sys.exit(app.exec())
