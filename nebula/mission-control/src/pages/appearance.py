from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class AppearancePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Appearance")
        description = QLabel("Themes, colors, wallpapers and customization.")

        layout.addWidget(title)
        layout.addWidget(description)

        self.setLayout(layout)
