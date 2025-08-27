import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
)


class VBoxLayoutHBoxLayoutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("基礎佈局 (VBox & HBox) 範例")
        self.setGeometry(300, 300, 400, 300)

        main_layout = QVBoxLayout(self)

        hbox_group = QGroupBox("QHBoxLayout (水平排列)")
        hbox_group.setObjectName("hbox_group")
        h_layout = QHBoxLayout()
        h_layout.addWidget(QPushButton("按鈕 H1"))
        h_layout.addWidget(QPushButton("按鈕 H2"))
        h_layout.addWidget(QPushButton("按鈕 H3"))
        hbox_group.setLayout(h_layout)
        
        vbox_group = QGroupBox("QVBoxLayout (垂直排列)")
        vbox_group.setObjectName("vbox_group")
        v_layout = QVBoxLayout()
        v_layout.addWidget(QPushButton("按鈕 V1"))
        v_layout.addWidget(QPushButton("按鈕 V2"))
        v_layout.addWidget(QPushButton("按鈕 V3"))
        vbox_group.setLayout(v_layout)

        nested_group = QGroupBox("巢狀佈局 (HBox 內含 VBox)")
        nested_group.setObjectName("nested_group")
        outer_h_layout = QHBoxLayout()
        
        left_v_layout = QVBoxLayout()
        left_v_layout.addWidget(QPushButton("左上"))
        left_v_layout.addWidget(QPushButton("左下"))
        
        right_v_layout = QVBoxLayout()
        right_v_layout.addWidget(QPushButton("右上"))
        right_v_layout.addWidget(QPushButton("右下"))
        
        outer_h_layout.addLayout(left_v_layout)
        outer_h_layout.addWidget(QPushButton("中間的按鈕"))
        outer_h_layout.addLayout(right_v_layout)
        
        nested_group.setLayout(outer_h_layout)

        main_layout.addWidget(hbox_group)
        main_layout.addWidget(vbox_group)
        main_layout.addWidget(nested_group)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VBoxLayoutHBoxLayoutExample()
    window.show()
    sys.exit(app.exec())