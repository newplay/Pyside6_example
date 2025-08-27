import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QPoint


class MovableLabel(QLabel):
    """
    一個可以透過滑鼠拖曳移動的 QLabel。
    """
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.SizeAllCursor)
        self._mouse_press_pos = None
        self._mouse_move_pos = None

    def mousePressEvent(self, event):
        """當滑鼠按下時，記錄下當前滑鼠的相對位置和絕對位置。"""
        if event.button() == Qt.LeftButton:
            self._mouse_press_pos = event.globalPosition().toPoint()
            self._mouse_move_pos = event.globalPosition().toPoint()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """當滑鼠移動時，如果左鍵被按住，則移動標籤。"""
        if event.buttons() == Qt.LeftButton:
            # 計算滑鼠移動的距離
            curr_pos = event.globalPosition().toPoint()
            delta = curr_pos - self._mouse_move_pos
            
            # 移動標籤
            new_pos = self.pos() + delta
            self.move(new_pos)
            
            # 更新滑鼠位置
            self._mouse_move_pos = curr_pos
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """當滑鼠釋放時，重置位置記錄。"""
        if event.button() == Qt.LeftButton:
            self._mouse_press_pos = None
            self._mouse_move_pos = None
        super().mouseReleaseEvent(event)


class MovableLabelExample(QWidget):
    """
    一個展示可移動 QLabel 的範例視窗。
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("可移動標籤範例")
        self.setGeometry(300, 300, 500, 400)

        # 在這個範例中，我們不使用佈局管理器，
        # 以便自由地移動標籤。
        self.label1 = MovableLabel("拖動我！", self)
        self.label1.setGeometry(50, 50, 100, 30)
        self.label1.setStyleSheet("border: 1px solid black; background-color: lightblue;")

        self.label2 = MovableLabel("我也能動！", self)
        self.label2.setGeometry(200, 150, 100, 30)
        self.label2.setStyleSheet("border: 1px solid black; background-color: lightgreen;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovableLabelExample()
    window.show()
    sys.exit(app.exec())
