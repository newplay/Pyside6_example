
import sys
import os
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel, QHBoxLayout, QPushButton
)
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# --- 解決 Matplotlib 中文顯示問題 ---
try:
    from matplotlib.font_manager import FontProperties
    import platform
    system = platform.system()
    if system == 'Windows':
        font_path = 'C:/Windows/Fonts/simhei.ttf'
        cn_font = FontProperties(fname=font_path)
    elif system == 'Darwin': # macOS
        cn_font = FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')
    else: # Linux
        font_paths = [
            '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
            '/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc',
            '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
        ]
        font_found = False
        for path in font_paths:
            if os.path.exists(path):
                cn_font = FontProperties(fname=path)
                font_found = True
                break
        if not font_found:
            raise FileNotFoundError()
except (FileNotFoundError, ImportError):
    cn_font = None

if cn_font:
    import matplotlib
    matplotlib.rcParams['font.sans-serif'] = [cn_font.get_name()]
    matplotlib.rcParams['axes.unicode_minus'] = False


class Matplotlib3DCanvas(FigureCanvas):
    """一個用於顯示 3D 圖形的 Matplotlib 畫布元件。"""
    def __init__(self, parent=None, width=8, height=6, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.figure)
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111, projection='3d')

    def plot(self, X, Y, Z):
        """繪製 3D 曲面圖。"""
        self.ax.clear()
        self.ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        self.ax.set_title("3D 曲面圖 (可互動)", fontproperties=cn_font if cn_font else None)
        self.ax.set_xlabel("X 軸")
        self.ax.set_ylabel("Y 軸")
        self.ax.set_zlabel("Z 軸")
        self.draw()


class Matplotlib3DExample(QWidget):
    """展示如何在 PySide6 中嵌入可互動的 Matplotlib 3D 圖表。"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Matplotlib 3D 範例")
        
        self.canvas = Matplotlib3DCanvas(self)
        self.X = None
        self.Y = None
        self.Z_base = None

        # --- 控制元件 ---
        self.resolution_slider = QSlider(Qt.Horizontal)
        self.resolution_slider.setMinimum(10)
        self.resolution_slider.setMaximum(100)
        self.resolution_slider.setValue(25)
        self.resolution_label = QLabel(f"解析度: {self.resolution_slider.value()}x{self.resolution_slider.value()} Grid")
        self.refresh_button = QPushButton("刷新隨機數據")

        # --- 佈局 ---
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(QLabel("低"))
        slider_layout.addWidget(self.resolution_slider)
        slider_layout.addWidget(QLabel("高"))

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(slider_layout)
        main_layout.addWidget(self.resolution_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.refresh_button)

        # --- 信號連接 ---
        self.resolution_slider.valueChanged.connect(self.update_plot_resolution)
        self.refresh_button.clicked.connect(self.plot_random_noise)
        
        # --- 初始繪製 ---
        self.update_plot_resolution(self.resolution_slider.value())

    def update_plot_resolution(self, value):
        """根據滑桿的值更新 3D 圖形的網格和基礎數據。"""
        step = 1.0 / (value / 10.0)
        self.resolution_label.setText(f"解析度: {int(10/step)}x{int(10/step)} Grid (步長: {step:.2f})")

        X_new = np.arange(-5, 5, step)
        Y_new = np.arange(-5, 5, step)
        if len(X_new) < 2 or len(Y_new) < 2:
            return
            
        self.X, self.Y = np.meshgrid(X_new, Y_new)
        R = np.sqrt(self.X**2 + self.Y**2)
        self.Z_base = np.sin(R)
        self.canvas.plot(self.X, self.Y, self.Z_base)

    def plot_random_noise(self):
        """在現有曲面上添加隨機噪聲並重繪。"""
        if self.Z_base is None:
            return
        # 添加一些隨機噪聲
        noise = np.random.normal(0, 0.1, self.Z_base.shape)
        Z_noisy = self.Z_base + noise
        self.canvas.plot(self.X, self.Y, Z_noisy)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Matplotlib 3D 獨立執行範例")
    main_window.setCentralWidget(Matplotlib3DExample())
    main_window.resize(800, 700)
    main_window.show()
    sys.exit(app.exec())
