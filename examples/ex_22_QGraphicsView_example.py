import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsEllipseItem,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtGui import QColor, QBrush, QPen, QFont, QPainter
from PySide6.QtCore import Qt


class QGraphicsViewExample(QWidget):
    """
    一個展示 QGraphicsView 框架基礎功能的範例。
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2D 圖形視圖 (QGraphicsView) 範例")
        self.setGeometry(300, 300, 600, 500)

        # 1. 創建一個場景 (Scene)
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(-250, -250, 500, 500) # 設定場景邊界

        # 2. 在場景中添加圖形項 (Graphics Items)
        self.add_items_to_scene()

        # 3. 創建一個視圖 (View) 來顯示場景
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing) # 啟用反鋸齒，使圖形更平滑
        self.view.setDragMode(QGraphicsView.RubberBandDrag) # 設定拖曳模式為橡皮筋選擇

        # 創建佈局
        layout = QVBoxLayout(self)
        info_label = QLabel("你可以拖曳、選取、縮放這些圖形物件。")
        info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(info_label)
        layout.addWidget(self.view)

    def add_items_to_scene(self):
        """向場景中添加多個可互動的圖形物件。"""
        # 紅色可移動矩形
        rect_item = QGraphicsRectItem(0, 0, 100, 100)
        rect_item.setPos(-150, -50)
        rect_item.setBrush(QBrush(QColor("red")))
        rect_item.setPen(QPen(Qt.black, 2))
        rect_item.setFlags(QGraphicsRectItem.ItemIsMovable | QGraphicsRectItem.ItemIsSelectable)
        self.scene.addItem(rect_item)

        # 藍色可移動、可縮放圓形
        ellipse_item = QGraphicsEllipseItem(0, 0, 120, 80)
        ellipse_item.setPos(50, 50)
        ellipse_item.setBrush(QBrush(QColor("blue")))
        ellipse_item.setFlags(QGraphicsRectItem.ItemIsMovable | QGraphicsRectItem.ItemIsSelectable)
        self.scene.addItem(ellipse_item)
        
        # 綠色固定文字
        text_item = self.scene.addText("固定的文字", QFont("Arial", 16))
        text_item.setPos(-240, -240)
        text_item.setDefaultTextColor(QColor("darkgreen"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QGraphicsViewExample()
    window.show()
    sys.exit(app.exec())