import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QFormLayout,
    QLineEdit,
    QGroupBox,
    QVBoxLayout,
)
from PySide6.QtGui import QIntValidator, QFont
from PySide6.QtCore import Qt


class QLineEditValidationExample(QWidget):
    """
    一個展示 QLineEdit 進階驗證功能的範例。

    這個視窗展示了：
    - setMaxLength: 限制輸入長度。
    - QIntValidator: 只允許輸入特定範圍的整數。
    - setInputMask: 使用遮罩來格式化輸入。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit 進階驗證範例")
        self.setGeometry(300, 300, 400, 200)

        # 創建主佈局和容器
        main_layout = QVBoxLayout(self)
        group_box = QGroupBox("輸入驗證")
        form_layout = QFormLayout(group_box)
        
        # --- 1. 長度限制 (maxLength) ---
        length_limit_edit = QLineEdit()
        length_limit_edit.setMaxLength(10)
        length_limit_edit.setPlaceholderText("最多輸入 10 個字元")
        
        # --- 2. 整數驗證 (QIntValidator) ---
        int_validator_edit = QLineEdit()
        # 創建一個驗證器，只允許輸入 0 到 999 之間的整數
        int_validator = QIntValidator(0, 999, self)
        int_validator_edit.setValidator(int_validator)
        int_validator_edit.setPlaceholderText("只能輸入 0-999 的數字")

        # --- 3. 輸入遮罩 (InputMask) ---
        mask_edit = QLineEdit()
        # H: 十六進位字元; 9: 數字; N: 字母或數字; A: 字母
        # 遮罩中的分號用於分隔遮罩和佔位符字元
        mask_edit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        
        # 添加到表單佈局
        form_layout.addRow("長度限制 (10):", length_limit_edit)
        form_layout.addRow("整數驗證 (0-999):", int_validator_edit)
        form_layout.addRow("MAC 位址遮罩:", mask_edit)
        
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QLineEditValidationExample()
    window.show()
    sys.exit(app.exec())
