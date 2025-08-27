import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QTextEdit,
)
from PySide6.QtCore import Qt, QDir


class QFileDialogExample(QWidget):
    """
    一個展示 QFileDialog 不同模式的範例。

    這個視窗包含：
    - 多個按鈕，分別用於觸發「開啟單一檔案」、「開啟多個檔案」、
      「選擇目錄」和「儲存檔案」的對話框。
    - 一個 QTextEdit 用於顯示選擇的結果。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog 範例")
        self.setGeometry(300, 300, 500, 400)

        # 創建元件
        self.open_file_button = QPushButton("開啟單一檔案...")
        self.open_files_button = QPushButton("開啟多個檔案...")
        self.select_dir_button = QPushButton("選擇目錄...")
        self.save_file_button = QPushButton("儲存檔案...")

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText("這裡將顯示選擇的檔案或目錄路徑")

        # 設定佈局
        layout = QVBoxLayout(self)
        layout.addWidget(self.open_file_button)
        layout.addWidget(self.open_files_button)
        layout.addWidget(self.select_dir_button)
        layout.addWidget(self.save_file_button)
        layout.addWidget(self.result_display)

        # 連接信號與槽
        self.open_file_button.clicked.connect(self.open_file)
        self.open_files_button.clicked.connect(self.open_files)
        self.select_dir_button.clicked.connect(self.select_directory)
        self.save_file_button.clicked.connect(self.save_file)

    def open_file(self):
        """開啟一個「選擇單一檔案」的對話框。"""
        # 檔案過濾器格式: "描述 (*.ext1 *.ext2);;另一個描述 (*.ext3)"
        file_filter = "圖片檔案 (*.png *.jpg *.bmp);;文字檔案 (*.txt);;所有檔案 (*)"
        # getOpenFileName 返回一個元組 (選擇的檔案路徑, 選擇的過濾器)
        file_path, selected_filter = QFileDialog.getOpenFileName(
            self,
            "選擇一個檔案",
            QDir.homePath(), # 預設開啟的目錄
            file_filter
        )

        if file_path:
            self.result_display.setText(f"選擇的單一檔案:\n{file_path}\n\n使用的過濾器: {selected_filter}")
            print(f"File selected: {file_path}")

    def open_files(self):
        """開啟一個「選擇多個檔案」的對話框。"""
        file_filter = "Python 檔案 (*.py);;所有檔案 (*)"
        # getOpenFileNames 返回一個元組 (選擇的檔案路徑列表, 選擇的過濾器)
        file_paths, selected_filter = QFileDialog.getOpenFileNames(
            self,
            "選擇多個檔案",
            ".", # 預設開啟當前目錄
            file_filter
        )

        if file_paths:
            self.result_display.setText(f"選擇的多個檔案:\n" + "\n".join(file_paths))
            print(f"Files selected: {file_paths}")

    def select_directory(self):
        """開啟一個「選擇目錄」的對話框。"""
        # getExistingDirectory 返回選擇的目錄路徑
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "選擇一個目錄",
            QDir.homePath()
        )

        if dir_path:
            self.result_display.setText(f"選擇的目錄:\n{dir_path}")
            print(f"Directory selected: {dir_path}")

    def save_file(self):
        """開啟一個「儲存檔案」的對話框。"""
        file_filter = "文字檔案 (*.txt);;Markdown (*.md)"
        # getSaveFileName 返回一個元組 (使用者輸入的檔案路徑, 選擇的過濾器)
        file_path, selected_filter = QFileDialog.getSaveFileName(
            self,
            "儲存檔案為",
            QDir.homePath() + "/untitled.txt", # 預設檔名
            file_filter
        )

        if file_path:
            self.result_display.setText(f"準備儲存到:\n{file_path}")
            print(f"File to save: {file_path}")
            # 在真實應用中，接下來會執行實際的檔案寫入操作
            # with open(file_path, 'w') as f:
            #     f.write("Hello, world!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QFileDialogExample()
    window.show()
    sys.exit(app.exec())
