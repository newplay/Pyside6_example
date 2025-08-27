import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QLabel,
    QHeaderView,
)
from PySide6.QtCore import Qt


class QTreeWidgetExample(QWidget):
    """
    一個展示 QTreeWidget 功能的範例。

    這個視窗包含：
    - 一個 QTreeWidget，顯示一個包含多個欄位的檔案系統結構。
    - 一個 QLabel，用於顯示當前選中項目的詳細資訊。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeWidget 範例")
        self.setGeometry(300, 300, 600, 400)

        # 創建元件
        self.tree_widget = QTreeWidget()
        self.info_label = QLabel("請選擇一個樹節點")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 設定樹
        self.setup_tree()

        # 設定佈局
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.tree_widget)
        main_layout.addWidget(self.info_label)

        # 連接信號
        self.tree_widget.currentItemChanged.connect(self.on_item_changed)

    def setup_tree(self):
        """初始化樹的結構和內容。"""
        # 1. 設定欄位數量和標頭
        self.tree_widget.setColumnCount(3)
        self.tree_widget.setHeaderLabels(["名稱", "類型", "大小"])

        # 2. 調整標頭外觀
        self.tree_widget.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tree_widget.header().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.tree_widget.header().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        # 3. 創建根節點
        root_item = QTreeWidgetItem(self.tree_widget, ["/home/user", "目錄", "4.0 KB"])
        
        # 4. 添加子節點
        # 第一層子節點
        docs_item = QTreeWidgetItem(root_item, ["Documents", "目錄", "1.2 MB"])
        pics_item = QTreeWidgetItem(root_item, ["Pictures", "目錄", "5.8 GB"])
        config_file = QTreeWidgetItem(root_item, [".profile", "檔案", "807 B"])

        # 第二層子節點 (在 Documents 底下)
        report_doc = QTreeWidgetItem(docs_item, ["report.docx", "檔案", "512 KB"])
        notes_txt = QTreeWidgetItem(docs_item, ["notes.txt", "檔案", "1.2 KB"])

        # 第二層子節點 (在 Pictures 底下)
        vacation_folder = QTreeWidgetItem(pics_item, ["Vacation", "目錄", "2.1 GB"])
        cat_jpg = QTreeWidgetItem(pics_item, ["cat.jpg", "檔案", "800 KB"])
        
        # 第三層子節點
        beach_jpg = QTreeWidgetItem(vacation_folder, ["beach.jpg", "檔案", "1.5 MB"])

        # 預設展開根節點
        self.tree_widget.expandItem(root_item)
        self.tree_widget.expandItem(pics_item)

    def on_item_changed(self, current, previous):
        """當選中項目改變時，更新標籤。"""
        if not current:
            return

        # 獲取所有欄位的數據
        name = current.text(0)
        item_type = current.text(1)
        size = current.text(2)

        # 獲取節點的完整路徑
        path_parts = [name]
        parent = current.parent()
        while parent:
            path_parts.insert(0, parent.text(0))
            parent = parent.parent()
        
        full_path = "/".join(path_parts)

        self.info_label.setText(
            f"選中: {name} | 類型: {item_type} | 大小: {size}\n"
            f"完整路徑: {full_path}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QTreeWidgetExample()
    window.show()
    sys.exit(app.exec())
