import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QCheckBox,
    QRadioButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
)
from PySide6.QtCore import Qt


class CheckRadioExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox & QRadioButton 範例")
        self.setGeometry(300, 300, 400, 300)

        checkbox_group = QGroupBox("你的興趣 (可多選)")
        self.checkbox1 = QCheckBox("寫程式")
        self.checkbox2 = QCheckBox("閱讀")
        self.checkbox3 = QCheckBox("運動")
        self.tristate_checkbox = QCheckBox("全選/全不選")
        self.tristate_checkbox.setTristate(True)

        checkbox_layout = QVBoxLayout()
        checkbox_layout.addWidget(self.checkbox1)
        checkbox_layout.addWidget(self.checkbox2)
        checkbox_layout.addWidget(self.checkbox3)
        checkbox_layout.addWidget(self.tristate_checkbox)
        checkbox_group.setLayout(checkbox_layout)

        radio_group = QGroupBox("你的作業系統 (單選)")
        self.radio1 = QRadioButton("Windows")
        self.radio2 = QRadioButton("macOS")
        self.radio3 = QRadioButton("Linux")
        self.radio2.setChecked(True)

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.radio1)
        radio_layout.addWidget(self.radio2)
        radio_layout.addWidget(self.radio3)
        radio_group.setLayout(radio_layout)

        self.result_label = QLabel("請選擇你的選項", self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("border: 1px solid #ccc; padding: 8px; font-weight: bold;")

        main_layout = QVBoxLayout(self)
        options_layout = QHBoxLayout()
        options_layout.addWidget(checkbox_group)
        options_layout.addWidget(radio_group)
        main_layout.addLayout(options_layout)
        main_layout.addWidget(self.result_label)

        self.checkbox1.stateChanged.connect(self.update_selection)
        self.checkbox2.stateChanged.connect(self.update_selection)
        self.checkbox3.stateChanged.connect(self.update_selection)
        self.tristate_checkbox.stateChanged.connect(self.handle_tristate)
        self.radio1.toggled.connect(self.update_selection)
        self.radio2.toggled.connect(self.update_selection)
        self.radio3.toggled.connect(self.update_selection)
        
        self.update_selection()

    def update_selection(self):
        interests = []
        if self.checkbox1.isChecked(): interests.append("寫程式")
        if self.checkbox2.isChecked(): interests.append("閱讀")
        if self.checkbox3.isChecked(): interests.append("運動")

        os = "未知"
        if self.radio1.isChecked(): os = "Windows"
        if self.radio2.isChecked(): os = "macOS"
        if self.radio3.isChecked(): os = "Linux"
        
        if self.sender() is not self.tristate_checkbox:
            self.tristate_checkbox.stateChanged.disconnect(self.handle_tristate)
            if len(interests) == 3:
                self.tristate_checkbox.setCheckState(Qt.CheckState.Checked)
            elif len(interests) == 0:
                self.tristate_checkbox.setCheckState(Qt.CheckState.Unchecked)
            else:
                self.tristate_checkbox.setCheckState(Qt.CheckState.PartiallyChecked)
            self.tristate_checkbox.stateChanged.connect(self.handle_tristate)

        self.result_label.setText(f"興趣: {', '.join(interests) or '無'} | 系統: {os}")

    def handle_tristate(self, state):
        if state == Qt.CheckState.PartiallyChecked.value:
            return
        is_checked = (state == Qt.CheckState.Checked.value)
        self.checkbox1.setChecked(is_checked)
        self.checkbox2.setChecked(is_checked)
        self.checkbox3.setChecked(is_checked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckRadioExample()
    window.show()
    sys.exit(app.exec())