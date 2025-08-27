import sys
import os
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel, QHBoxLayout, QPushButton
)
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# --- 解決 Matplotlib 中文顯示問題 (保持不變) ---
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


# {{ modifications, a C-style code block }}
# - class Matplotlib2DCanvas(FigureCanvas):
# -     """一個用於顯示 2D 圖形的 Matplotlib 畫布元件。"""
# -     def __init__(self, parent=None, width=5, height=4, dpi=100):
# -         self.figure = Figure(figsize=(width, height), dpi=dpi)
# -         super().__init__(self.figure)
# -         self.setParent(parent)
# -         self.ax = self.figure.add_subplot(111)
# - 
# -     def plot(self, x, y, title='2D 函數圖', xlabel='X 軸', ylabel='Y 軸'):
# -         """繪製 2D 線圖。"""
# -         self.ax.clear()
# -         self.ax.plot(x, y, '.-')
# -         self.ax.set_title(title, fontproperties=cn_font if cn_font else None)
# -         self.ax.set_xlabel(xlabel, fontproperties=cn_font if cn_font else None)
# -         self.ax.set_ylabel(ylabel, fontproperties=cn_font if cn_font else None)
# -         self.ax.grid(True)
# -         self.draw()
# + 重構 Canvas 以專門繪製熱圖
class Matplotlib2DCanvas(FigureCanvas):
    """一個用於顯示 2D 熱圖的 Matplotlib 畫布元件。"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.figure)
        self.setParent(parent)
        # ax 在每次繪圖時重新創建，以處理 colorbar
        self.ax = None

    def plot_heatmap(self, data, title='2D 熱圖', xlabel='X 軸', ylabel='Y 軸'):
        """繪製 2D 熱圖，並穩健地處理重繪。"""
        # 清除整個 Figure 以避免舊的 colorbar 殘留
        self.figure.clear()
        
        # 重新添加 subplot
        self.ax = self.figure.add_subplot(111)
        
        # 繪製熱圖
        im = self.ax.imshow(data, cmap='viridis', interpolation='nearest')
        
        # 添加顏色條
        self.figure.colorbar(im, ax=self.ax)
        
        self.ax.set_title(title, fontproperties=cn_font if cn_font else None)
        self.ax.set_xlabel(xlabel, fontproperties=cn_font if cn_font else None)
        self.ax.set_ylabel(ylabel, fontproperties=cn_font if cn_font else None)
        
        self.draw()
# {{ end modifications }}


class Matplotlib2DExample(QWidget):
    """展示如何在 PySide6 中嵌入可互動的 Matplotlib 2D 熱圖。"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Matplotlib 2D 範例 - 網格精度與隨機數據")
        
        self.canvas = Matplotlib2DCanvas(self)
# {{ modifications, a C-style code block }}
# -         self.x_data = None
# -         self.y_base = None
# + # 移除不再需要的數據屬性
# {{ end modifications }}
        
        # --- 控制元件 ---
        self.precision_slider = QSlider(Qt.Horizontal)
        self.precision_slider.setMinimum(10)
        self.precision_slider.setMaximum(500)
        self.precision_slider.setValue(100)
# {{ modifications, a C-style code block }}
# -         self.precision_label = QLabel(f"繪圖點數: {self.precision_slider.value()}")
# + # 更新標籤文本以反映新功能
        self.precision_label = QLabel(f"網格精度: {self.precision_slider.value()}x{self.precision_slider.value()}")
# {{ end modifications }}

        self.refresh_button = QPushButton("刷新隨機數據")

        # --- 佈局 (保持不變) ---
        controls_layout = QVBoxLayout()
        
        precision_layout = QHBoxLayout()
        precision_layout.addWidget(QLabel("低"))
        precision_layout.addWidget(self.precision_slider)
        precision_layout.addWidget(QLabel("高"))
        controls_layout.addLayout(precision_layout)
        controls_layout.addWidget(self.precision_label, alignment=Qt.AlignCenter)
        controls_layout.addWidget(self.refresh_button)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(controls_layout)

        # --- 信號連接 (保持不變) ---
        self.precision_slider.valueChanged.connect(self.update_plot_precision)
        self.refresh_button.clicked.connect(self.plot_random_noise)
        
        # --- 初始繪製 (調用不變，但功能已更新) ---
        self.update_plot_precision(self.precision_slider.value())

# {{ modifications, a C-style code block }}
# -     def update_plot_precision(self, num_points):
# -         """根據滑桿的值更新繪圖精度並重繪基準圖形。"""
# -         self.precision_label.setText(f"繪圖點數: {num_points}")
# - 
# -         self.x_data = np.linspace(0, 4 * np.pi, num_points)
# -         self.y_base = np.sin(self.x_data)
# -         
# -         self.canvas.plot(self.x_data, self.y_base, title='基準正弦曲線')
# + # 重構此方法以生成和繪製熱圖
    def update_plot_precision(self, grid_size):
        """根據滑桿的值更新網格精度並繪製新的熱圖。"""
        self.precision_label.setText(f"網格精度: {grid_size}x{grid_size}")

        # 生成二維隨機數據
        data = np.random.rand(grid_size, grid_size)
        
        self.canvas.plot_heatmap(data, title='隨機數據熱圖')
# {{ end modifications }}

# {{ modifications, a C-style code block }}
# -     def plot_random_noise(self):
# -         """在基準數據上添加隨機噪聲並重繪。"""
# -         if self.y_base is None:
# -             return
# -         
# -         # 添加一些隨機噪聲
# -         noise = np.random.normal(0, 0.2, self.y_base.shape)
# -         y_noisy = self.y_base + noise
# -         
# -         self.canvas.plot(self.x_data, y_noisy, title='帶有噪聲的正弦曲線')
# + # 重構此方法以重用精度更新的邏輯來實現“刷新”
    def plot_random_noise(self):
        """重新生成一個全新的隨機熱圖。"""
        # 只需使用當前滑桿的值調用更新函數即可
        self.update_plot_precision(self.precision_slider.value())
# {{ end modifications }}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Matplotlib 2D 獨立執行範例")
    main_window.setCentralWidget(Matplotlib2DExample())
    main_window.resize(600, 500)
    main_window.show()
    sys.exit(app.exec())