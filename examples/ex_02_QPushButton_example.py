import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
)
from PySide6.QtCore import Qt


class QPushButtonExample(QWidget):
    """
    一個展示 QPushButton 多種功能的範例。

    這個視窗包含：
    - 一個標準 QPushButton，點擊時會更新一個計數器 QLabel。
    - 一個 QCheckBox 用於控制按鈕的啟用/禁用狀態。
    - 一個 QCheckBox 用於將按鈕設置為可勾選 (checkable) 狀態。
    - 一個 QLabel 用於顯示可勾選按鈕的當前狀態。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPushButton 範例")
        self.setGeometry(300, 300, 350, 250)

        # 建立主要元件
        self.main_button = QPushButton("點擊我!", self)
        self.main_button.setStyleSheet("padding: 10px; font-size: 16px;")

        self.count_label = QLabel("點擊次數: 0", self)
        self.count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.checkable_status_label = QLabel("按鈕未被勾選", self)
        self.checkable_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.enable_checkbox = QCheckBox("啟用/禁用按鈕", self)
        self.enable_checkbox.setChecked(True) # 預設啟用

        self.checkable_checkbox = QCheckBox("設置為可勾選 (Checkable)", self)

        # 設定佈局
        main_layout = QVBoxLayout(self)
        
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.enable_checkbox)
        control_layout.addWidget(self.checkable_checkbox)

        main_layout.addWidget(self.count_label)
        main_layout.addWidget(self.main_button)
        main_layout.addWidget(self.checkable_status_label)
        main_layout.addLayout(control_layout)

        # 連接信號與槽
        self.main_button.clicked.connect(self.on_button_clicked)
        self.main_button.toggled.connect(self.on_button_toggled)
        self.enable_checkbox.stateChanged.connect(self.toggle_button_enabled)
        self.checkable_checkbox.stateChanged.connect(self.toggle_button_checkable)

        # 初始化計數器
        self.click_count = 0

    def on_button_clicked(self):
        """處理按鈕點擊事件。"""
        # 只有在非 checkable 模式下，或 checkable 模式下被點擊選中時才計數
        if not self.main_button.isCheckable() or self.main_button.isChecked():
            self.click_count += 1
            self.count_label.setText(f"點擊次數: {self.click_count}")

    def on_button_toggled(self, checked):
        """處理按鈕勾選狀態變化的事件 (僅在 checkable 時觸發)。"""
        if checked:
            self.checkable_status_label.setText("按鈕狀態: 已勾選 (Checked)")
        else:
            self.checkable_status_label.setText("按鈕狀態: 未被勾選")

    def toggle_button_enabled(self, state):
        """根據 checkbox 狀態啟用或禁用按鈕。"""
        is_enabled = (state == Qt.Checked.value)
        self.main_button.setEnabled(is_enabled)
        print(f"按鈕啟用狀態: {is_enabled}")

    def toggle_button_checkable(self, state):
        """根據 checkbox 狀態設置按鈕是否可勾選。"""
        is_checkable = (state == Qt.Checked.value)
        self.main_button.setCheckable(is_checkable)
        print(f"按鈕可勾選狀態: {is_checkable}")
        # 重置狀態標籤
        self.on_button_toggled(self.main_button.isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QPushButtonExample()
    window.show()
    sys.exit(app.exec())
