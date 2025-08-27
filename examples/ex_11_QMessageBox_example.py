import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt


class QMessageBoxExample(QWidget):
    """
    一個展示不同類型 QMessageBox 的範例。

    這個視窗包含多個按鈕，每個按鈕都會觸發一種標準的訊息框。
    一個 QLabel 用於顯示使用者在訊息框中做出的選擇。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox 範例")
        self.setGeometry(300, 300, 400, 300)

        # 創建元件
        self.info_button = QPushButton("顯示資訊 (Information)")
        self.question_button = QPushButton("提出問題 (Question)")
        self.warning_button = QPushButton("發出警告 (Warning)")
        self.critical_button = QPushButton("報告嚴重錯誤 (Critical)")
        self.about_button = QPushButton("顯示關於對話框 (About)")

        self.result_label = QLabel("這裡將顯示對話框的返回結果")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("border: 1px solid #ccc; padding: 8px;")

        # 設定佈局
        layout = QVBoxLayout(self)
        layout.addWidget(self.info_button)
        layout.addWidget(self.question_button)
        layout.addWidget(self.warning_button)
        layout.addWidget(self.critical_button)
        layout.addWidget(self.about_button)
        layout.addStretch()
        layout.addWidget(self.result_label)

        # 連接信號與槽
        self.info_button.clicked.connect(self.show_info_message)
        self.question_button.clicked.connect(self.show_question_message)
        self.warning_button.clicked.connect(self.show_warning_message)
        self.critical_button.clicked.connect(self.show_critical_message)
        self.about_button.clicked.connect(self.show_about_message)

    def show_info_message(self):
        """顯示一個簡單的資訊訊息框。"""
        QMessageBox.information(
            self,
            "操作成功",
            "你的設定已成功儲存。",
            QMessageBox.StandardButton.Ok
        )
        self.result_label.setText("資訊框已顯示 (無返回值)")

    def show_question_message(self):
        """顯示一個問題訊息框，並根據返回值更新標籤。"""
        reply = QMessageBox.question(
            self,
            "確認操作",
            "你確定要刪除這個檔案嗎？此操作不可復原。",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No # 預設焦點在 'No' 按鈕
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.result_label.setText("使用者選擇了 'Yes'")
            print("使用者選擇了 'Yes'")
        else:
            self.result_label.setText("使用者選擇了 'No'")
            print("使用者選擇了 'No'")

    def show_warning_message(self):
        """顯示一個警告訊息框。"""
        QMessageBox.warning(
            self,
            "注意",
            "你的密碼即將在 3 天後過期。",
            QMessageBox.StandardButton.Ok
        )
        self.result_label.setText("警告框已顯示")

    def show_critical_message(self):
        """顯示一個嚴重錯誤訊息框。"""
        QMessageBox.critical(
            self,
            "錯誤",
            "無法連接到資料庫，請檢查你的網路連線。",
            QMessageBox.StandardButton.Abort
        )
        self.result_label.setText("嚴重錯誤框已顯示")

    def show_about_message(self):
        """顯示一個 '關於' 對話框。"""
        QMessageBox.about(
            self,
            "關於本應用",
            "<b>PySide6 範例瀏覽器</b><br>"
            "版本: 1.0<br>"
            "這是一個用於學習 PySide6 元件的應用程式。"
        )
        self.result_label.setText("'關於' 對話框已顯示")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMessageBoxExample()
    window.show()
    sys.exit(app.exec())
