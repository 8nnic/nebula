from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        buttons = [
            "🏠 Home",
            "🎨 Appearance",
            "🖥 Desktop",
            "🛰 Widgets",
            "⚡ Performance"
        ]

        for text in buttons:
            button = QPushButton(text)
            layout.addWidget(button)

        layout.addStretch()

        self.setLayout(layout)
