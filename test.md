### 分析報告

#### 1. 任務目標與核心需求 (Task Goal & Core Requirements)
本次任務的核心目標是創建一個 PySide6 的教學範例集合。此集合需具備高度的結構化、完整性與可執行性。根據您的要求，每個範例模組都必須包含六個核心部分：
- **簡介 (Introduction)**: 解釋元件用途。
- **原始碼 (Source Code)**: 提供完整、可獨立運行的 Python 程式碼。
- **效果展示 (Effect Demonstration)**: 使用文字或 ASCII 藝術模擬 GUI 介面。
- **互動說明 (Interaction Explanation)**: 描述使用者操作與程式回應的因果關係。
- **參數影響 (Parameter Influence)**: 闡述關鍵參數如何改變元件行為。
- **延伸應用 (Extended Application)**: 提出元件組合的可能性。

#### 2. 技術組件拆解 (Technical Component Breakdown)
任務涵蓋的 PySide6 組件已被明確定義，可分為兩大類：

- **元件 (Widgets)**:
    - `QLabel`, `QPushButton`
    - `QLineEdit`, `QTextEdit`
    - `QCheckBox`, `QRadioButton`
    - `QComboBox`
    - `QListWidget`, `QTableWidget`, `QTreeWidget`
    - `QSlider`, `QDial`
    - `QProgressBar`
    - `QTabWidget`
    - `QMessageBox`
    - `QFileDialog`
    - `QColorDialog`, `QFontDialog`
    - `QMenuBar`, `QToolBar`, `QStatusBar`

- **佈局 (Layouts)**:
    - `QVBoxLayout`, `QHBoxLayout`
    - `QGridLayout`
    - `QFormLayout`
    - `QStackedLayout`

#### 3. 系統架構與關鍵約束 (System Architecture & Key Constraints)
- **獨立執行單元**: 每個範例都將被設計成一個獨立的 Python 腳本，包含完整的 `QApplication` 生命週期管理，確保使用者可以直接複製並執行。
- **基底視窗選擇**:
    - 大多數範例將使用 `QWidget` 作為基礎視窗容器，以保持範例的簡潔性。
    - 針對 `QMenuBar`, `QToolBar`, `QStatusBar` 的範例，必須使用 `QMainWindow` 作為基礎視窗，因為這些元件是 `QMainWindow` 的原生組成部分。這是一個關鍵的架構決策。
- **程式碼風格**: 所有 Python 程式碼將嚴格遵循 PEP 8 編碼規範。
- **互動性**: 每個範例的程式碼都將包含必要的信號與槽 (signals & slots) 連接，以展示元件的真實互動效果，而不僅僅是靜態展示。

#### 4. 已知與未知元素 (Knowns & Unknowns)
- **已知**:
    - 需要涵蓋的完整元件與佈局清單。
    - 每個範例必須包含的六大說明區塊。
    - 輸出格式為逐一產出，而非單一文件。
- **未知/待處理**:
    - `QTableWidget` 和 `QTreeWidget` 的範例可能較為複雜，需要在展示核心功能的同時保持程式碼的簡潔易懂，這是一個需要權衡的點。
    - 為了讓範例之間更有連貫性，可以考慮設計一個微型主題，但目前將優先確保每個範例的獨立清晰性。

#### 方案一：標準互動模式 (Standard Interactive Pattern)

此方案為所有範例建立一個基礎互動模型，確保一致性與易理解性。

- **描述**: 每個範例將圍繞一個核心的「輸入 -> 處理 -> 輸出」循環來設計。例如，`QLineEdit` (輸入) 的文字可以透過 `QPushButton` (處理) 的點擊事件，最終顯示在 `QLabel` (輸出) 上。這種模式清晰地展示了元件之間如何通過信號與槽進行通信。
- **優點**:
    - **一致性高**: 使用者可以快速掌握每個範例的結構。
    - **教學效果好**: 清晰地演示了 GUI 程式設計的核心概念——事件驅動。
    - **易於擴展**: 可以在此基礎上輕鬆組合更多元件。
- **缺點**: 對於某些純展示性元件（如 `QProgressBar`），可能需要稍微調整模式，例如由 `QSlider` 或計時器作為輸入源。

#### 方案二：即時參數切換模式 (Real-time Parameter Toggling Pattern)

