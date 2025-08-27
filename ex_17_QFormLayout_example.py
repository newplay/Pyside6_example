import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QHBoxLayout,
    QGroupBox,
    QVBoxLayout, # <-- 修正點：新增這個匯入
)
from PySide6.QtCore import Qt


class QFormLayoutExample(QWidget):
    """
    一個展示 QFormLayout 功能的範例。

    這個視窗展示了如何使用 QFormLayout 快速創建一個結構化的使用者資料表單。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout (表單佈局) 範例")
        self.setGeometry(300, 300, 400, 250)

        # 創建表單佈局實例
        form_layout = QFormLayout() # <-- 修正點：移除 self
        
        # 設定標籤和欄位的對齊方式
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)

        # --- 創建表單元件 ---
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.age_input = QLineEdit() # 實際應用中可用 QSpinBox
        
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["男", "女", "其他"])
        
        self.newsletter_check = QCheckBox("訂閱電子報")

        # --- 使用 addRow() 添加行 ---
        form_layout.addRow("姓名:", self.name_input)
        form_layout.addRow("電子郵件:", self.email_input)
        form_layout.addRow("年齡:", self.age_input)
        form_layout.addRow("性別:", self.gender_combo)
        form_layout.addRow(self.newsletter_check)
        
        submit_button = QPushButton("提交")
        cancel_button = QPushButton("取消")
        button_layout = QHBoxLayout()
        button_layout.addStretch() 
        button_layout.addWidget(submit_button)
        button_layout.addWidget(cancel_button)
        
        form_layout.addRow(button_layout)

        # 將 QFormLayout 放入一個 GroupBox 增加視覺效果
        group_box = QGroupBox("使用者註冊表單")
        group_box.setObjectName("group_box")
        group_box.setLayout(form_layout)
        
        # 設置主視窗佈局
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QFormLayoutExample()
    window.show()
    sys.exit(app.exec())