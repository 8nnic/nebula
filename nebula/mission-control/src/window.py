from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
)

from widgets.card import Card


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mission Control")
        self.resize(1100, 700)

        mainLayout = QVBoxLayout()

        title = QLabel("Mission Control")
        title.setObjectName("title")

        subtitle = QLabel("Customize Your Universe.")
        subtitle.setObjectName("subtitle")

        grid = QGridLayout()

        grid.addWidget(Card("🎨 Appearance", "Themes, colors and fonts"), 0, 0)
        grid.addWidget(Card("🛰 Widgets", "Desktop widgets"), 0, 1)
        grid.addWidget(Card("🖥 Desktop", "Panels and layouts"), 1, 0)
        grid.addWidget(Card("⚡ Performance", "System tweaks"), 1, 1)

        mainLayout.addWidget(title)
        mainLayout.addWidget(subtitle)
        mainLayout.addSpacing(25)
        mainLayout.addLayout(grid)

        self.setLayout(mainLayout)