此方案旨在讓「參數影響」部分變得更具互動性，而不僅僅是文字描述。

- **描述**: 在主範例視窗中，額外增加一些控制元件（如 `QCheckBox` 或 `QRadioButton`），用來即時切換被展示元件的關鍵參數。例如，在 `QLabel` 範例中，可以放幾個複選框來控制文字是否 `setWordWrap(True)` 或改變對齊方式 `setAlignment()`，使用者勾選後能立即看到 `QLabel` 的外觀變化。
- **優點**:
    - **學習體驗極佳**: 使用者可以即時看到參數改變後的效果，加深理解。
    - **探索性強**: 鼓勵使用者嘗試不同的參數組合。
- **缺點**:
    - **程式碼稍複雜**: 需要額外編寫控制參數的邏輯。
    - **介面可能變擁擠**: 需要在有限的空間內放置更多控制元件。

#### 方案三：情境模擬模式 (Scenario Simulation Pattern)

此方案將範例融入一個微型應用情境中，使其更貼近實際應用。

- **描述**: 與其孤立地展示一個按鈕，不如將其放入一個「使用者登入表單」或「設定對話框」的迷你情境中。例如，`QFormLayout` 的範例可以是一個完整的「使用者註冊」表單，包含 `QLineEdit`、`QCheckBox` 等。
- **優點**:
    - **實用性強**: 展示了元件在真實世界中的應用方式。
    - **更有趣**: 故事性的情境能提高學習者的興趣。
- **缺點**:
    - **焦點可能分散**: 使用者可能需要花更多時間理解業務邏輯，而非元件本身。
    - **設計成本高**: 需要為每個範例構思一個合理的微型情境。

#### 最終決策

我們將融合 **方案一** 和 **方案二** 作為核心設計策略。

1.  **以「標準互動模式」為骨架**: 確保每個範例都有一個清晰、核心的互動功能。
2.  **以「即時參數切換模式」為血肉**: 在適當的情況下（特別是對於外觀和行為參數多的元件），加入即時控制項，讓使用者可以動態調整參數並觀察結果。

這種混合方法可以在確保教學核心清晰的同時，提供豐富的互動性和探索性，從而達到最佳的學習效果。例如，`QPushButton` 範例不僅會點擊改變文字，還會提供一個 `QCheckBox` 來動態啟用/禁用 (Enable/Disable) 按鈕，或切換其 `checkable` 屬性。

### 實作計劃報告

#### 1. 整體架構
本計畫將按照「先基礎元件，後複合元件，再佈局管理」的順序，逐一生成教學範例。每個範例都將嚴格遵循 INNOVATE 階段確定的「標準互動模式」 + 「即時參數切換模式」的混合策略。

#### 2. 產出內容規格
每個範例模組的輸出將包含以下六個部分的完整內容：
1.  **簡介**: 用途說明。
2.  **原始碼**: 遵循 PEP 8 的完整可執行程式碼。
3.  **效果展示**: ASCII 藝術模擬圖。
4.  **互動說明**: 信號與槽的行為解釋。
5.  **參數影響**: 結合程式碼中的即時切換功能進行說明。
6.  **延伸應用**: 與其他元件的組合建議。

#### 3. 實作檢查清單 (Implementation Checklist)

以下是按順序生成的範例清單，每個項目都是一個獨立的、完整的任務單元。

**第一部分：基礎元件**
1.  **生成 `QLabel` 範例**:
    - **核心互動**: 使用 `QPushButton` 點擊後更新 `QLabel` 的文字。
    - **參數展示**: 使用 `QCheckBox` 動態切換 `QLabel` 的 `setWordWrap` (自動換行) 屬性。
    - **效果模擬**: 展示初始、點擊後、啟用換行後的不同狀態。
2.  **生成 `QPushButton` 範例**:
    - **核心互動**: 按鈕點擊後，在終端或一個 `QLabel` 上計數。
    - **參數展示**: 使用 `QCheckBox` 動態切換按鈕的 `setEnabled` (啟用/禁用) 狀態和 `setCheckable` (可勾選) 狀態。
3.  **生成 `QLineEdit` 範例**:
    - **核心互動**: `QLineEdit` 的 `textChanged` 信號即時將內容同步到一個 `QLabel` 上。
    - **參數展示**: 使用 `QComboBox` 動態切換 `setEchoMode` (正常、密碼、靜默)。
