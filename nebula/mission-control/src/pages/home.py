from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("NebulaOS")
        subtitle = QLabel("Customize Your Universe.")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        self.setLayout(layout)