4.  **生成 `QTextEdit` 範例**:
    - **核心互動**: 一個按鈕獲取 `QTextEdit` 的純文字內容，另一個按鈕獲取 HTML 內容，並顯示在 `QLabel` 中。
    - **參數展示**: 使用 `QCheckBox` 切換 `setReadOnly` 屬性。
5.  **生成 `QCheckBox` / `QRadioButton` 範例**:
    - **核心互動**: `QCheckBox` 的狀態改變 (stateChanged) 會更新一個 `QLabel`。一組 `QRadioButton` 中只有一個能被選中，選中項會更新同一個 `QLabel`。
    - **參數展示**: 展示 `setTristate` (三態複選框) 的效果。

**第二部分：選擇與數值元件**
6.  **生成 `QComboBox` 範例**:
    - **核心互動**: 當使用者在下拉列表中選擇一個新項目時，`currentTextChanged` 信號會更新一個 `QLabel`。
    - **參數展示**: 使用 `QCheckBox` 切換 `setEditable` 屬性，允許使用者輸入自訂項目。
7.  **生成 `QSlider` / `QDial` 範例**:
    - **核心互動**: 拖動 `QSlider` 或 `QDial` 時，其 `valueChanged` 信號會即時更新一個 `QLabel` 顯示當前數值，並同步更新一個 `QProgressBar` 的進度。
8.  **生成 `QProgressBar` 範例**:
    - **核心互動**: 使用 `QSlider` 控制進度條的展示（已在上一項中合併）。此處將展示由 `QTimer` 控制的自動進度條。
    - **參數展示**: 按鈕可以重置進度條，並切換其 `textVisible` 屬性。

**第三部分：容器與複合元件**
9.  **生成 `QListWidget` / `QTableWidget` / `QTreeWidget` 範例**: (將拆分為三個獨立範例)
    - **`QListWidget`**: 核心互動是新增、刪除列表項，並在選中項改變時更新 `QLabel`。
    - **`QTableWidget`**: 核心互動是動態填充表格數據，點擊單元格時獲取其內容。
    - **`QTreeWidget`**: 核心互動是構建一個多級樹狀結構，並在點擊節點時顯示節點資訊。
10. **生成 `QTabWidget` 範例**:
    - **核心互動**: 包含數個分頁，每個分頁有不同內容。切換分頁時，`currentChanged` 信號會更新 `QStatusBar` 的訊息。

**第四部分：對話框**
11. **生成 `QMessageBox` 範例**:
    - **核心互動**: 點擊不同按鈕，彈出不同類型（Information, Question, Warning, Critical）的訊息框。
12. **生成 `QFileDialog` 範例**:
    - **核心互動**: 一個按鈕打開「檔案選擇」對話框，並將選擇的檔案路徑顯示在 `QLineEdit` 中。另一個按鈕打開「檔案儲存」對話框。
13. **生成 `QColorDialog` / `QFontDialog` 範例**:
    - **核心互動**: 按鈕分別彈出顏色選擇和字體選擇對話框，並將選擇結果應用於一個 `QLabel` 的背景色和字體上。

**第五部分：主視窗元件**
14. **生成 `QMenuBar` / `QToolBar` / `QStatusBar` 範例**:
    - **核心互動**: 在 `QMainWindow` 中創建菜單、工具欄和狀態欄。點擊菜單項或工具欄按鈕 (`QAction`) 會在狀態欄顯示提示訊息。

**第六部分：佈局管理**
15. **生成 `QVBoxLayout` / `QHBoxLayout` 範例**:
    - **核心互動**: 展示如何垂直和水平排列多個 `QPushButton`。
16. **生成 `QGridLayout` 範例**:
    - **核心互動**: 將多個按鈕放置在一個 3x3 的網格中，展示跨行跨列的用法。
17. **生成 `QFormLayout` 範例**:
    - **核心互動**: 創建一個典型的表單，包含標籤和輸入框（`QLabel` + `QLineEdit`）。
18. **生成 `QStackedLayout` 範例**:
    - **核心互動**: 使用 `QComboBox` 或 `QListWidget` 來切換 `QStackedLayout` 中顯示的不同頁面（`QWidget`）。

